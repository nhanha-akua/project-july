def convert(lst):
    return ([i for item in lst for i in item.split()])
lst = ['just say you wont miss me']
print( convert(lst))