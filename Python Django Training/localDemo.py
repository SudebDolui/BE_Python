def hello(a):
    """
    This is an example of local module
    """
    print(a)

def even(b):
    """
    This function check for even or not
    """
    print("It is Even") if b%2 == 0 else print("It is odd")

def genNumber(n):
    """
    This function generates number upto a given number
    """
    for i in range(n+1):
        print(i, end=' ')

def genNumDivBy5(n):
    """
    This function generates numbers divisible by 5 upto a given number
    """
    for i in range(n+1):
        if i%5==0: 
            print(i, end=' ')

def genNumDivBy12(n):
    """
    This function generates numbers divisible by 12 upto a given number
    """
    for i in range(n+1):
        if i%12==0: 
            print(i, end=' ')