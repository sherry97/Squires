#!/usr/bin/env python
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
def added():
    parts = bottle.request.forms
    return parts.getunicode("skills")

def addToDB(db, name, url, skills, zipcode):
    result = db.workers.insert_one(
        {
            "name" : name,
            "URL" : url,
            "skills" : skills,
            "zip" : zipcode
        }
    )    

def searchDB(db, skills, zipcode, skillMatchThreshold):
    w = []

    cursor = db.workers.find({"zip" : zipcode})
    for document in cursor:
        skillMatch = len(list(set(skills) & set(document['skills'])))/len(skills)
        if skillMatch >= skillMatchThreshold:
            try:
                # print(document)
                w.append(Worker(document['name'], document['URL'], document['skills']))
            except KeyError:
                continue
    return w

def displayToForm(lst):
    for l in lst:
        print(l.name+"\t"+l.url)
        print(l.skills)

def main():
    bottle.debug(True)
    bottle.run(host='0.0.0.0', port=8090)

    client = MongoClient()
    db = client.test
    # filler data
    addToDB(db, "Steve Rogers", "avengers.com/cap", ["shield throwing", "Java", "vigilante justice"], "20055")
    addToDB(db, "Natasha Romanov", "avengers.com/widow", ["assassination", "snark", "CSS"], "20055")
    addToDB(db, "Sam Wilson", "avengers.com/falcon", ["bird suit", "Java", "HTML", "CSS"], "20055")
    # /filler data
    skills = added()
    zipcode = "20055"
    skillMatchThreshold = 0.5
    matchedWorkers = searchDB(db, skills, zipcode, skillMatchThreshold)
    if (len(matchedWorkers) < 10):
        # new scrape
        # add to DB
        pass

    displayToForm(matchedWorkers);
    client.drop_database(db)

if __name__ == '__main__': main()