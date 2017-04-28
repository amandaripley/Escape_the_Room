import json

def openfile(mytime):
    besttime = open("besttime.json", "r").read()
    mydictionary = json.loads(besttime)

    for key in mydictionary:
        mykey = mydictionary[key]

    if(mytime <= mykey):
        print("Your time was:", mytime, "That was your best time!")
        besttime = open("besttime.json", "w")
        mynewdictionary = {"The best time is": mytime}
        towrite = json.dumps(mynewdictionary)
        besttime.write(towrite)
        besttime.close()

    else:
        print("Try again for a better time!")
