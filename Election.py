import os
import csv 

Counter = 0

CandidateName = []
CandidateList = []


VoterCount1 = 0
VoterCount2 = 0
VoterCount3 = 0
VoterCount1Percent = 0
VoterCount2Percent = 0
VoterCount3Percent = 0


# Read in the file
Polls = os.path.join("C:\\Users\\musta\\OneDrive\\Desktop\\PythonCodes\\hw3\\PyPoll\\Resources\\election_data.csv")

with open(Polls) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    reader = list(csvreader)

    for rows in reader:
        CandidateName = rows[2]
        if CandidateName not in CandidateList:
            CandidateList.append(CandidateName)

    for rows in reader:
        Counter += 1
        
        if rows[2] == CandidateList[0]:
            VoterCount1 += 1
        elif rows[2] == CandidateList[1]:
            VoterCount2 += 1
        elif rows[2] == CandidateList[2]:
            VoterCount3 +=1

VoterCount1Percent = VoterCount1 / Counter * 100
VoterCount2Percent = VoterCount2 / Counter * 100
VoterCount3Percent = VoterCount3 / Counter * 100

VoterCount1Percent = round(VoterCount1Percent,3)
VoterCount2Percent = round(VoterCount2Percent,3)    
VoterCount3Percent = round(VoterCount3Percent,3)

#print(VoterCount1Percent)
#print(VoterCount2Percent)
#print(VoterCount3Percent)

Max = max(VoterCount1,VoterCount2,VoterCount3)

if Max == VoterCount1:
    Winner = CandidateList[0]
elif Max == VoterCount2:
    Winner = CandidateList[1]
elif Max == VoterCount3:
    Winner = CandidateList[2]

#print(Winner)
print(f"Election Results")
print(f"-------------------------------")
print(f"Total Votes: {Counter}")
print(f"-------------------------------")
print(f"{CandidateList[0]}: {VoterCount1Percent}% ({VoterCount1})")
print(f"{CandidateList[1]}: {VoterCount2Percent}% ({VoterCount2})")
print(f"{CandidateList[2]}: {VoterCount3Percent}% ({VoterCount3})")
print(f"-------------------------------")
print(f"Winner: {Winner}")
print(f"-------------------------------")



#Print conclusions into new file
with open("C:\\Users\\musta\\OneDrive\\Desktop\\PythonCodes\\hw3\\PyPoll\\Resources\\Analysis.txt","w", newline="") as Text_file:
    #Text_file.write(
    WinningCandidateSummary = (f"""Election Results
        -------------------------------
        Total Votes: {Counter}
        -------------------------------
        {CandidateList[0]}: {VoterCount1Percent}% ({VoterCount1})
        {CandidateList[1]}: {VoterCount2Percent}% ({VoterCount2})
        {CandidateList[2]}: {VoterCount3Percent}% ({VoterCount3})
        -------------------------------
        Winner: {Winner}
        -------------------------------""")

    print(WinningCandidateSummary)
    Text_file.write(WinningCandidateSummary)

#print(Voter1)
#print(VoterCount1)
#print(Voter2)
#print(VoterCount2)
#print(Voter3)
#print(VoterCount3)
#print(Counter)

#with open("your file path here","w", newline="") as csvfile:
    #csvfile.write(what you want to write here)