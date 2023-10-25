
# def convert_to_celsius(temp_f: float = 75) -> float:
#     return (temp_f - 32) * 5 / 9

# print(f"Room temperature: {round(convert_to_celsius(), 1)} C ")

def print_letter(letter: str, *paparam, **testas) -> str:
    print(letter)
    if paparam:
        print(f"Args: {paparam}")
        print(type(paparam))
    if testas:
        print(f"Kwargs: {testas}")
        print(type(testas))
    return letter

print_letter("A", 25, "32", name = "Antanas")

# def add_two_numbers(no_a: int, no_b: int) -> int:
#     return no_a + no_b
# print(f"Sum of numbers: {add_two_numbers(5)}")

# def multiply_two_numbers(no_a: int, no_b: int) -> int:
#      return no_a * no_b
# print(f"Multi of numbers: {multiply_two_numbers(5, 5)}")

# multiplication = lambda a, b: a * b
# print(multiplication(5, 5))

# add_default_quantity = lambda amount: amount + 25
# print(add_default_quantity(444))
