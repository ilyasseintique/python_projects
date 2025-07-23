import re
import secrets
import string
def gen_passeword(length=10, letters=4, nums=3, chars=3):
    all_chars=string.ascii_letters+string.digits+string.punctuation
    if letters + nums + chars > length:
        raise ValueError("the length must be bigger than the the some of other arguments ")
    while True:
        pwd=''
        for _ in range(length):
            pwd+=secrets.choice(all_chars)
        constraints=[(nums,r'\d'),
                     (letters,r'\w'),
                     (chars,r'\W')
                    ]
        checked=all(constraint <= len(re.findall(pattern,pwd)) for constraint , pattern in constraints)
        if checked:
            break
    return pwd
numOfPass=1
while True:
    print("welcom to our classique programme for generating strong passwords for free\nmenu : \n for precising how many pwds you want print P \n for continue and generating single pwd print C \n for exiting print E \n")
    ans=input()
    if ans=='E':
        print("bis später !!")
        break
    if ans=='P':
        numOfPass=int(input("give how many pwds you want :"))
    for _ in range(numOfPass):
        length=int(input("give the length of your password :"))
        letters=int(input("give the number of the letter that you want in you password : "))
        chars=int(input("give the number of the characters that you want in you password : "))
        nums=int(input("give the number of the numbers that you want in you password : "))
        print(gen_passeword(length,letters,nums,chars))





