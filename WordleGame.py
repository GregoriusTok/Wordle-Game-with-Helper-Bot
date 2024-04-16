import random

ValidWordsFile = open("ValidWords.txt", "r")
ValidWords = ValidWordsFile.read().upper()
WordList = ValidWords.split("\n")
ValidWordsFile.close()
from random import randrange

answer = WordList[randrange(0, len(WordList))].upper()

correctionsHistory = []

TotalTurns = 6
for turn in range(TotalTurns):
    trial = input("Guess: ").upper()
    
    corrections = []
    for i in trial:
        n = trial.index(i)
        
        if i == answer[n]:
            corrections.append("🟩")
        elif i not in answer:
            corrections.append("⬛️")
        elif i in answer:
            corrections.append("🟨")
    
    print(trial)
    
    correctionsHistory.append(corrections)
    for i in correctionsHistory:
        print(i)
    
    if trial == answer:
        print("YOU WON in", turn + 1, "MOVES")
        break
    