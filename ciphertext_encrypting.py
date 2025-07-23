text = input("donner votre mot afin de le crypté : ")
key = input("donner le key :")
alphabets = "abcdefghijklmnopqrstuvwxyz"
encryption_text = ''
def encry(text,key):
    global encryption_text
    i=0
    for char in text:
        if char==' ':
            encryption_text+=' '
        else:
            key_index=alphabets.find(key[i])
            index_text = alphabets.find(char)
            encryption_text+=alphabets[(index_text+key_index)%len(alphabets)]
            i=(i+1)%len(key)
    print(encryption_text)
encry(text.lower(),key.lower())