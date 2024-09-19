def most_frequent(data: list[str]) -> str:
    
    most_freq = ''
    max_num = 0
    
    for elt in data:
        num = 0
        for elt2 in data:
            
            if elt2 == elt:
                num += 1
        if max_num < num:
            most_freq = elt
            max_num = num
                   
        
    return most_freq


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
