"""
File: hush.py
------------------
Simple command-line password manager. See README.md for getting started 
and how to use the program. Arguments:
$ python3 hush.py 
	prints database 
$ python3 hush.py a
	for adding an entry to the db. Sets up an interpreter where you
	can type/paste the information for each field in the db. 
$ python3 hush.py s <query (str)> 
	search for an entry and it will print it out. Search scans each field
	for a exact query match. 
$ python3 hush.py show
	same functionality as python3 hush.py 
$ python3 hush.py l 
	prints the total number of entries in the db 
$ python3 hush.py d <query (int)>
	deletes the entry at index <query (int)> in the db. 
"""

import sys 
import pdb
import pandas as pd


# init global vars 
PASSWORDS_FILE_PATH = "passwords.csv"
DATABASE = pd.read_csv(PASSWORDS_FILE_PATH)



def length():
	"""
	Returns the number of passwords stored in the database. 
	"""
	return len(DATABASE)



def add():
	"""
	Function that appends a new password item
    to the passwords file. Each entry consists of the following
    five items: 
    1. Name of the service 
    2. Email 
    3. Username
    4. Password
    5. (Optional) Notes
	"""
	new_row = []
	for i in range(5):
		if i == 0:
			input_description = "Name of service: "
		elif i == 1:
			input_description = "Email: "
		elif i == 2:
			input_description = "Username: "
		elif i == 3:
			input_description = "Password: "
		elif i == 4:
			input_description = "(Optional) Notes: "

		user_input = input(input_description)

		if user_input is None:
			user_input = "No input"

		new_row.append(user_input)

	
	# append the row to pandas DATABASE 
	DATABASE.loc[len(DATABASE)] = new_row


	# print
	print(f"New entry added at index {length() - 1}.")

	# save 
	save()



def show():
	"""
	Function that prints out all the passwords in the list. 
	"""
	print(DATABASE)



def search(query):
	"""
	Function that searches the list for the query. Looks 
	for exact match in the list. If query is not found, 
	it prints nothing.   
	"""
	print("not implemented yet.")
	pass



def delete(idx):
	"""
	deletes an entry from the database specified at index. 
	Index starts at 0. 
	"""
	assert (idx < length() - 1) and (idx >= 0), "specified index must be in bounds"
	DATABASE.drop(idx, inplace=True)
	DATABASE.reset_index(inplace=True)

	save()



def save():
	"""
	helper function to assist in serialization. Saves the contents 
	of new_database to PASSWORDS_FILE_PATH. 
	""" 
	DATABASE.to_csv(PASSWORDS_FILE_PATH, index=False) 



# ----------------------- (main() runner) ----------------------------------


def main():
	user_arguments = sys.argv[1:]
	arg_count = len(user_arguments)  # num user arguments 

	# print out list if no argument was specified 
	if arg_count == 0:
		show()  # show the list 
		sys.exit() 

	# add item to list if 'add' argument is specified 
	if (user_arguments[0] == "add" or user_arguments[0] == "a"):
		add()
		sys.exit()
	
	# search the list with given argument as query if 'search' argument is specified
	if (user_arguments[0] == "search" or user_arguments[0] == "s") and arg_count > 1:
		search(' '.join(user_arguments[1:]))

	# print out list if 'show' argument is specified
	if user_arguments[0] == "show":
		show()
	
	# print out num items in list if 'len' argument is specified
	if user_arguments[0] == "len" or user_arguments[0] == "l":
		print("Number of items:", length())

	# complete (delete) specific item from list 
	if (user_arguments[0] == "delete" or user_arguments[0] == "d") and arg_count == 2:
		specified_idx = int(user_arguments[1]) 
		delete(specified_idx)
	elif (user_arguments[0] == "delete" or user_arguments[0] == "d") and (arg_count < 2 or arg_count > 2):
		user_len_args = 0 
		if len(user_arguments) == 1:
			user_len_args = 0
		else:
			user_len_args = len(user_arguments[1:]) 

		raise ValueError(f"For deleting, must provide exactly one additional CLI argument on top of 'd'/'delete'. You provided {user_len_args} additional arguments")



if __name__ == '__main__':
    main()
