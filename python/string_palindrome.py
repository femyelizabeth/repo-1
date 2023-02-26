#module function
def isPalindrome(str):
    if (str()==str[::-1]):
        return True
    else:
        return False
str=input("enter the string:")
str.tolower()
if isPalindrome(str):
    print(str,"is a plaindrome")
else:
    print(str,"not a palindrome")
