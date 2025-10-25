def timeconvertion(time):
  hour = time[0]
  minute = time[1]
  notation = time[2]
  if(notation == "am" and hour==12):
    hour = 0
  elif(notation=="pm" and hour != 12):
    hour += 12
  return (f"{hour}:{minute}")



s1 = "10:17"
s2 = "10:17"

# Convert strings to hours and minutes
ss1 = list(map(int, s1.split(":")))
ss2 = list(map(int, s2.split(":")))

# ss1 = timeconvertion(ss1)
# ss2 = timeconvertion(ss2)

# Compute total minutes for each time
time1 = ss1[0] * 60 + ss1[1]  # Convert to total minutes
time2 = ss2[0] * 60 + ss2[1]  # Convert to total minutes

# Calculate the difference in minutes
diff = abs(time2 - time1)

# Convert back to hours and minutes
hours = diff // 60
minutes = diff % 60

# Display the result
print(f"{hours:02}:{minutes:02}")