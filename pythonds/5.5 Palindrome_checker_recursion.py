"""
recursion:
Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise.

kayak
aibohphobia
Live not on evil
Reviled did I live, said I, as evil I did deliver
Go hang a salami; I’m a lasagna hog.
Able was I ere I saw Elba
Kanakanak – a town in Alaska
Wassamassaw – a town in South Dakota

"""

def isPal(asentence):
    # remove space and punctuation in string
    s = "".join(e for e in asentence if e.isalnum())
    # base case:
    if len(s) <= 1:
        return True
    else:
        return isPal(s[1:-1]) and s[0] == s[-1]

if __name__ == '__main__':   
    print(isPal("x") == True)
    print(isPal("radar") == True)
    print(isPal("hello") == False)
    print(isPal("") == True)
    print(isPal("hannah") == True)
    print(isPal("madam i'm adam") == True)
