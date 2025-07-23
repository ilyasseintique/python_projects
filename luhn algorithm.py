code_num = input("give your 16 digits 4 pes 4 separated by - ")
def checking_fct(code_num):
    somme=0
    somme1=0
    total=0
    #we have to transform the input
    for char in code_num:
        if not char.isalnum():
            code_num = code_num.replace(char,"")
    # transformed_serie=code_num.translate(str.maketrans({"-":"", " ":""}))
    reversed_serie=code_num[::-1]
    odd_numbers=reversed_serie[0::2]
    even_numbers=reversed_serie[1::2]
    for digit in even_numbers:
        num= int(digit)*2
        if num >= 10 :
            num= num // 10 + num % 10
        somme+=num
    for digit in odd_numbers :
        somme1+=int(digit)
    tot=somme1+somme
    if tot % 10 ==0 :
        return "valid !"
    else:
        return "invalid !"
print(checking_fct(code_num))
