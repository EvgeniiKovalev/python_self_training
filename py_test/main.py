"""
 Реализовать метод, принимающий в качестве аргумента одномерный целочисленный массив, и возвращающий
 новый массив, который содержит элементы исходного массива, идущие после последней единицы.
 Если входной массив не содержит единиц, то должно быть брошено RuntimeException.
 Примеры:
 Входной массив: [ 1 2 1 2 2 ] => Результат: [ 2 2 ]
 Входной массив: [ 2 2 2 2 ] => RuntimeException
 Реализовать метод, проверяющий входной массив, что он состоит только из чисел 1 и 2. Если в массиве
 присутствуют числа кроме 1 и 2, или нет хотя бы одной единицы или двойки,
 то результат должен быть равен false
 Примеры:
 [ 1 2 ] => true
 [ 1 1 ] => false
 [ 1 3 ] => false
 [ 1 2 2 1 ] => true
 Реализовать набор тестов для методов.
"""

def method_one(src : list) -> list:
    indexLastOne = -1
    for i in range(len(src) - 1, -1, -1):
        if src[i] == 1:
            indexLastOne = i
            break

    if indexLastOne == -1:
        raise ValueError('Не содержит единиц')

    result = []
    j = 0
    for i in range(indexLastOne + 1, len(src), 1):
        print(i, src[i])
        result.append(src[i])
        j += 1
    return result

def method_two(src : list) -> bool:
    present_one = False
    present_two = False

    for item in src:
        if item == 1:
            present_one = True
            continue
        if item == 2:
            present_two = True
            continue
        return False

    return  present_one and present_two


if __name__ == "__main__":
    print(method_one([1, 2, 1, 2, 2]))
    print(method_one([2, 2, 2, 2]))
    print(method_two([2, 2, 2, 2]))
    print(method_two([1, 2, 3]))
    print(method_two([1, 2, 1]))




