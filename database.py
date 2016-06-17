#!/usr/bin/env python
#   launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mongodb.plist
#   OR
#   brew services start mongodb
import bottle
from pymongo import MongoClient
import scrapy

class Worker():
    def __init__(self, name, url, skills):
        self.name = name
        self.url = url
        self.skills = skills

@bottle.get('/')
def index():
    return bottle.template('views/search.tpl')

@bottle.post('/searched')
def searched():
    parts = bottle.request.forms
    reqSkills = parts.getunicode("required_skills")
    prefSkills = parts.getunicode("preferred_skills")
    zipcode = parts.getunicode("zip")
    skillMatchThreshold = parts.getunicode("threshold")
    matchedWorkers = searchDB(db, reqSkills, prefSkills, zipcode, skillMatchThreshold)
    if (len(matchedWorkers) < 10):
        # new scrape
        # add to DB
        pass
    return bottle.template('views/output.tpl')

def addToDB(db, name, url, skills, zipcode):
    result = db.workers.insert_one(
        {
            "name" : name,
            "URL" : url,
            "skills" : skills,
            "zip" : zipcode
        }
    )    

def searchDB(db, reqSkills, prefSkills, zipcode, skillMatchThreshold):
    w = []

    cursor = db.workers.find({"zip" : zipcode})
    for document in cursor:
        if len(list(set(reqSkills) & set(document['skills']))) < len(reqSkills):
            continue
        skillMatch = len(list(set(prefSkills) & set(document['skills'])))/len(prefSkills)
        if skillMatch >= skillMatchThreshold:
            try:
                # print(document)
                w.append([Worker(document['name'], document['URL'], document['skills']), skillMatch])
            except KeyError:
                print('KeyError!')
                continue
    return w

def displayToForm(lst):
    for l, skillMatch in lst:
        print(l.name+"\t"+l.url+"\t"+str(skillMatch))
        print(l.skills)

    #   display to webpage

def main():
    bottle.debug(True)
    bottle.run(host='0.0.0.0', port=8090)

    client = MongoClient()
    db = client.test
    #
    #   filler data
    #
    addToDB(db, "Steve Rogers", "avengers.com/cap", ["shield throwing", "Java"], "20055")
    addToDB(db, "Natasha Romanov", "avengers.com/widow", ["assassination", "snark", "CSS"], "20055")
    addToDB(db, "Sam Wilson", "avengers.com/falcon", ["bird suit", "Java", "HTML", "CSS"], "20055")
    #
    #   /filler data
    #
    skills = searched()
    zipcode = "20055"
    skillMatchThreshold = 0.5
    matchedWorkers = searchDB(db, skills, zipcode, skillMatchThreshold)
    if (len(matchedWorkers) < 10):
        # new scrape
        # add to DB
        pass

    searched(matchedWorkers)
    client.drop_database(db)

if __name__ == '__main__': main()