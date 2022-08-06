from arithmetic_arranger import arithmetic_arranger

userInput = input('Enter an expression, or multiple separated by commas >')
expStrs = userInput.split(',')
expCleaned = []

for str in expStrs :
    cleanExp = str.strip()
    expCleaned.append(cleanExp)

print(arithmetic_arranger(expCleaned, True))
