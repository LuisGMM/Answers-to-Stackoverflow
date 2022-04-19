


dict1 = {'key1a': [i for i in range(5)], 'key1b': [i for i in range(6)]}
dict2 = {'key2a': [i for i in range(5)], 'key2b': [i for i in range(6)]}


def elements_in_common(list1: list, list2: list) -> float:

    biggest_list = list1 if len(list1) >= len(list2) else list2
    smallest_list = list1 if biggest_list is list1 else list2
    
    elements_in_common = [element for element in biggest_list if element in smallest_list]

    return elements_in_common


table = {}

for dict1_key, dict1_val in dict1.items():
    table[dict1_key] = {}


