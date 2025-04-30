Premium_Ground_shipping = 125.00

weight = 30
cost=int(0)
cheapest_option1= int(0)
cheapest_option3= int(0)

print("Welcome to Sal's Shipping")
print("Your options for shipping with us are the folloing:")
print("\n")
#Ground Shipping 
if weight <= 2 and weight>=0:
  cost=(weight*1.50)+20
  print("1. Ground Shipping.You will be charged $",cost)
elif weight >2 and weight <= 6:
  cost=(weight*3.00)+20
  print("1. Ground Shipping.You will be charged $",cost)
elif weight >6 and weight <= 10:
  cost=(weight*4.00)+20
  print("1. Ground Shipping.You will be charged $",cost)
elif weight >10:
  cost=(weight*4.75)+20
  print("1. Ground Shipping.You will be charged $",cost)
else: 
  print("Weight is less than 0")
cheapest_option1= cost

print("2. Premium Ground Shipping.You will be charged $",Premium_Ground_shipping)

#Drone Shipping

if weight <= 2 and weight>=0:
  cost=weight*4.50
  print("3. Drone Shipping.You will be charged $", cost)
elif weight >2 and weight <= 6:
  cost=weight*9.00
  print("3. Drone Shipping.You will be charged $",cost)
elif weight >6 and weight <= 10:
  cost=weight*12.00
  print("3. Drone Shipping.You will be charged $",cost)
elif weight >10:
  cost=weight*14.25
  print("3. Drone Shipping.You will be charged $",cost)
else: 
  print("Weight is less than 0")
cheapest_option3= cost

print("\n")
if cheapest_option1 < Premium_Ground_shipping and cheapest_option1 < cheapest_option3:
  print ("Ground Shipping is the cheapest.Let's go ahead with it")
elif cheapest_option3 < Premium_Ground_shipping and cheapest_option3 < cheapest_option1:
  print ("Drone shipping is the cheapest. Let's go ahead with it")
elif Premium_Ground_shipping < cheapest_option3 and Premium_Ground_shipping < cheapest_option1:
  print ("Premium Ground Shipping is the cheapest. Let's go ahead with it")
elif cheapest_option1 == Premium_Ground_shipping and  cheapest_option1<= cheapest_option3:
  print("Ground shipping and Premium Ground are same price and cheapest. You can choose any of these")  
elif cheapest_option3 == Premium_Ground_shipping and  cheapest_option3<= cheapest_option1:
  print("Premium Ground Shipping and Drone shipping are same price and cheapest. You can choose any of these")
elif cheapest_option3 == cheapest_option1 and cheapest_option3<= Premium_Ground_shipping:
  print("Ground Shipping and Drone shipping are same price and cheapest. You can choose any of these")
else:
  print("All three options are the same price. You can choose any")  
