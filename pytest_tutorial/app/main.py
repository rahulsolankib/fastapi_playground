import math

def divide_two_number(number_one: int, number_two: int):
    return math.floor(number_one / number_two)


if __name__ == "__main__":
    print(divide_two_number(10, 2))