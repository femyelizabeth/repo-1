#HCF
num1=int(input("Enter 1st numbers:"))
num2=int(input("Enter 2nd number:"))
if(num1>num2):
   min=num2
else:
   min=num1
for i in range(1, min+1):
   if((num1 % i == 0) and (num2 % i == 0)):
      hcf=i
print(hcf)
