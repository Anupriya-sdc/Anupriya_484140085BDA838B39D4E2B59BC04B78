def isLeapyear(year):
  if(year % 4 == 0 & year % 100 !=0)/year % 400 ==0:
    return True
  else:
    return False
year=int(input("enter the year"))
if isLeapyear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))