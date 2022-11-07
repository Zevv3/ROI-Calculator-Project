# import main_menu

class Property_abridged():
    def __init__(self, name, totalInvestment, monthlyIncome, monthlyExpenses):
        self.name = name
        self.monthlyIncome = monthlyIncome
        self.monthlyExpenses = monthlyExpenses
        self.totalInvestment = totalInvestment
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

# def create_abridged():
#     name = None
#     totalInvestment = None
#     monthlyIncome = None
#     monthlyExpenses = None
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
#         if not monthlyIncome:
#             try:
#                 monthlyIncome = int(input("What will be the approximate monthly income? This includes rent and any other services your tenants will be paying for.  \n$"))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 continue    
#         if not monthlyExpenses:
#             try:
#                 monthlyExpenses = int(input("What do you expect the monthly expenses to be? This includes things like property tax, property managers, repairs, mortgage, etc.  \n$"))
#             except:
#                 print("Something went wrong. Please make sure you entered a numerical value with no special characters and try again.")
#                 continue
#         break
#     newProperty = Property_abridged(name, totalInvestment, monthlyIncome, monthlyExpenses)
#     while True:
#         if newProperty not in main_menu.properties:
#             main_menu.properties.append(newProperty)
#         elif newProperty in main_menu.properties:
#             print(f"{newProperty} is already in your property list. You will have to re-name it to add it to the list.")
#             newProperty = input("What would you like to re-name this property?\n")
#             newProperty.add()
#         break