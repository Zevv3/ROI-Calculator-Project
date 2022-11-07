# import main_menu

class Property():
    def __init__(self, name, rent, otherIncome, tax, insurance, utilities, vacancy, repairs, CapEx, mortgage, otherExpenses, totalInvestment):
        self.name = name
        self.rent = rent
        self.otherIncome = otherIncome
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.vacancy = vacancy
        self.repairs = repairs
        self.CapEx = CapEx
        self.mortgage = mortgage
        self.otherExpenses = otherExpenses
        self.totalInvestment = totalInvestment
        self.monthlyIncome = self.rent + self.otherIncome
        self.monthlyExpenses = self.tax + self.insurance + self.utilities + self.vacancy + self.repairs + self.CapEx + self.mortgage + self.otherExpenses
        self.roi = None
        

    def calc(self):
        monthlyCashFlow = self.monthlyIncome  - self.monthlyExpenses
        self.roi = ((monthlyCashFlow * 12)/self.totalInvestment) * 100
        self.roi = round(self.roi,2)
        print(f"Your Annual Return On Investment is {self.roi}%.")

    def get_name(self):
        return self.name

    def alter(self):
        while True:
            tempDict = {'Monthly Income': self.monthlyIncome, 'Monthly Expenses': self.monthlyExpenses, 'Total Investment': self.totalInvestment}
            print(tempDict)
            ask = input("What value would you like to edit? ")
            if ask.lower().strip() in ('monthly income', 'income'):
                while True:
                    try:
                        new = int(input(f"What would you like to change the monthly income to? \n$"))
                        self.monthlyIncome = new
                        self.calc()
                        break
                    except:
                        print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                        continue
                break
            elif ask.lower().strip() in ('monthly expenses', 'expenses'):
                while True:
                    try:
                        new = int(input("What would you like to change the monthly expenses to? \n$"))
                        self.monthlyExpenses = new
                        self.calc()
                        break
                    except:
                        print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                        continue
                break
            elif ask.lower().strip() in ('total investment', 'investment', 'total'):
                while True:
                    try:
                        new = int(input("What would you like to change the total investment to? \n$"))
                        self.monthlyExpenses = new
                        self.calc()
                        break
                    except:
                        print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
                        continue
                break
            elif ask.lower().split() in ('quit','q'):
                break
            else: 
                print("There was an error. Please choose a valid option.")
                continue




# def create():
#     name = None
#     totalInvestment = None
#     rent = None
#     otherIncome = None
#     tax = None
#     insurance = None
#     utilities = None
#     vacancy = None
#     repairs = None
#     CapEx = None
#     mortgage = None
#     otherExpenses = None
#     while True:
#         if not name:
#             name = input("\nWhat would you like to name your property? ")
#             name = name.lower().strip()      
#         if not totalInvestment:
#             try:
#                 totalInvestment = int(input("\nWhat would your total investment be? This would be any money you need to put into the property initially. This includes down payment, any closing costs, renovation costs, etc.\n$"))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 continue
#         if not rent:
#             try:
#                 print("\nNow we will calculate the monthly income.")
#                 rent = int(input("What will be the approximate monthly rent?  \n$"))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 continue
#         if not otherIncome:
#             try:
#                 otherIncome = int(input("Will there be other sources of income such as laundry, storage, etc.? If no, input 0.  \n$"))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 continue
        
#         if not tax:
#             print("\nNow we will tally up the monthly expenses.")
#             try:
#                 tax = int(input("What is the approximate tax on the property?  \n$"))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 continue

#         if not insurance:
#             try:
#                 insurance = int(input("What is the approximate insurance payment per month for the property?  \n$"))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 insurance = int(input("What is the approximate insurance payment per month for the property?  \n$"))
                
#         if not utilities:
#             try:
#                 utilities = int(input("What is the approximate monthly utilites bill? You may choose to have your tenant pay this bill for you. If so, input 0. \n$"))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 continue
#         if not vacancy:
#             try:
#                 print("Every property will be vacant for some amount of time. We recommend setting aside approximately 5% of the rental income to account for this vacancy time, but you can set aside more or less depending on how much time you expect the property to be vacant for.")
#                 vacancy = int(input("How much would you like to set aside for vacancy time?  \n$"))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 continue
#         if not repairs:
#             try:
#                 repairs = int(input("How much would you like to set aside for repairs every month?  \n$ "))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 continue
#         if not CapEx:
#             try:
#                 CapEx = int(input("How much would you like to set aside for capital expenditures each month? This would include things like structural repairs or appliance upgrades, etc. \n$"))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 continue

                
#         if not mortgage:
#             try:
#                 mortgage = int(input("What is the expected monthly mortgage on the property? \n$"))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 continue

#         if not otherExpenses:
#             try:
#                 otherExpenses = int(input("Are there any additional monthly epenses such as a property manager, an HOA fee, or groundskeeping services? If not, input 0. \n$"))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 continue
#         break
#     newProperty = Property(name, rent, otherIncome, tax, insurance, utilities, vacancy, repairs, CapEx, mortgage, otherExpenses, totalInvestment)
#     while True:
#         if newProperty not in self.get_names():
#             self.properties.append(newProperty)
#         elif newProperty in self.get_names():
#             print(f"{newProperty} is already in your property list. You will have to re-name it to add it to the list.")
#             newProperty = input("What would you like to re-name this property?\n")
#             continue
#         break
    
    # print(name.__dict__)