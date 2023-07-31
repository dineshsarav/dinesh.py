## positive numbers

def positivenumbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    for num in positive_numbers:
        print(num)

input_str = input("Enter a list of numbers separated by commas: ")
input_list = [int(num) for num in input_str.split(",")]

print("Positive numbers in the list:")
positivenumbers(input_list)
