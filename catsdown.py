import random as r
import time, os

def intro():
	print "Welcome to catsdown!\nIt's a ripoff of Countdown."
	print "Well, just the numbers game."
	print "\n\n\nWe have 24 numbers. 'Small' and 'large' numbers."
	print "\n2 each small number, 1-10"
	print "1 of each large number; 25, 50, 75, and 100\n"
	print "\nYou'll get 6 total numbers."
	print "At least one of those numbers must be large."
	print "You'll use these, along with basic arithmetic"
	print "to try to get to a random three-digit number."

def first_ask():
	first = raw_input("How many small numbers?\n")
	valid_answer = check_answer(first)
	return valid_answer

def check_answer(answer):
	checked = check_number(answer)
	while type(checked) is not list:
		checked = check_number(checked)
	return checked

def check_number(num):
	try:
		small = int(num)
		if 2 <= small < 6:
			large = 6 - small
			how_many = [small, large]
			print "\n\n\nPerfect.\n%d small, and %d large it will be!" % (small, large)
			print "Press ENTER when you're ready! Or CTRL + C to be a quitter."
			raw_input()
			return how_many
	except:
		small = raw_input("That's not a number, 2-5.\nTry again: ")
		return small

def get_target():
	target = r.randint(100,1000)
	return target

def game_list(f):
	game_list = r.sample(smalls, f[0]) + r.sample(bigs, f[1])
	return game_list

def clear_command():
	return os.system('cls' if os.name == 'nt' else 'clear')

def start_game():
	answer = first_ask()
	numbers = game_list(answer)
	stringy_list = " | ".join(map(str, numbers))
	target = get_target()
	clear_command()

	print "Target: %d\n\nList: %s" % (target, stringy_list)
	time.sleep(32.5)
	print "\n\n\nThat's 30 seconds."
	print "That's all they give you on the show."
	print "You can keep playing as long as you want though."
	print "\n\n\nWhen you're ready for new numbers, press ENTER."
	print "Or CTRL + C to make me go away."




# tiles: 2 of each 1-10
#        1 of each 25, 50, 75, 100
smalls = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
bigs = [25,50,75,100]


intro()
start_game()





