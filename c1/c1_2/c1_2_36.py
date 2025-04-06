#import pandas as pd

s = 'My name is Mike. Hi Mike.'

is_start = s.startswith('My')
print(is_start)

is_start = s.startswith('x')
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
# 
print(s.capitalize())