#/usr/local/bin python3

# Implement an algorithm to determine if a string has all unique characters.
# What if you can not use additional data structures?

def is_all_chars_unique_no_data_structures(input_str):
    for i in range(len(input_str)):
        char_to_verify = input_str[i]
        for j in range(len(input_str)):
            if char_to_verify == input_str[j] and j != i:
                return False
    return True

non_unique_str = 'are all characters in this string unique?'
all_unique_str = 'it works!'

print(is_all_chars_unique_no_data_structures(non_unique_str))
print(is_all_chars_unique_no_data_structures(all_unique_str))