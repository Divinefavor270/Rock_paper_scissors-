# import random module
import random
 



# Print instructions

# perform progression of string
print("Winning Rules of the Rock paper scissor game as follows: \n"
+"Rock vs paper->paper wins \n"
+ "Rock vs scissor->Rock wins \n"
+"paper vs scissor->scissor wins \n")

while True:
	print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
	
	# get user input 
	outcome = int(input("User turn: "))

	# if any one of the condition is true
	# let it return a positive value	
	# loop until user enters a valid input
	while outcome> 3 or outcome < 1:
		outcome = int(input("enter valid input: "))
		

	# boot value of outcome_name variable
	# let it equate the outcome value
	if outcome == 1:
		outcome_name = 'Rock'
	if outcome == 2:
		outcome_name = 'paper'
	else:
		outcome_name = 'scissor'
		
	# declare user outcome
	print("user choice is: " + outcome_name)
	print("\nNow its computer turn.......")

	# Computer chooses randomly any number btw 1,2,3.
	# randit method of random module
	comptender = random.randint(1, 3)
	
	# looping until comp_tender value
	# is equal to the outcome value
	while comptender == outcome:
		comptender = random.randint(1, 3)

	# initialize value of comp_tender_name
	# variable corresponding to the outcome value
	if comptender == 1:
		comptender_name = 'Rock'
	if comptender == 2:
		comp_tender_name = 'paper'
	else:
		comptender_name = 'scissor'
		
	print("Computer choice is: " + comptender_name)

	print(outcome_name + " V/s " + comptender_name)

	# stakes for winning
	if((outcome == 1 and comptender == 2) or
	(outcome == 2 and comptender ==1 )):
		print("paper wins => ", end = "")
		result = "paper"
		
	if((outcome == 1 and comptender == 3) or
		(outcome == 3 and comptender == 1)):
		print("Rock wins =>", end = "")
		result = "Rock"
	else:
		print("scissor wins =>", end = "")
		result = "scissor"

	# Print
    #  either user or computer wins
	if result == outcome_name:
		print("<== User wins ==>")
	else:
		print("<== Computer wins ==>")
		
	print("how would you like a rematch? (YEA/NAH)")
	ans = input()


	# if user input n or N then condition is True
	if ans == 'n' or ans == 'N':
		break
	
# outta the loop????
#  print thanks for playing
print("\nThanks for playing")
