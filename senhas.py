import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%¨&*'

for_pass = lower_case + upper_case + numbers + symbols
passaword_size = 12

passaword = "".join(random.sample(for_pass, passaword_size))

print(passaword)