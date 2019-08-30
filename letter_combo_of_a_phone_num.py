# author: YANG CUI
"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
 below. Note that 1 does not map to any letters.

This program uses backtracking
"""

def digitMapsLetter(digit):
    if digit == "2":
        result = ["a", "b", "c"]
    elif digit == "3":
        result = ["d", "e", "f"]
    elif digit == "4":
        result = ["g", "h", "i"]
    elif digit == "5":
        result = ["j", "k", "l"]
    elif digit == "6":
        result = ["m", "n", "o"]
    elif digit == "7":
        result = ["p", "q", "r", "s"]
    elif digit == "8":
        result = ["t", "u", "v"]
    elif digit == "9":
        result = ["w", "x", "y", "z"]
    return result

def letter_combo_aux(inputString):
    if inputString == "":
        return []
    letterList = []
    resultString = ""
    letter_combo(inputString, resultString, letterList)
    return letterList

def letter_combo(inputString, resultString, letterList):
    # base case
    if inputString == "":
        letterList.append(resultString)
    # choose/explore/unchoose
    else:
        # choose digit
        letter = inputString[0]
        letters = digitMapsLetter(letter)

        for j in range(len(letters)):
            # choose letter
            letterChosen = letters[j]
            resultString = resultString + letters[j]
            letters.__delitem__(j)
            inputString = inputString[1:]

            # explore
            letter_combo(inputString, resultString, letterList)

            # unchoose
            resultString = resultString[:len(resultString) - 1]
            letters.insert(j,letterChosen)
            inputString = letter + inputString
    return

print(letter_combo_aux(""))



