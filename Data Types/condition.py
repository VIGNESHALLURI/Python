def check_time_day():
     time = int(input("enter the time (0 to 23): "))
     if 6 <=  time <=12:
       return "it is day time"
     else:
       return "it is not day time"
print(check_time_day())
