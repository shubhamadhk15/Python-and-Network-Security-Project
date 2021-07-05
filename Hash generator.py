
import hashlib

text = input("Enter the String that needs to be encoded : ")

text_encoding = hashlib.md5(text.encode())

final_result = text_encoding.hexdigest()


print("The required hash value is : " + final_result)