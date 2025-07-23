'''This Is Our First Assiment In this Path Of Learning So Injoy Reading It
First Ex. Is about How To Calculat a Profit ,second Ex. Is About How To Make A Rate Of Return
Calculator, And The Last Ex. basically It's A String XD'''

#Profit Calculator:
'''print("----------------------------------------------------------------------------")
print("Hello Sir","This Is A Profit Calculator","Use It To calculat Ur Profit",sep="\n")
print("----------------------------------------------------------------------------")

def calculating_Profits():
    ur_revenue = float(input("\nsir can u write ur revenue down here pls: "))
    ur_expenses = float(input("\nand here u may Write ur expenses pls: "))

    ur_profit = ur_revenue - ur_expenses

    print(f"\nur revenue is:{ur_revenue},and ur expenses is:{ur_expenses}") #I Tried here to make the code Elegant ;)
    
    return print(f"\nso this is ur profit sir:{ur_profit}")

calculating_Profits()

print("\n")

#Rate Of Return:
print("----------------------------------------------------------------------------")
print("Hello Sir, This Is An Calculator To Get The Rate Of Return",sep="\n")
print("----------------------------------------------------------------------------")

initial_price = float(input("\nEnter Ur Initical Price pls"))
future_price = float(input("\nEnter The Future Predect pls"))

rate_of_return = (initial_price - future_price / initial_price) * 100 #this is the Rate Of Return Equancion ask ChatGPT if u want

print(f"\nThis Is The Best Rate I Can Give U:{rate_of_return}%")

if rate_of_return > 0 :
    print("True")
else:
    print("false")

print("\n")

#String:
print("----------------------------------------------------------------------------")
print("Hello Sir, This Is An Calculator To Get The Rate Of Return",sep="\n")
print("----------------------------------------------------------------------------")

name = input("\nCan U Pls Enter Ur Name:").capitalize()
age = input("\nmay u insert ur age pls:")
city_name = input("\npls input ur city name pls:").capitalize()

print(f"Hello{name}, Happy birthday!You're {age} years old now :) Do you need to find a nice restaurant in {city_name} to celebrate?",sep="\n")'''

#Bonus
#print("""this is an f-string in python, it looks like this: "f\"{var_name}\"" """)
