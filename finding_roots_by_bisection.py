from math import ceil
def root_fct(num,a,b,int_lenght_stop=0.01):
    if num<0:
        raise ValueError("il faut un nbr positif !!")
    while b-a > int_lenght_stop:
        c=(a+b)/2
        if c**2<num:
            a=c
        else:
            b=c
    return (a+b)/2
num=float(input("donner votre nombre :"))
intervalle=input("donner l'intervalle en cette forme : a,b  :")
length=float(input("donner la longueur de votre intervalle (par defaut elle va être 0.01 :"))
a=float((intervalle.split(','))[0])
b=float((intervalle.split(','))[1])
print(ceil(root_fct(num,a,b,length)))
