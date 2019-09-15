#Receive the encoded string from your friend & decode it to check the original message. PS: You will receive Encoded string and the Algorithm used for encoding.
import codecs
str=input("Enter an encoded string or enter some string i'll encode and decode it back again using codecs module:")
y=codecs.encode(str, encoding='utf-8', errors='strict')
print("I have used encoding built-in funcion and encoded it :{}".format(y))
dec=codecs.decode(y, encoding='utf-8', errors='strict')
print("Now I have decoded back the encoded string:{}".format(dec))
