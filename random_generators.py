from random import randint as rand
import json
def read_data():
    #a function that simply returns the data file as a json object
    with open("rg-data.json") as datafile:
        data = json.load(datafile)
    return data
    

def gender():
    #return a random gender from genders
    return read_data()["genders"][rand(0, 1)]
   
def name(gender):
    #hold both sex names in a var to avoid duplicated file opening calls to figure out len()
    names = read_data()["names"]

    if(gender == "male"):
        #return random male name
        return names["male"][rand(0, len(names["male"])-1)]

    elif(gender == "female"):
        #return random female name
        return names["female"][rand(0, len(names["female"])-1)]

def randint(min, max):
    #just random 0 - 100 for traits
    return rand(min, max)

def acquaintance_name():
    names = read_data()["acquaintance_names"]
    return names[rand(0, len(names)-1)]
