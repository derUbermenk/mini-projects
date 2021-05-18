import csv
from classRespondent import Respondent as Re

numRespondents = 300 + 1

i = 0
with open('tabulatedResults.csv','w', newline='') as file:
    writer = csv.writer(file)
    while i < numRespondents:
        i+=1
        a = Re()
        writer.writerow([i,a.region, a.salary_PrP, a.salary_now,
                         a.emp_PrP, a.uEmp_PrP,
                         a.familySize, a.numStudents,
                         a.emp_now, a.uEmp_now,
                         a.budget["food"], a.budget["houseRent"],
                         a.budget["utilities"], a.budget["transport"],
                         a.budget["communication"], a.budget["education"],
                         a.budget["others"], a.budget["savings"]])
        

print("done tabulating")