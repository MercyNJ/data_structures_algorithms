def is_palindrome(s):
    # Remove spaces and punctuation and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the string equals its reverse
    return s == s[::-1]

# Test the function
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("level"))  # Output: True
print(is_palindrome("A man, a plan, a canal, Panama!"))  # Output: True
print(is_palindrome("hello"))  # Output: False
