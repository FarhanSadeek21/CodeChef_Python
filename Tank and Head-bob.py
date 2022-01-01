testCase = int(input())
for i in range(testCase):
    wordLength = int(input())
    word = input()
    if('Y' in word):
        print('NOT INDIAN')
    elif('I' in word):
        print('INDIAN')
    else:
        print('NOT SURE')
