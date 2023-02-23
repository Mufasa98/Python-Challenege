import os
import csv 

TotalMonths = -1
ProfitLossPerMonth = 0
NetProfitLoss = 0

Month1 = []
ProfitChangeMonthly = []
ProfitChange = int
Checker1 = int
Checker2 = int
MaxTicker = str
MinTicker = str



# Read in the file
Budget = os.path.join("C:\\Users\\musta\\OneDrive\\Desktop\\PythonCodes\\hw3\\PyBank\\Resources\\budget_data.csv")

#Part 1: Getting total months
with open(Budget) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter="-")
    for row in csvreader:
        TotalMonths = TotalMonths + 1

#Part 2: Getting NetProfitLoss
with open(Budget, encoding="utf") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")    
    next(csvreader, None)  

    
    for row in csvreader:
        ProfitLossPerMonth = row[1]
        NetProfitLoss = int(ProfitLossPerMonth) + (NetProfitLoss)

    #print(NetProfitLoss)

#Part 3: Getting monthly changes
with open(Budget) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    
    reader = list(csvreader)

    Counter = int(reader[0][1])

#Part 4: Getting greatest increase and greatest  decrease.
    Checker1 = int(reader[0][1])
    Checker2 = int(reader[0][1])

    for i in reader:    
        Month2 =   Counter - int(i[1])
        Counter = int(i[1])
        ProfitChangeMonthly.append(Month2)

        #Minimum
        if Month2 < Checker1:
            Checker1 = Month2
            MaxTicker = str(i[0])


        #Maximum
        elif Month2 > Checker2:
            Checker2 = Month2
            MinTicker = str(i[0])


    #print(ProfitChangeMonthly)
    ProfitChange = sum(ProfitChangeMonthly) / (len(ProfitChangeMonthly)-1)
    print(ProfitChange)

    ProfitChange = -abs(ProfitChange)
    Checker1 = abs(Checker1)
    Checker2 = -abs(Checker2)

    #print(Checker1)
    #print(MaxTicker)
    #print(MinCheck)

    #print(Checker2)    
    #print(MinTicker)
    #print(MaxCheck)



print(f"Finanicial Analysis")
print(f"---------------------------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${NetProfitLoss}") 
print(f"Average Change: ${ProfitChange}")
print(f"Greatest Increase in Profits: {MaxTicker}  {Checker1}")
print(f"Greatest Decrease in Profits: {MinTicker}  {Checker2}")

    
    
