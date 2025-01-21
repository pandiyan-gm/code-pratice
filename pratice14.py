#Question 14: this program checks whether the given year is leap or not

def is_leap(year):
    leap=False

    if(year%4==0):        #If a year divided by 4 it is a leap year as well as for centurian years it must divided on both 100 and 400 
        if(year%100==0):
            if(year%400==0):
                leap=True
            else:
                leap=False
        else:
            leap=True
    else:
        leap=False
    return leap

year=int(input("Enter a year: "))
if is_leap(year):
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")
