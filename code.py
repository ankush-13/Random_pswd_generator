import random
import string 

pass_len = 12 
charValues = string.digits + string.ascii_letters + string.punctuation

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)     # USING STRING 

password = "".join([random.choice(charValues) for i in range(pass_len)])    # USING LIST COMPREHENSION 


print("Your random password is : ",password)
