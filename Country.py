#Cesar Murillo 
#CIS261
#Country

def display_menu():
    print("Welcome To The Country Code Manager!\n")
    print("1. Display A Country")
    print("2. Add A Country")
    print("3. Delete A Country")
    print("4. Exit")
    
def display_country_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "\nCountry Codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)

def display_country_details(countries):
    display_country_codes(countries)
    code = input("\nEnter Country Code: ").upper()
    if code in countries:
        name = countries[code]
        print(f"\nCountry Name: {name}.\n")
    else:
        print("\nThere Is No Country With That Code.\n")
        
def add_country(countries):
    code = input("\nPlease Enter The Country Code: ").upper() 
    if code in countries:
        name = countries[code]
        print(f"\n{name} Is Already Using Code.\n")
    else:
        name = input("\nEnter The Country Name: ").title()
        countries[code] = name
        print(f"\nThe Country {name} With Code {code} Was Added Successfully.\n") 
        
def delete_country(countries):
    code = input("\nEnter The Country Code To Delete: ").upper() 
    if code in countries:
        name = countries.pop(code) 
        print(f"\nThe Country With Code {code} Has Been Deleted.\n")
    else:
        print("Invalid Code, Please Try Again.\n")
        
def main():
    countries = {"MX": "Mexico", "US": "United States", "ES": "Spain", "IE": "Ireland"}
    
    while True:
        display_menu()
        selection = input("\nEnter Your Selection (1-4): ")
        if selection == '1':
            display_country_details(countries)
        elif selection == '2':
            add_country(countries)
        elif selection == '3':
            delete_country(countries)
        elif selection == '4':
            print("\nThank You For Using The Country Code Manager!")
            break
        else:
            print("\nInvalid Command, Please Try Again.\n")

if __name__ == "__main__":
    main()