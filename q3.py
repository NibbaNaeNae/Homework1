totalMark = 0

for x in range(5):
    userInput = int(input("What mark did you get? "))
    totalMark = totalMark + userInput

average = str(totalMark/5)


print("Answer is " + average + "/8")
