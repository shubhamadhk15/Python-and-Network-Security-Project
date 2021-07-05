
import hashlib

text = input("Enter the String that needs to be encoded : ")

md5_encoding = hashlib.md5(text.encode())
sha256_encoding = hashlib.sha256(text.encode())
sha512_encoding = hashlib.sha512(text.encode())



print("The required hash value using MD5 algorithm is : " + md5_encoding.hexdigest())
print("The required hash value using SHA256 algorithm is : " + sha256_encoding.hexdigest())
print("The required hash value using SHA512 algorithm is : " + sha512_encoding.hexdigest())

