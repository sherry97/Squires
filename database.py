from pymongo import MongoClient
import scrapy

class Worker():
    def __init__(self, name, url, skills):
        self.name = name
        self.url = url
        self.skills = skills


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
        skillMatch = len(list(set(skills) & set(document.skills)))//len(skills)
        if (skillMatch >= skillMatchThreshold):
            w.append(Worker(document.name, document.url, document.skills))

    return w

def displayToForm(lst):
    for l in lst:
        print("name: "+l.name+" || URL: "+l.url+" || skills: "+l.skills)

def main():
    client = MongoClient()
    db = client.test
    # filler data
    addToDB(db, "Steve Rogers", "avengers.com/cap", ["shield throwing", "Java", "vigilante justice"], "20055")
    addToDB(db, "Natasha Romanov", "avengers.com/widow", ["assassination", "snark", "CSS"], "20055")
    addToDB(db, "Sam Wilson", "avengers.com/falcon", ["bird suit", "Java", "HTML", "CSS"], "20055")
    skills = ["CSS", "HTML", "Java"]
    zipcode = "20055"
    skillMatchThreshold = 0.5
    matchedWorkers = searchDB(db, skills, zipcode, skillMatchThreshold)
    if (len(matchedWorkers) < 10):
        # new scrape
        # add to DB
        pass

    displayToForm(w);

if __name__ == '__main__': main()