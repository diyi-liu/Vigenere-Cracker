# base on the list given, create a library that indicates the percentage of
# each letter showing up in the list. If the list is None, return the average
# letter percentile
def buildDict(mylist):
    if mylist == None:
        f
    else 
    return percentDict

# 
def similar(dict1, dict2):

# Remove all chaarters in file that are not letters, and convert all letters
# to uppercase. Return a list of uppercase letters.
def cleanCypherText(file):
    return []

# find the distance between each occurance of all character sequences that
# are at least 3 letters long.
def findAllDistance(charList):
    return []

def main():
    # Ask for input file name from the user
    cypherTextName = input("Please input the name of the cypher text "
                           + "filename: ")
    cypherText = open(cypherTextName, "r")
    cleanedCypherText = cleanCypherText(cypherText)
    distances = findAllDistance(cleanedCypherText)
    for i in range(1, len(cleanedCypherText)/4, 1):
        for j in range(len(distances)):
            if distances[j] % i == 0:
                keylen = i
            else:
                break
    letterChance = buildDict(None)
    # A list of lists that containes the cypher text encoded by the
    # same letter key
    text1 = []
    for i in range(keylen):
        for j in range(0, len(cleanedCypherText), keylen):
            text1[i].append(cleanedCypherText[j])
    # A list of dictionaries that contains the percentage of each letter
    # in the input list. 
    dictionarys = []
    for i in range(keylen):
        dictionarys[i] = buildDict(text1[i])
    # Check how many digits each part shifted from the average percentage
    # dictionary.
    for i in range(keylen):
        if similar(dictionary[i], letterChance):
