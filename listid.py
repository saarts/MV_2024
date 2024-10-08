
list_example = ['banana','tomato','potato','pot']
list_example_2 = ['ananas', 'cream']

print(list_example)
print(list_example[0])
print(len(list_example))
print(list_example[3])
print(list_example[len(list_example) - 1])
list_example.append('cola')
print(list_example)
list_example.pop(0)
print(list_example)
print(list_example + list_example_2)
string_example = ", ".join(list_example)
print(string_example)

list_numbers = [2, 3, 6, 9, 10]
print(sum(list_numbers))
print(max(list_numbers))
print(min(list_numbers))

