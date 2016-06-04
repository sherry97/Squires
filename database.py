from pymongo import MongoClient
import scrapy

class Worker():
    def __init__(self, name, url, skills):
        self.name = name
        self.url = url
        self.skills = skills


def addToDB(name, url, skills, zipcode):
    client = MongoClient()
    db = client.test
    result = db.workers.insert_one(
        {
            "name" : name,
            "URL" : url,
            "skills" : skills,
            "zip" : zipcode
        }
    )    

def searchDB(skills, zipcode, skillMatchThreshold):
    w = []

    client = MongoClient()
    db = client.test
    cursor = db.workers.find({"zip" : zipcode})
    for document in cursor:
        skillMatch = (double)len(skills & document.skills)/(double)len(skills)
        if (skillMatch >= skillMatchThreshold):
            w.append(Worker(document.name, document.url, document.skills))

    return w

def displayToForm(lst):
    for l in lst:
        print("name: "+l.name+" || URL: "+l.url+" || skills: "+l.skills)

def main():
    skills = ["CSS", "HTML", "Java"]
    zipcode = "20055"
    skillMatchThreshold = 0.5
    matchedWorkers = searchDB(skills, zipcode, skillMatchThreshold)
    if (len(matchedWorkers) < 10):
        # new scrape
        # add to DB
        pass

    displayToForm(w);

if __name__ == '__main__': main()