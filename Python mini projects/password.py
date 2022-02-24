import random
num = "0123456789"
alph = "abcdefghijklmnopqrstuvwxyz"
capalp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sp = "@#$%&*}{"
password = num+alph+capalp+sp
dig = 11

pas = "".join(random.sample(password,dig))
print("your password is :  ",pas)
