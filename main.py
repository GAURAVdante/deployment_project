from Cal_funcations import substract , add , multiplay

print(" Choose 1")
print(" 1. Addition \n 2. Substraction \n 3. Multiplication ")
q = int(input("Enter Number from 1 2 or 3 -->   "))
if q not in [1,2,3]:
    print("Invalid Value ")
else:
    
    a, b = map(int, input("Enter Space Seprated 2 Values  \n" ).split())
    if q==1:
        print(add(a,b))
    elif q==2:
        print(substract(a,b))
    else:
        print(multiplay(a,b))


 