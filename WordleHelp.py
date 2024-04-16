import random 

ValidWordsFile = open("ValidWords.txt", "r")
ValidWords = ValidWordsFile.read().upper()
WordList = ValidWords.split("\n")
ValidWordsFile.close()

def ScoreWordsFunc():
    ScoredLetters = {
        "E" : 56.88,
        "A" : 43.31,
        "R" : 38.64,
        "I" : 38.45,
        "O" : 36.51,
        "T" : 34.43,
        "N" : 33.92,
        "S" :  29.23,
        "L" : 27.98,
        "C" : 23.13,
        "U" : 18.51,
        "D" : 17.25,
        "P" : 16.14,
        "M" : 15.36,
        "H" : 15.31,
        "G" : 12.59,
        "B" : 10.56,
        "F" : 9.24,
        "Y" : 9.06,
        "W" : 6.57,
        "K" : 5.61, 
        "V" : 5.13,
        "X" : 1.47,
        "Z" : 1.39,
        "J" : 1,
        "Q" : 0}
    #Scoring Words
    ScoredWords = {}
    for i in WordList:
        ScoredWords[i] = 0

        #Letters
        for a in i:
            ScoredWords[i] += ScoredLetters[a]

        for a in range(len(i) - 1):
            #Double Letters
            if i[a] == i[a + 1]:
                ScoredWords[i] = ScoredWords[i] * 0.5
        
            #2 of same letter
            if i.count(i[a]) > 1:
                ScoredWords[i] = ScoredWords[i] * 0.75
        
        #Ends in S or D
        if i[-1] == "S" or i[-1] == "D" and i[-2] == "E": 
            ScoredWords[i] = ScoredWords[i] * 0.1


        #Has vowels
        vowelList = ["A", "E", "I", "O", "U"]
        for a in vowelList:
            if a not in i:
                ScoredWords[i] = ScoredWords[i] * 1.4
    
    SortedScoredWords = {}
    sorting = sorted(ScoredWords, key=ScoredWords.get, reverse = True)
    for w in sorting:
        SortedScoredWords[w] = ScoredWords[w]
    return SortedScoredWords

ScoredWords = ScoreWordsFunc()

def write_dict_to_file(thing, file):
    with open(file, "w") as f:
        for key, value in thing.items():
            f.write("%s : %s\n" % (key,value))
write_dict_to_file(ScoredWords, "ScoredWords.txt")


CorrectionsList = {}

turn = 1

Done = False

ScoredWordsCopy = ScoredWords.copy()
maxValue = max(ScoredWordsCopy.values())
fiveScoreList = [key for key in ScoredWordsCopy if ScoredWordsCopy[key] == maxValue]
recommend = fiveScoreList[random.randrange(0, len(fiveScoreList))]
print(fiveScoreList)
print(recommend, ScoredWords[recommend])

while not Done:
    word = ""
    CorrectionsList = {}
    while len(word) != 5:
        word = input("Trial Word: ").upper()
    corrections = ""
    print("Green = G, Yellow = Y, Black = B")
    while len(corrections) != 5:
        corrections = input("Results: ").upper()
    
    if corrections == "GGGGG":
        Done = True
        print(turn)
        print("YOU WON!!!")
        break

    for i in word:
        if i not in CorrectionsList:
            CorrectionsList[i] = corrections[word.index(i)]

    #WordList = [a for a in WordList if a[0] == "T"]
    for i in CorrectionsList:
        if CorrectionsList[i] == "B":
            WordList = [a for a in WordList if i not in a]
        elif CorrectionsList[i] == "G":
            WordList = [a for a in WordList if a[word.index(i)] == i]
        elif CorrectionsList[i] == "Y":
            WordList = [a for a in WordList if i in a and  a[word.index(i)] != i]


    
    if ScoredWords != {}:
        while recommend not in WordList:
            del ScoredWords[recommend]
            ScoredWordsCopy = ScoredWords.copy()
            maxValue = max(ScoredWordsCopy.values())
            fiveScoreList = [key for key in ScoredWordsCopy if ScoredWordsCopy[key] == maxValue]
            recommend = fiveScoreList[random.randrange(0, len(fiveScoreList))]
        print(recommend, ScoredWords[recommend])
    if ScoredWords == {} or len(WordList) <= 10:
        print(WordList)


    print(len(WordList), "Words Left")
    turn += 1
    # print(CorrectionsList)
