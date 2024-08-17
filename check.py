num=int(input("enter your nbumber"))
if num <0:
    print("neg")

else:
    print("postive")

name=str(input("enter your nmae"))
eng=int(input("enter english marks:"))
urdu=int(input("enter urdu marks:"))
math=int(input("enter maths marks:"))
sci=int(input("enter sci marks:"))
add=(eng+urdu+math+sci)
per=add/400*100
print("total=",add,per,"%")
if per >=90:
    print("your name is:",name,"& your grade is 'A+'")
elif per >=80:
    print("B")

else:
    print("pass")
    




