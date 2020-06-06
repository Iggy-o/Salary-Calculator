'''
Ighoise Odigie
June 1, 2020
Youtube: https://www.youtube.com/channel/UCud4cJjtCjEwKpynPz-nNaQ?
Github: https://github.com/Iggy-o
Preview: https://repl.it/@IghoiseO/Sorter-Plus#script.js
'''

#<!--Welcome Script-->
separator = '-'*10
print(f"\nSALARY CALCULATOR™\n{separator}")

#<!--Creating Input Variables-->
#Collecting user name info
userName = str(input("\nWelcome, I am 'B-47', your personal salary bot...\n\nWhat is your name? -> "))

#Collecting user data on worked hours
greeting = f"\n{separator}\n\nHello {userName}, now let's get some information on your financial state..."
hoursWorked = float(input(f"{greeting}\n\n1) How many hours do you work bi-weekly? (Numerical Value) -> "))

#Collecting user hourly pay rate data
hourlyPayRate =  float(input("\n2) How much are you paid hourly? (Numerical Value) -> "))

#Collecting user tax data
tax = float(input("\n3) What is your tax rate? (Numerical Value) -> "))
#totalSales = float(input("\n3) What is the worth of your sales in the last two weeks? (Numerical Value) -> "))

#Collecting user expenses data
#monthlyExpenses = float(input("\n4) How much are your average monthly expenses? (Numerical Value) -> "))



#<!--Calculating the User's Paycheck-->
#Calculating the user's paycheck before taxes
payCheckAmount_untaxed = hoursWorked * hourlyPayRate

#Calculating the paycheckAmount after taxes
taxRate = tax
payCheckAmount_taxed = payCheckAmount_untaxed * (100 - taxRate)/100


#<!--Calculating the yearly, monthly and biweekly pay-->
#Calculating biweekly pay
biweeklyPay = round((payCheckAmount_untaxed), 2)
biweeklyPay_Taxed = round((payCheckAmount_taxed), 2)

#Calculting monthly pay
monthlyPay = round((biweeklyPay * 2), 2)
monthlyPay_Taxed = round((biweeklyPay_Taxed * 2), 2)

#Calculating yearly pay
yearlyPay =  round((monthlyPay * 12), 2)               
yearlyPay_Taxed = round((monthlyPay_Taxed * 12), 2)     


#<!--Printing the Results-->
#Creating the user message
stats = f"Bi-weekly Net Income -> ${str(biweeklyPay)}\n Taxed Bi-weekly Net Income -> ${str(biweeklyPay_Taxed)}\n\n\
Monthly Net Income -> ${str(monthlyPay)}\n Taxed Monthly Net Income -> ${str(monthlyPay_Taxed)}\n\n\
Yearly Net Income -> ${str(yearlyPay)}\n Taxed Yearly Net Income -> ${str(yearlyPay_Taxed)}"

message =  f"\nOkay {userName}, Based on this data, these are your personalized statistics:\n\n{stats}"

#Printing the message
print(f"\n{separator}{message}")

#<!--Program Complete-->