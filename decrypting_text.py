text=input("donner votre que vous voulez le decrypté :")
key = input("donner le key :")
alphabets="abcdefghijklmnopqrstuvwxyz"
decrypted_text = ""
def decry(text,key):
    i=0
    global decrypted_text
    for char in text:
        if char == ' ':
            decrypted_text+=' '
        else:
            index_text=alphabets.find(char)
            index_key=alphabets.find(key[i])
            decrypted_text+=alphabets[(index_text-index_key)%len(alphabets)]
            i=(i+1)%len(key)
    print(decrypted_text)
decry(text.lower(),key.lower())
