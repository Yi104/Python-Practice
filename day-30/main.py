

# try:
#     file = open("a_file.txt")
# except:
#     file = open("a_file.txt","w")
#
#     # except, except, else, finally
#     # raise: raise own exception


height = float(input("height:"))
weight = float(input("weight:"))

if height > 3:
    raise ValueError("Human height should not be over 3 m")
if weight > 200:
    raise ValueError("Human weight should not exceed 200 kg")

bmi = weight/ height **2
print(bmi)