import random
import math

def swapNames(data, percentage):
    sample = random.sample(data, math.floor(len(data) * percentage))
    for element in sample:
        temp = element['first_name']
        element['first_name'] = element['last_name']
        element['last_name'] = temp

def initialFirstName(data, percentage):
    sample = random.sample(data, math.floor(len(data) * percentage))
    for element in sample:
        element['first_name'] = element['first_name'][0]

def initialLastName(data, percentage):
    sample = random.sample(data, math.floor(len(data) * percentage))
    for element in sample:
        element['last_name'] = element['last_name'][0]

def deleteAttribute(data, percentage):
    sample = random.sample(data, math.floor(len(data) * percentage))
    for element in sample:
        i = random.randint(0, len(element) - 2)
        element[list(element)[i]] = ''

def shareAttributes(data, percentage):
    sample = random.sample(data, math.floor(len(data) * percentage))
    index = 0
    while index < len(sample) - 1:
        element = sample[index]
        sharedKey = list(element)[random.randint(0, len(element) - 2)]
        element[sharedKey] = sample[index + 1][sharedKey]
        index += 2

#percentage = x% are not unique profiles
def sameProfiles(data, percentage):
    sample = random.sample(data, math.floor(len(data) * percentage))

    index = 0
    while index < len(sample):
        element = sample[index]
        for key in element:
            element[key] = sample[index - 1][key]
        index += 2