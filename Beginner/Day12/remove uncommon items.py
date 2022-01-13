from collections import Counter

list_1 = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
counted_list = Counter(list_1)
all_values = counted_list.values()
max_value = max(all_values)

for item in all_values:
    print(list_1)
    print(item)
    list(filter(lambda a: a < max_value, list_1))
    print(list_1)


print(list_1)


