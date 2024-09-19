def end_zeros(a: int) -> int:
    
    i = 1
    a = str(a)
    
    while (i <= len(a)) and (a[-i] == '0'):
        i += 1
              
    
    return i-1


print("Example:")
print(end_zeros(10))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
