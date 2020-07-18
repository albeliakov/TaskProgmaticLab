import numexpr as ne

def decimal_to_ternary(num):
    newNum = ''
    base = 3
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    newNum = '0'*(9-len(newNum)) + newNum

    return newNum


# ====== цифры            : 9___8___7___6___5___4___3___2___1___0 ======
# ====== индексы операций :  [0] [1] [2] [3] [4] [5] [6] [7] [8]  ======

requiredValue = 200 
#requiredValue = int(input("Enter required value: "))
#print()

operNum2Symb = {'0': '', '1': '+', '2': '-'}

for comb in range(3**9):

    signsComb = decimal_to_ternary(comb)
    signsNum2Symb = [operNum2Symb[sign] for sign in list(signsComb)]

    currExpression = ('9{0[0]}8{0[1]}7{0[2]}6{0[3]}5{0[4]}'
                      '4{0[5]}3{0[6]}2{0[7]}1{0[8]}0'.format(signsNum2Symb))

    if ne.evaluate(currExpression) == requiredValue:
        print("{}={}".format(currExpression, requiredValue))
