import sys

digit_string = sys.argv[1]
num = int(digit_string)

for i in range(num):
    print(' '*(num-i-1) + '#'*(i+1))
    
