def too_old(x): return x < 30

ages = [22, 25, 29, 34, 56, 24, 12]

list(filter(too_old, ages))


def young_person(x): return x > 30

ages = [22, 25, 29, 34, 56, 24, 12]

filter(young_person, ages)
print(list(too_old(45)))
print(list(young_person(23)))