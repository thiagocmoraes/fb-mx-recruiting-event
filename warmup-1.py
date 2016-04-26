#/usr/local/bin python3

# Implement an algorithm to determine if a string has all unique characters. 

def is_all_chars_unique(input_str):
    char_set = set()
    for char in input_str:
        if char in char_set:
            return False
        char_set.update(char)
    return True

non_unique_str = 'are all characters in this string unique?'
all_unique_str = 'it works!'

print(is_all_chars_unique(non_unique_str))
print(is_all_chars_unique(all_unique_str))