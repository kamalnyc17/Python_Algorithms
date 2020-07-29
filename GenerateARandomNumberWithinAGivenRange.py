import random


def generate_random_num(num1, num2):
    return random.randint(num1, num2)


print(f"Current Random Number: {generate_random_num(1, 20)}")
