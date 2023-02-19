import sys

digit_string = sys.argv[1]
digit = int(digit_string)
s = 0
while digit != 0:
    s += digit%10
    digit = digit//10
    
print(s)

