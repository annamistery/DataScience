import math

# Тест для math.pi
assert math.pi==3.141592653589793, "math.pi не соответствует ожидаемой величине."

# Тест для math.sqrt (квадратный корень)
assert math.sqrt(9) == 3, "Квадратный корень из 9 равен 3"

# Тест для math.pow (возведение в степень)
assert math.pow(2, 2) == 4, "2 во степени 2 равно 4."
assert math.pow(3, 3) == 27, "3 в степени 3 равно 27"

assert math.sqrt(4) == 2, "квадратный корень из 4 равен 2"



# Тест для math.hypot (гипотенуза)

assert math.hypot(3, 4) == 5.0, "Гипотенуза треугольника со сторонами 3 и 4 равна 5"

# Пример и проверка для функции filter
nums = [-2, -1, 0, 1, 2, 5 ,8,-9]
# Фильтруем, оставляем только отрицательные числа числа
positive_nums = list(filter(lambda x: x < 0, nums))
assert positive_nums == [-2,-1, -9], "filter не отфильтровал отрицательные числа правильно."

# Пример и проверка для функции map
# Возводим числа в квадрат
squared_nums = list(map(lambda x: x**2, nums))
assert squared_nums == [4, 1, 0, 1, 4, 25, 64, 81], "map не преобразовал числа в их квадраты правильно."

# Пример и проверка для функции sorted
mixed_nums = [3, 1, 4, 1, 5, 9, 2]
# Сортируем числа
sorted_nums = sorted(mixed_nums)
assert sorted_nums == [1, 1, 2, 3, 4, 5, 9], "sorted не отсортировал числа правильно."

print("All tests passed.")



