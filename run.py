import main_menu


"""
This program will allow you to create a property by entering information such as monthly income, expenses,
and total investment figures. When a property is created, the program will give you the expected Return On 
Investment over a 12 month period and add that property to your property list. Your property list is accessible
at any time and will list the property name and it's calculated ROI. Any property you have stored in your
list is viewable and editable at any time. Only total investment, total monthly income, and total monthly expenses are
able to be edited. After editing, a new ROI will be calculated based on the new information. Just run this file
to get started!
"""


calc = main_menu.Calculator()
calc.run()