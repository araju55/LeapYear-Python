def isLeapYear(year):
    return(year%4 == 0 and (year%100!=0 or year%400==0))

y = int(input("Enter a year: "))
isOrNot = isLeapYear(y)
print(isOrNot)
