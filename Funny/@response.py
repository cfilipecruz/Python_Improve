def character_distribution(input_string):
    char_count = {}

    for char in input_string:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count  # Correctly placed outside the loop

# Example usage:
result = character_distribution("Hello, World!")
print(result)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

import pytest



# Test case 1: General input with mixed case and special characters (Logical case)

def test_general_case():

  assert character_distribution('Hello, World!') == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}



# Test case 2: Empty string (Edge case)

def test_empty_string():

  assert character_distribution('') == {}



# Test case 3: String with no alphabetic characters (Edge case)

def test_no_alphabetic_characters():

  assert character_distribution('12345!@#$%') == {}



# Test case 4: String with all identical alphabetic characters (Edge case)

def test_identical_characters():

  assert character_distribution('aaaaaa') == {'a': 6}



# Test case 5: String with mixed letters and numbers (Logical case)

def test_mixed_letters_numbers():

  assert character_distribution('a1b2c3d4e5f6g7h8i9j0') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}



# Test case 6: String with mixed case letters (Logical case)

def test_mixed_case():

  assert character_distribution('AaBbCcDdEe') == {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2}



# Test case 7: Large input with repetitive pattern (Performance case)

def test_large_input():

  large_input = 'abcde' * 1000

  expected_output = {'a': 1000, 'b': 1000, 'c': 1000, 'd': 1000, 'e': 1000}

  assert character_distribution(large_input) == expected_output

# Test case 8: Single-character string (Edge case)
def test_single_character():
    assert character_distribution('a') == {'a': 1}

# Test case 9: String with only uppercase letters (Edge case)
def test_all_uppercase():
    assert character_distribution('ABCDE') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}

# Test case 10: String with only lowercase letters (Edge case)
def test_all_lowercase():
    assert character_distribution('abcde') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}

# Test case 11: All alphabetic characters A-Z, a-z (Comprehensive test)
def test_all_alphabetic_characters():
    input_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    expected_output = {char.lower(): 2 for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert character_distribution(input_string) == expected_output

# Test case 12: Input with spaces only (Edge case)
def test_spaces_only():
    assert character_distribution('     ') == {}

# Test case 13: Input with special characters only (Edge case)
def test_special_characters_only():
    assert character_distribution('!@#$%^&*()') == {}

# Test case 14: Very large input with random characters (Performance case)
def test_very_large_random_input():
    import random
    import string
    large_input = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=100000))
    alphabetic_characters = [char.lower() for char in large_input if char.isalpha()]
    expected_output = {char: alphabetic_characters.count(char) for char in set(alphabetic_characters)}
    assert character_distribution(large_input) == expected_output

# Test case 15: Repeated single character with mixed case (Logical case)
def test_repeated_single_character():
    assert character_distribution('AaAaAa') == {'a': 6}

# Test case 16: Input with leading and trailing spaces (Edge case)
def test_leading_trailing_spaces():
    assert character_distribution('  a b c  ') == {'a': 1, 'b': 1, 'c': 1}

# Test case 17: Non-English alphabetic characters (Assumption-based edge case)
def test_non_english_alphabetic_characters():
    assert character_distribution('áéíóúüñ') == {'á': 1, 'é': 1, 'í': 1, 'ó': 1, 'ú': 1, 'ü': 1, 'ñ': 1}

# Test case 18: Input with newline and tab characters (Edge case)
def test_newline_and_tabs():
    assert character_distribution('a\nb\tc') == {'a': 1, 'b': 1, 'c': 1}