import hashlib
import os


salt = os.urandom(32)
text = input("Enter the String that needs to be encoded : ")
text2 = salt.hex() + text + salt.hex()
rep = 5

print("String after single Salting : "+text2)
while(rep > 0) :
    salt = os.urandom(32)
    text2 = salt.hex()+text2+salt.hex()
    rep = rep - 1

print("String after multiple  Salting : " + text2)


md5_encoding = hashlib.md5(text2.encode())
sha256_encoding = hashlib.sha256(text2.encode())
sha512_encoding = hashlib.sha512(text.encode())

print("The required hash value using MD5 algorithm is : " + md5_encoding.hexdigest())
print("The required hash value using SHA256 algorithm is : " + sha256_encoding.hexdigest())
print("The required hash value using SHA512 algorithm is : " + sha512_encoding.hexdigest())

