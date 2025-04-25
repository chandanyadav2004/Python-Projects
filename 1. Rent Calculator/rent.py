# Inputs we need from the user
# Total rent
# Total food order for snacks
# Electricity bill and units
# Charge per unit for electricity
# Persons living in room/flat


# #Outputs

# Total amount to be paid by each person

rent= int(input("Enter your hostel/flat rent: "))
food = int(input("Enter your total food order for snacks: "))
electricity = int(input("Enter your electricity bill: "))


charge_per_unit = int(input("Enter the charge per unit for electricity: "))  
person=int(input("Enter the number of persons living in the room/flat: "))



#Calculating the total amount to be paid by each person
total_rent = rent + food + (electricity * charge_per_unit)
total_amount_per_person = total_rent / person
print("The total amount to be paid by each person is: ", total_amount_per_person)
