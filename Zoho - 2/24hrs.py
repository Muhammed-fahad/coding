def time_conversion(time):
    time_parts = time[:-2].split(":")
    hour = int(time_parts[0])
    minute = int(time_parts[1])
    period = time[-2:].lower()
    
    if period == "am":
        if hour == 12:
            hour = 0 
    elif period == "pm":
        if hour != 12:
            hour += 12
    return f"{hour:02}:{minute:02}"

def time_convertion_24_12(time):
    values = time.split(":")
    hour = int(values[0])
    minutes = int(values[1])
    if hour > 12 :
        delimeter = "pm"
        hour-=12
    else:
        delimeter = "am"
    return(f"{hour:02}:{minutes:02}:{delimeter}")
        
    

time12 = input("Enter time in 12-hour format (hh:mmAM/PM): ")
print(time_conversion(time12))


time24 = input("Enter time in 24-hour format (hh:mm): ")
print(time_convertion_24_12(time24))
