from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    
    bool_val = True
    
    for i in range(len(elements) - 1):
        if elements[i] != elements[i + 1]:
            bool_val = False
        
    return bool_val


print("Example:")
print(all_the_same([1, 1, 1]))

# These "asserts" are used for self-checking
assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, "a", 1]) == False
assert all_the_same([1, 1, 1, 2]) == False
assert all_the_same([]) == True
assert all_the_same([1]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
