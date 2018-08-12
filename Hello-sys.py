import hashlib

b = hashlib.md5()
print(b.digest())
print(b.hexdigest)


import sys

print(sys.platform)



from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)

cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b"SuperSecretPassword")   #required to be bytes
print(ciphered_text)
unciphered_text = (cipher_suite.decrypt(ciphered_text))
print(unciphered_text)

import getpass

print (getpass.getuser())