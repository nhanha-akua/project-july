numbers = [1,56,234,87,4,76,24,69,90,135]

is_even = filter((lambda x: x % 2 == 0), numbers)

print(list(is_even))