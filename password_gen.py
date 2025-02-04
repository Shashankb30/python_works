import random
import string

def genPass(minLen,number=True,spChar=True):
    digit=string.digits
    letters=string.ascii_letters
    special=string.punctuation
    
    # print(digit,special,letters)
    charecter=letters
    if number:
        charecter+=digit
    if spChar:
        charecter+=special
        
    password=''
    meetsCriteria=False
    hasNum=False
    hasSpecial=False
    
    while not meetsCriteria or len(password)<minLen:
        newChar=random.choice(charecter)
        password+=newChar
        
        if newChar in digit:
            hasNum=True
        elif newChar in special:
            hasSpecial=True
        
        meetsCriteria=True
        if number:
            meetsCriteria=hasNum
        if spChar:
            meetsCriteria= meetsCriteria and hasSpecial
    return password

minLen=int(input("Enter Minimun Length of Password: "))
hasNum=input("Do you want the password to contain digits(y/n) ").lower()=="y"
hasSpecial=input("Do you want special character(y/n)? ").lower()=="y"

password=genPass(minLen,hasNum,hasSpecial)

print(password)

