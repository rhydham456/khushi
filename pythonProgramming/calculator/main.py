# %%
# agenda of our calculator 
# taking user input 
# first brackets will be taken care 
# then rest of calculation

# %%
calculation = str(input("enter your calculation"))

# %%
bracketIndex = []
for index in range(0,len(calculation)):
    if calculation[index]=='(':
        bracketIndex.append(index)
    if calculation[index]==')':
        bracketIndex.append(index)

bracketSignIndex = []
bracketCalculation = calculation[bracketIndex[0]+1:bracketIndex[1]]
print(bracketCalculation)
for index in range(0,len(bracketCalculation)):
    if bracketCalculation[index]=='+' or bracketCalculation[index]=='-' or bracketCalculation[index]=='/' or bracketCalculation[index]=='*':
       bracketSignIndex.append(index)
# print(bracketCalculation[bracketSignIndex[0]:])
bracketCalculationNumber = [int(bracketCalculation[:bracketSignIndex[0]]),int(bracketCalculation[bracketSignIndex[0]+1:])]
print(bracketCalculationNumber)
if bracketCalculation[bracketSignIndex[0]]=='+':
    result = bracketCalculationNumber[0]+bracketCalculationNumber[1]
    print(f'result is {result}')
if bracketCalculation[bracketSignIndex[0]]=='-':
    result = bracketCalculationNumber[0]-bracketCalculationNumber[1]
    print(f'result is {result}')
if bracketCalculation[bracketSignIndex[0]]=='/':
    result = float(bracketCalculationNumber[0]/bracketCalculationNumber[1])
    print(f'result is {result}')
if bracketCalculation[bracketSignIndex[0]]=='*':
    result = bracketCalculationNumber[0]*bracketCalculationNumber[1]
    print(f'result is {result}')

newCalculation = calculation.replace('('+bracketCalculation+")",str(result))
print(newCalculation)

# %%
signIndex = [0,len(newCalculation)]
numberList = []
mainCalculation:int = 0
for index in range(0,len(newCalculation)):
    if newCalculation[index]=='+' or  newCalculation[index]=='-' or  newCalculation[index]=='*' or  newCalculation[index]=='/' :
        signIndex.append(index)
signIndex.sort()
print(signIndex)

for index in range(1,len(signIndex)):
    numberList.append(newCalculation[signIndex[index-1]:signIndex[index]])
for item in numberList:
    mainCalculation+=int(item)
print(mainCalculation)


