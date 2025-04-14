#arithmetic operators
a=2
b=3
sum=a+b
print(a+b)

sub=a-b
print(a-b)

mul=a*b
print(a*b)

div=a/b
print(a/b)

mod=a%b
print(a%b)

fd=a//b
print(a//b)

#assignment operators
x=41
x+=1
print(x)

x=42
x-=2
print(x)

x=24
x*=4
print(x)

x=54
x/=2
print(x)

x=46
x//=3
print(x)

x=58
x%=4
print(x)

#logical operators
x=10
print(x>6 and x<15)

x=10
print(x>6 or x<15)

x=10
print(not(x>5 and x<15))

#bitwise operators
x=6
y=3
print(x&y)

print(x|y)

print(6^3)

print(~3)

print(x<<2)

print(x>>2)

#The right shift bitwise operator (>>) is used to shift the bits of a number to the right by a specified number of positions.
#syntax:result = number >> positions
#example
## Positive number
a = 16        # binary: 00010000
b = a >> 2    # binary: 00000100 → 4
print(b)      # Output: 4

# Negative number
a = -16       # binary: ...11110000 (in two's complement)
b = a >> 2    # binary: ...11111100 → -4
print(b)      # Output: -4
