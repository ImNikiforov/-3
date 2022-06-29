# Напишите функцию, которая проверяет: является ли слово палиндромом
def pol(str):
    if len(str) <= 1:
        return True
    elif str[0] != str[-1]:
        return False
    return pol(str[1:-1])
print(pol('шалаш'))