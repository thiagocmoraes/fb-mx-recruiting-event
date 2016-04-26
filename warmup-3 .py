#/usr/local/bin python3

# Implement an algorithm to determine if a string has all unique characters.
# What if you can not use additional data structures?

def is_all_chars_unique_by_sorting(input_str):
    chars = sorted(input_str)
    for index in range(1, len(chars)):
        if chars[index] == chars[index - 1]:
            return False
    return True

non_unique_str = 'are all characters in this string unique?'
all_unique_str = 'it works!'

print(is_all_chars_unique_by_sorting(non_unique_str))
print(is_all_chars_unique_by_sorting(all_unique_str))