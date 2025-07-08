def convert_distance(): 
    print('From km to miles, type "MILES"')
    print('From miles to km, type "KM"')
    while True:
        conversion_km_miles = input("Convert to: ").upper() # get user to input and changing input to uppercase
        if conversion_km_miles == "MILES": # if user wants to conver from km to miles
            while True:
                try:
                    km = float(input("km: "))
                    break  # valid input, exit the loop
                
                except ValueError:
                    print("Invalid input. Please enter a number.")

            miles = km * 0.621371
            print(f"{km} km is equal to {miles} miles.")
            break # exit loop
            
        elif conversion_km_miles == "KM": # if user wants to convert from miles to km
            while True:
                try:
                    miles = float(input("miles: "))
                    break # valid input, exit the loop
                
                except ValueError:
                    print("Invalid input. Please enter a number.")
    
            km = miles / 0.621371
            print(f"{miles} miles is equal to {km} km.")
            break # exit loop
            
        else: 
            print("Error. Please input KM or MILES.") # if user input anything else other than km or miles
    
def convert_temperature():
    print('From Celsius to Fahrenheit, type "F"')
    print('From Fahrenheit to Celsius, type "C"')
    while True:
        conversion_C_F = input("Convert to: ").upper() # get user to input and changing input to uppercase
        if conversion_C_F == "F": # if user wants to convert from Celsius to Fahrenheit
            while True:
                try:
                    C = float(input("Celsius: "))
                    break # valid input, exit the loop
                
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
            F = C * 9/5 + 32
            print(f"{C} \u2103 is equal to {F} \u2109.")
            break # exit loop
            
        elif conversion_C_F == "C": # if user wants to comver from Fahrenheit to  Celsius
            while True:
                try:
                    F = float(input("Fahrenheit: "))
                    break # valid input, exit the loop
                
                except ValueError:
                    print("Invalid input. Please enter a number.")
          
            C = (F - 32) * 5 / 9
            print(f"{F} \u2109 is equal to {C} \u2103.")
            break # exit loop
            
        else: 
            print("Error. Please input C or F.")
    
def convert_weight():
    print('From kg to pounds, type "POUNDS"')
    print('From pounds to kg, type "KG"')
    while True:
        conversion_kg_pounds = input("Convert to: ").upper() # get user to input and changing input to uppercase
        if conversion_kg_pounds == "POUNDS": # if user wants to convert from kg to pounds
            while True:
                try:
                    KG = float(input("kg: "))
                    break # valid input, exit the loop
                
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
            POUNDS = KG * 2.20462
            print(f"{KG} kg is equal to {POUNDS} lb.")
            break # exit loop
                
        elif conversion_kg_pounds == "KG": # if user wants to convert from pounds to kg
            while True:
                try:
                    POUNDS = float(input("Pounds: "))
                    break # valid input, exit the loop
                
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
            KG = POUNDS / 2.20462
            print(f"{POUNDS} lb is equal to {KG} kg.")
            break # exit loop
                
        else: 
            print("Error. Please input KG or POUNDS.")

def main(): # the main program that will call other functions when prompted
    print("This is a Unit Conversion Program.")
    print("To convert:")
    print('1. Distance between km and miles, type "D".')
    print('2. Temperature between celsius and fahrenheit, type "T".')
    print('3. Weight between kg and pounds, type "W".')
    
    while True:
        conversion_type = input("Convert:").upper() # prompt user for type of conversion
    
        if conversion_type == "D":
            convert_distance() # goes to that function when needed
            break # exit loop
        
        elif conversion_type == "T":
            convert_temperature()
            break # exit loop
                
        elif conversion_type == "W":
            convert_weight()
            break # exit loop
                
        else:
            print("Error. Please input D, T or W.") # if user did not input a D,T or W
        
main()

    