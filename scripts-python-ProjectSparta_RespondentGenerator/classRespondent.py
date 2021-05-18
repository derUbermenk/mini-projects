class Respondent:
    @staticmethod
    def genList(start, stop, step):
        list = []
        while start < stop:
            start += step
            list.append(start)
        return list

    def __init__(self):
        #_PrP refers to pre pandemic
        #_now refers to present
        #uEmp is unemployed
        #emp is employed
        self.region = self.getRegion()
        self.salary_PrP = self.getSalary_PrP(region = self.region)
        self.familySize = self.getFamilySize(salary_PrP=self.salary_PrP)
        self.numStudents = self.getNumStudents(familySize=self.familySize)
        self.emp_PrP = self.getEmp_PrP(familySize=self.familySize,numStudents=self.numStudents)
        self.uEmp_PrP = self.getuEmp_PrP(familySize=self.familySize, numStudents= self.numStudents,emp_PrP=self.emp_PrP )
        self.emp_now = self.getEmp_now(emp_PrP=self.emp_PrP)
        self.salary_now = self.getSalary_now(salary_PrP=self.salary_PrP,emp_PrP=self.emp_PrP,emp_now=self.emp_now)
        self.uEmp_now = self.getuEmp_now(emp_PrP=self.emp_PrP,emp_now=self.emp_now ,uEmp_PrP=self.uEmp_PrP)
        self.budget = self.getBudgetAllocation(salary_now=self.salary_now,region=self.region,familySize=self.familySize,
                                               numStudents=self.numStudents)


    def getRegion(self):
        import numpy.random as nr
        regions = ['Region V - Bicol Region', 'NCR - National Capital Region',
                   'Region III - Central Luzon', 'Region VII - Central Visayas',
                   'Region IVA - CALABARZON', 'CAR - Cordillera Administrative Region',
                   'Region I - Ilocos Region']

        respondentDistribution = [0.28, 0.28, 0.19, 0.03, 0.16, 0.03, 0.03]
        return nr.choice(regions,p = respondentDistribution)


    def getSalary_PrP(self,region):
        import numpy
        salaries = [3500, 13500, 23000, 32500, 41500, 47500, 6000, 72500, 80000]
        regionDistribution = {'CAR - Cordillera Administrative Region': [0.2,0.18,0.18,0.32,0.05,0.03,0.02,0.01,0.01],
                              'NCR - National Capital Region': [0.06,0.11,0.13,0.25,0.34,0.07,0.02,0.01,0.01],
                              'Region I - Ilocos Region': [0.11,0.09,0.11,0.3,0.11,0.11,0.07,0.08,0.02],
                              'Region IVA - CALABARZON': [0.01,0.05,0.11,0.2,0.37,0.13,0.11,0.02,0.0],
                              'Region V - Bicol Region': [0.11,0.15,0.18,0.25,0.15,0.02,0.11,0.01,0.02],
                              'Region VII - Central Visayas': [0.01,0.35,0.26,0.18,0.11,0.05,0.02,0.01,0.01],
                              'Region III - Central Luzon': [0.01,0.05,0.11,0.2,0.37,0.13,0.11,0.02,0.0]}

        for key in regionDistribution.keys():
            if key == region:
                salaryProbabilities = regionDistribution[key]
                salary_PrP = numpy.random.choice(salaries, p = salaryProbabilities)
                return salary_PrP



    def getSalary_now(self,salary_PrP, emp_PrP ,emp_now):
        import numpy

        if emp_now == emp_PrP:
            salary_now = salary_PrP
        elif emp_now < emp_PrP:
            increment = Respondent.genList(-1*(salary_PrP-500),0,salary_PrP/5)
            incrementProb = [0.09,0.56,0.25,0.1,0.0]
            salary_now = salary_PrP + numpy.random.choice(increment, p = incrementProb)

        elif emp_now > emp_PrP:
            increment = numpy.random.choice([15000,20000,10000,5000])
            salary_now = salary_PrP + increment

        elif emp_now == 0:
            salary_now = numpy.random.choice([500,1000,1500,2000,2500,3000,3500,4000,45000,4000])

        return int(salary_now)

    def getFamilySize(self,salary_PrP):
        import numpy
        possibleFamilySize = [2, 3, 4, 5, 6]

        if salary_PrP > 31000:
            probabilityValues = [0.1, 0.1, 0.6, 0.1, 0.1]
            famSize = numpy.random.choice(possibleFamilySize, p = probabilityValues)
            return famSize

        elif salary_PrP <= 31000:
            probabilityValues = [0.0,0.1,0.1,0.6,0.2]
            famSize = numpy.random.choice(possibleFamilySize, p = probabilityValues)
            return famSize


    def getNumStudents(self,familySize):
        import random
        import numpy
        ageDependencyRatio = 0.50
        isGreaterthanFamsize = True

        while isGreaterthanFamsize == True:
            incrementChoice = [random.randint(-50,-3)/100,random.randint(-2,2)/100, random.randint(2,5)/100]
            incrementProb = [0.2,0.6,0.2]
            increment = numpy.random.choice(incrementChoice, p = incrementProb)
            numStudents =  int(familySize - (familySize*(ageDependencyRatio + increment)) )


            if familySize-numStudents > 0:
                isGreaterthanFamsize = False
                return numStudents



    def getEmp_PrP(self,familySize, numStudents):
        import numpy
        dif = familySize - numStudents
        if dif <= 1:
            return 1
        else:
            return numpy.random.randint(1,familySize - numStudents)

    def getuEmp_PrP(self,familySize, numStudents,  emp_PrP):
        return familySize - (numStudents + emp_PrP)

    def getEmp_now(self,emp_PrP):
        import numpy
        check = -emp_PrP + 1
        if check == 0:
            prob = [0.65, 0.35]
            return numpy.random.choice([1,0],p = prob)
        else:
            increment =  numpy.random.randint(-emp_PrP+1,0)
            return emp_PrP + increment

    def getuEmp_now(self,emp_PrP, emp_now, uEmp_PrP ):
        increment = emp_PrP - emp_now
        return uEmp_PrP + increment


    def getBudgetAllocation(self,salary_now,region,familySize,numStudents):
        from budgetAllocationGeneration import bAll as bA
        avgbAll = {"food": 0.48, "houseRent": 0.17, "utilities": 0.1,
                   "transport": 0.05, "communication": 0.02,
                   "education": 0.01, "others": 0.01,"savings": 0.01}

        budgetAllocation = {"food": bA.setFood(salary_now,avgbAll["food"]),
                            "houseRent": bA.setHouse(salary_now,region,avgbAll["houseRent"]),
                            "utilities": bA.setUtilities(salary_now,familySize,avgbAll["utilities"]),
                            "transport": bA.setTransport(region,avgbAll["transport"]),
                            "communication":  bA.setCommunication(salary_now,avgbAll["communication"]),
                            "education": bA.setEducation(salary_now,numStudents,avgbAll["education"]),
                            "others": bA.setOthers(salary_now,avgbAll["others"]),
                            "savings": bA.setSavings(avgbAll["savings"])}

        preLimAllocation = 0
        for key in budgetAllocation.keys():
            try:
                preLimAllocation += budgetAllocation[key]
            except TypeError:
                preLimAllocation = 0

        #evaluate if prelimAllocation is greater or less than 1
        #it must equal to 1

        # this is a check as to how the preLimAllocation deviates from 1
        n = 1 - preLimAllocation


        if n != 0:
            #this means that preLimAllocation is larger than 1
            toDistribute = n/8
            for key in budgetAllocation.keys():
                try:
                    budgetAllocation[key] = budgetAllocation[key] + toDistribute
                except TypeError:
                    budgetAllocation["communication"] = 0.01

            return budgetAllocation

        else:
            return budgetAllocation
