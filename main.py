import string
import random

if __name__ == '__main__':
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    passlength = input("Enter password length\n")
    flag = passlength.isdigit()
    if flag == True:
        passlength = int(passlength)
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        random.shuffle(s)
        print("Your Password is: ")
        print("".join(random.sample(s,passlength)))
    else:
        print("Enter a digit")