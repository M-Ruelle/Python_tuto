from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    
    length = len(text)
    list_ = []
    
    if length%2 == 0:
        for i in range(length//2):
            list_.append(text[2*i:2*(i+1)])
        
    else:
        length = len(text) - 1
        text_bis = text[:-1]
        
        for i in range(length//2):
            list_.append(text_bis[2*i:2*(i+1)])
            
        list_.append(text[-1] + '_')
        
    return list_


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
