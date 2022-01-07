#Danielle Raskin 20936398

def caeser_cipher(string, key):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    dict = {} 
    for i in range(0, len(alphabet)):
        j = (i + key) % len(alphabet) 
        dict[alphabet[i]] = alphabet[j]

    result = ''

    for c in string:
        if c in dict.keys():
            result += dict[c]
        else:
            result += c
    
    return print(result) 
    










