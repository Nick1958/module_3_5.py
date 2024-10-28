# Самостоятельная работа по уроку "Рекурсия"
# Задача "Рекурсивное умножение цифр":

def get_multiplied_digits(number):
    str_number = str(number)      # переменная str_number и строковое представление(str) числа number
    first = int(str_number[0])   # переменную first, первый символ из str_number в числовом представлении(int)
    if len(str_number) == 1:
        return first
    return first * get_multiplied_digits(int(str_number[1:]))  # цифру first * на результат работы этой же функции,
                                                                # но уже без первой цифры.
# Стек вызовов: get_multiplied_digits(40203) -> 4*get_multiplied_digits(203) -> 4*2*get_multiplied_digits(3) -> 4*2*3

result1 = get_multiplied_digits(40203)
result2 = get_multiplied_digits(1234)
result3 = get_multiplied_digits(123456)

print(result1)
print(result2)
print(result3)