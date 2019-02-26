h=int(input("nhap chieu cao(cm): "))
m=int(input("nhap can nang(kg): "))
h=h/100
bmi=m/(h*h)
if(bmi<16): print("Severely underweight")
elif(bmi<18.5): print("Underweight")
elif(bmi<25): print("Normal")
elif(bmi<30): print("Overweight")
else: print("Obese")
