


#---------------------------------------
#------- Control Flow-------
#-----If , Elif, Else-------
#---- Make Decision---------
#---------------------------------------



uName = "Salar"
uCountry = "USA"
cName = "Python "
cPrice = 100
cDiscount = 30
print(f"Hello {uName} The Course {cName.strip()} Price is {cPrice - cDiscount}$") # Hello Salar The Course Python Price is 70$
print(f"Hello {uName} The Course {cName.strip()} Price is {cPrice - 80}$") # Hello Salar The Course Python Price is 20$

if uCountry == "Deutschland" :
    print(f"Hello {uName} because yor are from {uCountry}") # Hello Salar because yor are from Deutschland
    print(f"The Course {cName.strip()} Price is {cPrice - 80}") # The Course Python Price is 20

elif uCountry == "KSA" :
    print(f"Hello {uName} because yor are from {uCountry}")
    print(f"The Course {cName.strip()} Price is {cPrice - 40}")

elif uCountry == "USA" :
    print(f"Hello {uName} because yor are from {uCountry}")
    print(f"The Course {cName.strip()} Price is {cPrice - 50}")
    


else :

    print(f"Hello {uName} because yor are from {uCountry}") # Hello Salar because yor are from Deutschland
    print(f"The Course {cName.strip()} Price is {cPrice - 30}")









