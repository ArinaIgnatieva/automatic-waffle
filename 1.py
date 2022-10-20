result = []

def first():
    massive1 = []
    size = int(input("Введите размерность первого массива:"))
    for i in range (size):
        el = float(input("Введите элемент первого массива:"))
        massive1.append(el) 
    return massive1
massive1 = first()
print(massive1)

def second():
    massive2 = []
    size = int(input("Введите размерность второго массива:"))
    for i in range (size):
        el = float(input("Введите элемент второго массива:"))
        massive2.append(el) 
    return massive2
massive2 = second()
print(massive2)

for i in massive1:
    if i in massive2 and i not in result:
        result.append(i)  

print("Общие элементы первого и второго массивов:", result) 