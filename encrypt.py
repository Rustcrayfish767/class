# ui_password is the password that the user types
#encrypt_password is a function that takes the password that the user typed,  and returns the encrypted password. This encrypted password should match the one in the file.
#alphabet is the string containing the 26 alphabets 
def encrypt(enterpass):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 5
    encrypted_password =''
    for i in enterpass:
        position = alphabet.find(i)
        newposition = (position+key) % 26
        encrypted_password += alphabet[newposition]
    #debug print(encrypted_password)
    return(encrypted_password)
