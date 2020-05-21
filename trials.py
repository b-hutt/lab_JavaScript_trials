"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    
    for item in items:
        print(item)

output_all_items([1, 'hello', True])


def get_all_evens(nums):
    
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

print(get_all_evens([7, 8, 10, 1, 2, 2]))


def get_odd_indices(items):
    result = []

    for idx, item in enumerate(items):
        if idx % 2 != 0:
            result.append(item)

    return result

print(get_odd_indices([1, 'hello', True, 500]))


def print_as_numbered_list(items):
    
    i = 1

    for item in items:
        print(f'{i}. {item}')
        i += 1

print_as_numbered_list([1, 'hello', True])

def get_range(start, stop):
    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums

print(get_range(0, 5))


def censor_vowels(word):
    
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)

    return " ".join(chars)

print(censor_vowels('hello world'))


def snake_to_camel(string):
   
    camelCase = []

    for word in string.split('_'):
        print (word)
        camelCase.extend([word.title()])

    return "".join(camelCase)

print(snake_to_camel('hello_world'))


def longest_word_length(words):

    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest
    
print(longest_word_length(['jelly', 'fish', 'jellyfish', 'zebra']))

def truncate(string):

    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return ''.join(result)

print(truncate('aaaabbbbcccca'))


def has_balanced_parens(string):
    parens = 0

    for char in string: 
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

        if parens > 0:
            return False

    return parens < 0

print(has_balanced_parens('((This) (is) (good))'))

def compress(string):
    compressed = []

    current_char = ''
    char_count = 0

    for char in string:
        if char != current_char:
            compressed.append(current_char)

            if char_count > 1: 
                compressed.append(str(char_count))

        current_char = char
        char_count = 0

    char_count += 1

    compressed.append(current_char)

    if char_count>1:
        compressed.append(str(char_count))

    return ''.join(compressed)

print(compress('aabbaabb'))







