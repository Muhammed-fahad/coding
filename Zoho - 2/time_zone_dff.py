def convert_to_minutes(time_str):
    parts = time_str.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    am_pm = parts[2].upper()

    if am_pm == "PM" and hours != 12:
        hours += 12
    elif am_pm == "AM" and hours == 12:
        hours = 0

    return hours * 60 + minutes


def convert_to_time_str(total_minutes):
    total_minutes %= (24 * 60) 
    hours = total_minutes // 60
    minutes = total_minutes % 60

    am_pm = "AM"
    if hours >= 12:
        am_pm = "PM"
    if hours > 12:
        hours -= 12
    if hours == 0:
        hours = 12

    return f"{hours:02d}:{minutes:02d}:{am_pm}"


# Input
time_str = input("Enter the time (hh:mm:AM/PM): ")
diff_str = input("Enter the difference time (hh:mm): ")
ahedOrAfter = input("Enter if ahead or after (+ or -): ")

# Convert to minutes
time_minutes = convert_to_minutes(time_str)
diff_parts = diff_str.split(":")
diff_minutes = int(diff_parts[0]) * 60 + int(diff_parts[1])

# Perform calculation
if ahedOrAfter == "+":
    new_time_minutes = time_minutes + diff_minutes
else:
    new_time_minutes = time_minutes - diff_minutes

# Output
print("New time:", convert_to_time_str(new_time_minutes))
