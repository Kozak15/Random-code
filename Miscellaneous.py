
#100 bottles of beer on the wall
for i in range(100,-1,-1):
    if i == 0:
        print("Damn, we're out of beer!")
        print('Remember kids, alcohol is bad')
    else:
        print(f"{n} bottles of beer on the wall.")
        print(f"{n} bottles of beer.")
        print("Take one down, pass it around,")
        print(f"{n-1} bottles of beer on the wall\n")
#Even or odd
def even_or_odd(n):
    return 'EOvdedn'[n%2::2]
#Palindrome
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

#Assume that nand and nor are defined
def nand(a, b):
    return not (a and b)
def nor(a, b):
    return not (a or b)
#Not,and,or using nand
def not1(x):
    return nand(x, x)
def and1(x, y):
    return nand(nand(x,y),nand(x,y))
def or1(x, y):
    return nand(nand(x,x),nand(y,y))
#Not,and,or using nor
def not2(x):
    return nor(x, x)
def and2(x, y):
    return nor(nor(x,x),nor(y,y))
def or2(x, y):
    return nor(nor(x,y),nor(x,y))
