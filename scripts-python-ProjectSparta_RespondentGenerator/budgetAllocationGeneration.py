class bAll(object):

    @staticmethod
    def inverseLerp(v,c):
        #v is a tuple, c is a value b/w v[0](init value) to v[1](final value)
        percentage = round((c - v[0])/(v[1]-v[0]), 2)
        return percentage

    @staticmethod
    def setFood(salary,avgAllocation):
        import numpy
        #change the processes with lerp
        
        if salary >= 31000:
            part = bAll.inverseLerp((31000,150000), salary)
            increment = part * bAll.inverseLerp((0, 5), part)*-1
            if abs(increment) > 0.08:
                increment = (increment - numpy.random.randint(increment*100 - 7, increment*100 - 3)/100) * -1
        else:
            part =bAll.inverseLerp((3500,31000),salary)
            increment = part * bAll.inverseLerp((0,5),part)
            if increment > 0.08:
                increment = increment - numpy.random.randint(increment*100 - 5, increment*100 - 3)/100

        allocation = avgAllocation + round(increment,2)
        return round(allocation,2)

    @staticmethod
    def setUtilities(salary,familySize,avgAllocation):
        import numpy
        familyData = [{"familyRange": [i for i in range(2,4,1)],
                       "incrementValues": numpy.random.randint(-1/8,1)/100},
                      {"familyRange": [i for i in range(4,7,1)],
                       "incrementValues": numpy.random.randint(1/4,1)/100}]

        if salary >= 31000:
            part =bAll.inverseLerp((3500,31000),salary)
            salaryIncrement = part * bAll.inverseLerp((0,5),part)
            if salaryIncrement > 0.02:
                salaryIncrement  = (salaryIncrement - numpy.random.randint(salaryIncrement*100 - 3,
                                                                          salaryIncrement*100 - 1)/100)
        elif salary < 31000:
            part =bAll.inverseLerp((3500,31000),salary)
            salaryIncrement = part * bAll.inverseLerp((0,5),part)*-1
            if abs(salaryIncrement) > 0.02:
                salaryIncrement  = (salaryIncrement - numpy.random.randint(salaryIncrement*100 - 3,
                                                                          salaryIncrement*100 - 1)/100)*-1
        for item in familyData:
            if familySize in item["familyRange"]:
                familyIncrement = item["incrementValues"]


        allocation = avgAllocation + (salaryIncrement + familyIncrement)
        return round(allocation,2)
    
    @staticmethod
    def setHouse(salary,region,avgAllocation):
        import numpy

        regionData = [{"regionRange":['Region V - Bicol Region','CAR - Cordillera Administrative Region',
                                      'Region I - Ilocos Region'], "incrementValues": numpy.random.randint(-6,2)/100},
                      {"regionRange":['NCR - National Capital Region', 'Region III - Central Luzon',
                                      'Region VII - Central Visayas','Region IVA - CALABARZON'],
                       "incrementValues": numpy.random.randint(-2,6)/100}]

        if salary >= 31000:
            part = bAll.inverseLerp((31000,150000), salary)
            salaryIncrement = part * bAll.inverseLerp((0,5),part)
            if salaryIncrement > 0.03:
                salaryIncrement  = salaryIncrement - numpy.random.randint(salaryIncrement*100 - 5,
                                                                          salaryIncrement*100 - 3)/100
        else:
            part =bAll.inverseLerp((3500,31000),salary)
            salaryIncrement = part * bAll.inverseLerp((0,5),part)*-1
            if abs(salaryIncrement) > 0.03:
                salaryIncrement  = (salaryIncrement - numpy.random.randint(salaryIncrement*100 - 5,
                                                                           salaryIncrement*100 - 3)/100)*-1
        for item in regionData:
            if region in item["regionRange"]:
                regionIncrement = item["incrementValues"]


        allocation = avgAllocation + (salaryIncrement + regionIncrement)
        return round(allocation,2)

    @staticmethod
    def setTransport(region,avgAllocation):
        import numpy
        regionData = [{"regionRange":['Region V - Bicol Region','CAR - Cordillera Administrative Region',
                                      'Region I - Ilocos Region'],
                       "incrementValues": numpy.random.randint(-1/4,1)/100},
                      {"regionRange":['NCR - National Capital Region', 'Region III - Central Luzon',
                                      'Region VII - Central Visayas','Region IVA - CALABARZON'],
                       "incrementValues": numpy.random.randint(1/4,1)/100}]

        for item in regionData:
            if region in item["regionRange"]:
                regionIncrement = item["incrementValues"]

        allocation = avgAllocation + regionIncrement
        return round(allocation,2)

    @staticmethod
    def setCommunication(salary,avgAllocation):
        import numpy
        if salary >= 31000:
            part = bAll.inverseLerp((31000,150000), salary)
            increment = part * bAll.inverseLerp((0,8),part)
            if increment > 0.08:
                increment = (increment - numpy.random.randint(increment*100 - 7, increment*100 - 3)/100)
        else:
            part =bAll.inverseLerp((3500,31000),salary)
            increment = part * bAll.inverseLerp((0,8),part)*-1
            if abs(increment) > 0.08:
                increment = (increment - numpy.random.randint(increment*100 - 5, increment*100 - 3)/100)*-1

            allocation = avgAllocation + round(increment,2)
            return round(allocation,2)

    @staticmethod
    def setEducation(salary,numStudents,avgAllocation):
        import numpy
        if salary >= 31000:
            part = bAll.inverseLerp((31000,150000), salary)
            salaryIncrement = part * bAll.inverseLerp((0,8),part)
            if salaryIncrement > 0.08:
                salaryIncrement = (salaryIncrement - numpy.random.randint(salaryIncrement*100 - 7, salaryIncrement*100 - 3)/100)
        else:
            part = bAll.inverseLerp((3500,31000),salary)
            salaryIncrement = part * bAll.inverseLerp((0,8),part)*-1
            if abs(salaryIncrement) > 0.08:
                salaryIncrement  = (salaryIncrement - numpy.random.randint(salaryIncrement*100 - 5, salaryIncrement*100 - 3)/100)*-1

        if numStudents <= 2:
            studentIncrement = numpy.random.randint(1,2)/100*-1
        else:
            increments_prob = ([0,0.01,0.02],[0.75,0.13,0.12])
            studentIncrement = numpy.random.choice(increments_prob[0],p = increments_prob[1])
        
        allocation = avgAllocation + (salaryIncrement + studentIncrement)
        return round(allocation,2)

    @staticmethod
    def setSavings(avgAllocation):
        import numpy
        
        increments_prob = [(0.0,numpy.random.randint(-3,3)/100),(0.75,0.25)]
        allocation = avgAllocation + numpy.random.choice(increments_prob[0], p = increments_prob[1])
        
        return round(allocation,2)

    @staticmethod
    def setOthers(salary,avgAllocation):
        import numpy
        if salary >= 31000:
            part = bAll.inverseLerp((31000,150000), salary)
            salaryIncrement = part * bAll.inverseLerp((0,8),part)
            if salaryIncrement > 0.08:
                pass
            salaryIncrement = (salaryIncrement - numpy.random.randint(salaryIncrement*100 - 7, salaryIncrement*100 - 3)/100)
        else:
            part = bAll.inverseLerp((3500,31000),salary)
            salaryIncrement = part * bAll.inverseLerp((0,8),part)
            if salaryIncrement > 0.08:
                salaryIncrement  = (salaryIncrement - numpy.random.randint(salaryIncrement*100 - 5, salaryIncrement*100 - 3)/100)*-1
            
        allocation = avgAllocation + salaryIncrement
        return round(allocation,2)