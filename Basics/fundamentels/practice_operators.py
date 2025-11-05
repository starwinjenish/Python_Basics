billing_amount = 1000
tax = billing_amount*0.18
total = billing_amount + tax
print(total)

if total > 10000:
   discount = 0.10*total
   total -= discount
print(total)

#
age = 70
student = "yes"
if age >=60 and student == "yes":
   print("yes discount")
else:
   print("no discount")
  