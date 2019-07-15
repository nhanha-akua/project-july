from functools import reduce
def join_strings(words):
    secret = ""
    for word in words:
        secret += word + " "
    return secret
words = ["how", "far", "is", "too", "far"]
total = reduce(lambda item, running_total: item + " " + running_total, words)
print(total)
howfaristoofar = join_strings(words)
print(join_strings(words))
