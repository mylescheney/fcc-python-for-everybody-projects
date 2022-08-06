def arithmetic_arranger(problems, showAnswers):
    n1Line = ""
    n2Line = ""
    sepLine = ""
    answLine = ""
    arranged_problems = ""

    count = 1;
    for exp in problems :
        exp = exp.strip()
      
        # Separates the first number in the expression
        firstCut = exp.find(" ")
        firstN = exp[0:firstCut]
        
        # Separates the operator
        operator = "+"
        if exp.find("+") != -1 :
            operator = "+"
        if exp.find("-") != -1 :
            operator = "-"
        if exp.find("*") != -1 :
            operator = "*"
        if exp.find("/") != -1 :
            operator = "/"

        # Separates the second number in the expression
        secondCut = exp.find(operator)
        secondN = exp[secondCut + 1:]
        secondN = secondN.strip()

        # Determines the length of the stacked express, adding 2 to account for the operator and at least one space
        length = 1
        if len(firstN) >= len(secondN) :
            length = len(firstN) + 2
        else :
            length = len(secondN) + 2

        answer = ""
        if showAnswers == True :
            answer = eval(firstN + " " + operator + " " + secondN)
            if len(str(answer)) > length :
                length = len(str(answer))
        
        # Adding white space to the numbers that need it
        n1Blanks = length - len(firstN)
        n1Spaces = "  "
        while len(n1Spaces) < n1Blanks + 2 :
            n1Spaces = n1Spaces + " "
        if count != 1 :
            firstN = n1Spaces + "    " + firstN 
        else :
            firstN = n1Spaces + firstN 
        n1Line = n1Line + firstN

        n2Blanks = length - len(secondN)
        n2Spaces = ""
        while len(n2Spaces) < n2Blanks :
            n2Spaces = n2Spaces + " "
        if count != 1 :
            secondN = "    " + operator + " " + n2Spaces + secondN
        else :
            secondN = operator + " " + n2Spaces + secondN
        n2Line = n2Line + secondN

        # Creates the separating line
        dashes = ""
        for i in firstN :
            dashes = dashes + "-"
        if count != 1 :
            dashes = "    " + dashes
            dashes = dashes[:len(dashes) - 4]
        sepLine = sepLine + dashes

        # Creates the answer line
        answBlanks = length - len(str(answer))
        answSpaces = "  "
        answStr = str(answer)
        while len(answSpaces) < answBlanks + 2 :
            answSpaces = answSpaces + " "
        if count != 1 :
            answStr = answSpaces + "    " + str(answer) 
        else :
            answStr = answSpaces + str(answer) 
        answLine = answLine + answStr
            
        count = count + 1

    if showAnswers == True :
        arranged_problems = n1Line + "\n" + n2Line + "\n" + sepLine + "\n" + answLine
    else :
        arranged_problems = n1Line + "\n" + n2Line + "\n" + sepLine
    return arranged_problems