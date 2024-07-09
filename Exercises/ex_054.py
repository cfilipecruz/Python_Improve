import time

belowAge = 0
aboveAge = 0
year = time.localtime().tm_year

for c in range(1, 8):
    yearsArray = int(input("In which year did you born?"))
    age = year - yearsArray
    if age >= 18:
        aboveAge += 1
    else:
        belowAge += 1


print("There is {} people underage".format(belowAge))
print("There is {} people above age".format(aboveAge))
