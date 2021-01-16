import hashlib

found_pass = 0
#user input with input() method not working
input_hash = "dc53fc4f621c80bdc2fa0329a6123708"
dictionary = "archive.txt"

try:
    pass_file = open (dictionary, 'r')
except:
    print("Error" + dictionary + "not found")

for word in pass_file:
    cipher_word = word.encode('utf-8')
    hashed_word = hashlib.md5(cipher_word.strip())
    digest = hashed_word.hexdigest()

    if digest == input_hash:
        print("Found password: " + word)
        found_pass = 1
        break

if not found_pass:
    print("Password not found in file.")