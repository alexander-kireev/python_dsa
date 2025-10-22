def first_non_repeating_char(word):

    chars = {}

    for char in word:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for char in word:
        if chars[char] == 1:
            return char

    return None




word = "hello"

print(first_non_repeating_char(word))