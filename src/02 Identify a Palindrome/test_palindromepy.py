
import re

def is_palindrome(my_string):
  forward = ''.join(re.findall(r'[a-z]+',my_string.lower()))
  reversed = forward[::-1]
  if forward == reversed:
    print(f"'{my_string}' - Is a Palindrome.")
  else:
    print(f"'{my_string}' - Is NOT a Palindrome.")

if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
    print(is_palindrome("R A C E C A R")) 