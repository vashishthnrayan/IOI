def letterCombination(digits):
    if not digits:
        return[]

    keypad= {
        "2": "abc",
        "3":"def"
        ,"4":"ghi"
        ,"5":"jkl"
        ,"6":"mno"
        ,"7":"pqrs"
        ,"8":"tuv"
        ,"9":"wxyz"

    }
    result = []

    def bactrack(index,current ):
        if index == len (digits):
            result.append(current)
            return
        letters =  keypad[digits[index]]
        for letter in letters:
            bactrack(index+1,current  + letter)

    bactrack(0, "")
    return result


digits = input("Enter digit for 2 to 9 ")
print(letterCombination(digits))