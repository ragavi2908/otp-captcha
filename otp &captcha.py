import random
otp_num=random.randint(0000,9999)
print("your otp number is :",otp_num)


import string
import random
captcha="".join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=5))
print("your captcha is:",captcha)
