#Напишите функцию которая будет принимать номер кредитной карты и показывать только последние
# 4 цифры. Остальные цифры должны заменяться звездочками
def karta(a):
    return '*' * len(a[:-4]) + a[-4:]
print(karta('123456789'))

