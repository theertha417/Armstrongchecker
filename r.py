n= int(input('enter your number'))
num=n
numberofdigit=len(str(n))
sum=0
while n >0:
    digit=n%10
    sum+=digit**numberofdigit
    n//=10

if sum==num:
    print("armstrong number")
else:
    print ("not armstrong number")

