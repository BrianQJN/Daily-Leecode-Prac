test = {'a': 1, 'b': 2, 'c': 3}
print(list(test.values()))
test2 = {'a': 1, 'b': 2, 'c': 3}
print(list(test2.values()))
print(list(test.values()) == list(test2.values()))
print(test.keys() == test2.keys())