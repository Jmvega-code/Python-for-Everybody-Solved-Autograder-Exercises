#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

lar = None
sma = None

while True:
    num = input('Dame numerito:')
    if num == 'done':
         break
    try:
        num = int(num)
    except:
        print ('Invalid input')
        continue
    if lar is None:
        lar = num
    elif num > lar:
        lar = num
    elif sma is None:
        sma = num
    elif num < sma:
        sma = num
    
print('Maximum is', lar)
print('Minimum is', sma)