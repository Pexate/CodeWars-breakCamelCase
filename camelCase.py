camelCaseWord = input("Input a word in Camel Case: ")


def solution(s):
    sList = list(s)
    string = ""
    for i in range(len(sList)):
        if sList[i].isupper() == True:
            sList[i-1] += " "
    for i in range(len(sList)):
        string += sList[i]
    '''string.lower()
    string[0].capitalize() '''
    return string


print(solution(camelCaseWord).lower().capitalize())
