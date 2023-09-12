def sum_of_numbers(numbers):
 total = 0
 for number in numbers:
  total += number
 return total


def product_of_numbers(numbers):
 product = 1
 for number in numbers:
  product *= number
 return product


def reverse_numbers(numbers):
 return numbers[::-1]


def main():
 input_str = input("Enter a list of numbers separated by a single space: ")
 input_numbers = [int(x) for x in input_str.split()]


 sum_result = sum_of_numbers(input_numbers)
 product_result = product_of_numbers(input_numbers)
 numbers_reversed = reverse_numbers(input_numbers)


 print("Sum of given  numbers:  ", sum_result)
 print("Product of given numbers:  ", product_result)
 print("Numbers given in reverse order:   ", numbers_reversed)


if __name__ == "__main__":
 main()