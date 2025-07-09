def cube_numbers(numbers):
    return [x ** 3 for x in numbers]

numbers = list(map(int, input("Введіть числа через пробіл: ").split()))
cubes = cube_numbers(numbers)
print(cubes)
