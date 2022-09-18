'''10. Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)'''

day=int(input("enter day"))
month=int(input("Enter the value of month"))
year=int(input("enter the value of year"))
print(day,month,year,sep="-")
a,b=int(input("enter hour")),(input("enter minutes"))
print(a,":",b,"pm")
