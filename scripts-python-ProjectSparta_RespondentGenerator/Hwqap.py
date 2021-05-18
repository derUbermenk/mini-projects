from classRespondent import Respondent as Re



i = 0
while i < 200:
    reg = Re.getRegion()
    sal = Re.getSalary_PrP(reg)
    print(reg,": ",sal)
