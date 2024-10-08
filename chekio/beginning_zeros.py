def beginning_zeros(a: str) -> int:
    
    i = 0
    a = str(a)
    
    while i < len(a) and a[i] == '0':
        i+=1
    
    return i


print("Example:")
print(beginning_zeros("10"))

# These "asserts" are used for self-checking
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
