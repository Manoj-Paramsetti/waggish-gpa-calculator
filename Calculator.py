print("""
  ____ ____   _       ____      _            _       _
 / ___|  _ \ / \     / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __
| |  _| |_) / _ \   | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |_| |  __/ ___ \  | |__| (_| | | (__| |_| | | (_| | || (_) | |
 \____|_| /_/   \_\  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
""")
try:
	nos = int(input("Hey! How many subjects you have for this semester?\n"))
	print()
	marks = []
	credits = []
	sum_credits=0
	sum_marks=0
	print("Now Tell your marks 😜 \n")
	for i in range(0,nos):
		marks.append(int(input("subject {} mark? ".format(i+1)))/10)
		credit = int(input("What is the credit for that? "))
		print()
		marks[i] = marks[i] * credit
		credits.append(credit)
	for k in marks:
		sum_marks += k
	for j in credits:
		sum_credits += j
	gpa = sum_marks/sum_credits
	print("\n\nHey! I calculated your gpa 😆")
	input("Press enter to release 🙃\n\n")

	if(gpa<=10 and gpa >= 9):
		print("Hey! you got {} GPA 💥".format(gpa))
		print("Plan for a treat 🥂")
	elif(gpa < 9.0 and gpa >=8):
		print("Wow! man you got {} GPA".format(gpa))
		print("Next time aim for 9+ GPA then we will have big party ah 😜")
	elif(gpa < 8.0 and gpa >= 7):
		print("Wow! you got decent GPA. That is {} GPA ☺️ ".format(gpa))
		print("What is your next plan? 🤪")
	else:
		print("I guess you should concentrate on studies more than games 😂")
		print("You got {} GPA".format(gpa))
		print("plan for a sitting 🍺")
except:
	print("\nCalculator closed suddenly 😑")
