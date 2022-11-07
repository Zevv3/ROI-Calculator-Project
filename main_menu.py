

#I should have 2 calculators
#One maybe for beginners that would be the one I already made
#The other should be an abridged version that requires less information.
# For example, monthly expenses would just ask for monthly expenses instead of going through
# Each one individually
#This would be better for someone who is fairly experienced but just wants an easy way to calculate
#also makes testing way easier

import Property_module
import Property_abridged_module
class Calculator:
    def __init__(self):
        self.properties = []
        self.propertiesDict = {}


    def get_names(self):
        for property in self.properties:
            self.propertiesDict[property.name] = property.roi
        return self.propertiesDict
        # return [property.name for property in self.properties]

    def create(self):
        name = None
        totalInvestment = None
        rent = None
        otherIncome = None
        tax = None
        insurance = None
        utilities = None
        vacancy = None
        repairs = None
        CapEx = None
        mortgage = None
        otherExpenses = None
        while True:
            if not name:
                name = input("\nWhat would you like to name your property? ")
                name = name.lower().strip()      
            if not totalInvestment:
                try:
                    totalInvestment = int(input("\nWhat would your total investment be? This would be any money you need to put into the property initially. This includes down payment, any closing costs, renovation costs, etc.\nTotal Investments: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue
            if not rent:
                try:
                    print("\nNow we will calculate the monthly income.")
                    rent = int(input("What will be the approximate monthly rent?  \nRent: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue
            if not otherIncome:
                try:
                    otherIncome = int(input("Will there be other sources of income such as laundry, storage, etc.? If no, input 0.  \nMisc. Income: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue
            
            if not tax:
                print("\nNow we will tally up the monthly expenses.")
                try:
                    tax = int(input("What is the approximate tax on the property?  \nTaxes: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue

            if not insurance:
                try:
                    insurance = int(input("What is the approximate insurance payment per month for the property?  \nInsurance: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue
                    
            if not utilities:
                try:
                    utilities = int(input("What is the approximate monthly utilites bill? You may choose to have your tenant pay this bill for you. If so, input 0. \n Utilities: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue
            if not vacancy:
                try:
                    print("Every property will be vacant for some amount of time. We recommend setting aside approximately 5% of the rental income to account for this vacancy time, but you can set aside more or less depending on how much time you expect the property to be vacant for.")
                    vacancy = int(input("How much would you like to set aside for vacancy time?  \nVacancy: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue
            if not repairs:
                try:
                    repairs = int(input("How much would you like to set aside for repairs every month?  \nRepairs: $ "))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue
            if not CapEx:
                try:
                    CapEx = int(input("How much would you like to set aside for capital expenditures each month? This would include things like structural repairs or appliance upgrades, etc. \nCapital Expenditures: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue

                    
            if not mortgage:
                try:
                    mortgage = int(input("What is the expected monthly mortgage on the property? \nMortgage: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue

            if not otherExpenses:
                try:
                    otherExpenses = int(input("Are there any additional monthly epenses such as a property manager, an HOA fee, or groundskeeping services? If not, input 0. \n Misc. Expenses: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue
            break
        newProperty = Property_module.Property(name, rent, otherIncome, tax, insurance, utilities, vacancy, repairs, CapEx, mortgage, otherExpenses, totalInvestment)
        while True:
            if newProperty.name not in [property.name for property in self.properties]:
                self.properties.append(newProperty)
            else:
                print(f"{newProperty.name} is already in your property list. You will have to re-name it to add it to the list.")
                newProperty.name = input("What would you like to re-name this property?\n")
                continue
            break

    def create_abridged(self):
        name = None
        totalInvestment = None
        monthlyIncome = None
        monthlyExpenses = None
        while True:
            if not name:
                name = input("\nWhat would you like to name your property? ")
                name = name.lower().strip()      
            if not totalInvestment:
                try:
                    totalInvestment = int(input("\nWhat would your total investment be? This would be any money you need to put into the property initially. This includes down payment, any closing costs, renovation costs, etc.\n Total Investments: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue
            if not monthlyIncome:
                try:
                    monthlyIncome = int(input("What will be the approximate monthly income? This includes rent and any other services your tenants will be paying for.  \nMonthly Income: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue    
            if not monthlyExpenses:
                try:
                    monthlyExpenses = int(input("What do you expect the monthly expenses to be? This includes things like property tax, property managers, repairs, mortgage, etc.  \nMonthly Expenses: $"))
                except:
                    print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                    continue
            break
        newProperty = Property_abridged_module.Property_abridged(name, totalInvestment, monthlyIncome, monthlyExpenses)
        while True:
            if newProperty.name not in [property.name for property in self.properties]:
                self.properties.append(newProperty)
            else:
                print(f"{newProperty.name} is already in your property list. You will have to re-name it to add it to the list.")
                newProperty.name = input("What would you like to re-name this property?\n")
                continue
            break
    def run(self):
        
        print("\nWant to make some easy money? Try commoditizing basic human necesseties by investing in real estate!")
        print("Welcome to the ROI calculator!")
        while True:
            self.get_names()
            print("""
                Options:
                [1] -- Use Calculator
                [2] -- View your Property List
                [3] -- View a Property on your List
                [4] -- Add a Property to your list - full
                    Full walkthrough of all the components of a property that will affect the ROI
                [5] -- Add a Property to your list - abridged
                    For those who are more experienced investors who don't need a full breakdown
                    of the componenets of a property that will affect the ROI
                [6] -- Remove a Property from your List
                [7] -- Edit a Property
                [8] -- Quit
            """)
            action = input("Please choose an option from the list above: ")
            if action.lower().strip() in ("1", "one", "use", "use calculator", "calculator"):
                if self.properties == []:
                    print("You have no properties saved on our database. This application will ask for details about your new property in order to calculate the ROI.")
                    while True:
                        ask = input("Would you like to use the full property creator or the abridged version? (full/abridged) ")
                        if ask.lower().strip() in ('full', 'f'):
                            self.create()                   
                            currentProperty = self.properties[-1]
                            currentProperty.calc()
                            break
                        elif ask.lower().strip() in ('abridged','a'):
                            self.create_abridged()
                            currentProperty = self.properties[-1]
                            currentProperty.calc()
                            break
                        elif ask.lower().strip() in ('quit', 'q'):
                            break
                        else:
                            print("There was an error. Please choose from one of the options provided.")
                            continue
                else:
                    print("Choose a property from the list of your saved properties below. Or enter 'new' to calculate ROI of a different property.")
                    print(self.get_names())
                    choice = input("")
                    if choice.lower().strip() in ('new', 'n'):
                        while True:
                            ask = input("Would you like to use the full property creator or the abridged version? (full/abridged) ")
                            if ask.lower().strip() in ('full', 'f'):
                                self.create()                   
                                currentProperty = self.properties[-1]
                                currentProperty.calc()
                                break
                            elif ask.lower().strip() in ('abridged','a'):
                                self.create_abridged()
                                currentProperty = self.properties[-1]
                                currentProperty.calc()
                                break
                            elif ask.lower().strip() in ('quit', 'q'):
                                break
                            else:
                                print("There was an error. Please choose from one of the options provided.")
                                continue
                    elif choice.lower().strip() in self.get_names():
                        for property in self.properties:
                            if property.name == choice:
                                property.calc()
                        continue
                    else:
                        print(f"{choice} was not found in your property list.")
                        continue
            elif action.lower().strip() in ("2", 'two', 'view list', 'view property list'):
                print(self.get_names())
                continue
            elif action.lower().strip() in ("3", 'three', 'view property'):
                print(self.propertiesDict)
                choice = input("What property would you like to view? ")
                if choice.lower().strip() in self.get_names():
                    for property in self.properties:
                        if property.name == choice:
                            print(property.__dict__)
                            continue
                else:
                    print(f"{choice} was not found in your property list.")
                    continue
            elif action.lower().strip() in ("4", 'four', 'full'):
                self.create()                 
                currentProperty = self.properties[-1]
                currentProperty.calc()
                continue
            elif action.lower().strip() in ('5', 'five', 'abridged'):
                self.create_abridged()
                currentProperty = self.properties[-1]
                currentProperty.calc()
                continue
            elif action.lower().strip() in ('6', 'six' 'remove', 'remove property'):
                print(self.get_names())
                choice = input("What property would you like to remove? ")
                if choice.lower().strip() in self.get_names():
                    for property in self.properties:
                        if property.name == choice:
                            self.properties.remove(property)
                            continue
                else:
                    print(f"{choice} was not found in your property list.")
                    continue
            elif action.lower().strip() in ('7', 'seven', 'edit', 'edit property'):
                print(self.get_names())
                choice = input("What property would you like to edit? ")
                if choice.lower().strip() in self.get_names():
                    for property in self.properties:
                        if property.name == choice:
                            property.alter()
                            continue
                else:
                    print(f"{choice} was not found in your property list.")
                    continue
            elif action.lower().strip() in ('8','eight', 'quit', 'q'):
                break
            else:
                print("There was an error. Please enter one of the given options.")
                continue
# calc = Calculator()
# calc.run()
