
def calcProbPos(bPlus,bMinus,cPlus,cMinus):
    probPos = ((bPlus/cPlus)*(cPlus/(cPlus+cMinus)))/((bPlus+bMinus)/(cPlus+cMinus))
    return probPos
    
def calcMean(t,i):
        m = t/i
        return m

print('Enter a statement without punctuation:')
userStatement = input().lower()
print('THINKING...')
userStatement = userStatement.strip('\n').split(' ')
cPlus = 0
cMinus = 0
meanTotal = 0

with open('sampleCorpora.txt') as corpora:
    for line in corpora.readlines():
        lineArray = line.strip('\n').split(',')
        jment = str(lineArray[1])
        if jment == "pos":
            cPlus += 1
        else:
            if jment == "neg":
                cMinus += 1
                

lengthInput = len(userStatement)
for n in range(0,lengthInput):
    bPlus = 0
    bMinus = 0
    checkString = str(userStatement[n])
    #print(checkString)
    with open('sampleCorpora.txt') as corpora:
        for line in corpora.readlines():
            corporaLine = line.strip('\n').split(',')
            checkAgainst = str(corporaLine[0])
            if checkString in checkAgainst:
                posNegCheck = str(corporaLine[1])
                if posNegCheck == "pos":
                    bPlus += 1
                else:
                    if posNegCheck == "neg":
                        bMinus += 1
    
    probPos = calcProbPos(bPlus,bMinus,cPlus,cMinus)
    meanTotal = meanTotal + probPos

print('RESULT: ')

mean = calcMean(meanTotal,lengthInput)
print(str(mean))
if mean > 0.5:
    print('positive')
else:
    if mean < 0.5:
        print('negative')
    else:
        if mean == 0.5:
            print('neutral')
