# Name - Shivam Gupta
# Roll No - 2020406

import a2

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''


def read_data():
	return a2.read_data_from_file()


def filter_by_firstname():
	first_name = input('Enter the first name: ')
	return a2.filter_by_first_name(records, first_name)


def filter_by_lastname():
	last_name = input('Enter the last name: ')
	return a2.filter_by_last_name(records, last_name)


def filter_by_fullname():
	full_name = input('Enter the full name: ')
	return a2.filter_by_full_name(records, full_name)


def filter_by_age():
	min_age = int(input('Enter the lower limit of age: '))
	max_age = int(input("Enter the upper limit og age: "))
	return a2.filter_by_age_range(records, min_age, max_age)


def count_gender():
	return a2.count_by_gender(records)


def filter_using_address():
	address = {"house_no": -100, "block": "", "town": "", "city": "", "state": "", "pincode": -100}
	print('------------------------------')
	print("        INPUT ADDRESS")
	print('------------------------------')
	house_no = int(input("Enter the House Number: "))
	if house_no != '':
		address["house_no"] = house_no
	block = input("Enter the House Number: ")
	if block != '':
		address["block"] = block
	town = input("Enter the town: ")
	if town != '':
		address["town"] = town
	city = input("Enter the city: ")
	if city != '':
		address["city"] = city
	state = input("Enter the state: ")
	if state != '':
		address["state"] = state
	pincode = int(input("Enter the pincode"))
	if pincode != '':
		address["pincode"] = pincode
	return a2.filter_by_address(records, address)


def alumni():
	institute_name = input('Enter Institute Name:')
	return a2.find_alumni(records, institute_name)


def topper_of_each_institute():
	return a2.find_topper_of_each_institute(records)


def find_donors():
	receiver_id = int(input("Enter receiver person's id: "))
	return a2.find_blood_donors(records, receiver_id)


def find_common_friends():
	list_of_ids = [x for x in input("Enter multiple ids to find common friends (space-seperated): ").split()]
	return a2.get_common_friends(records, list_of_ids)


def related():
	person1 = int(input('Enter ID 1: '))
	person2 = int(input('Enter ID 2: '))
	return a2.is_related(records, person1, person2)


def delete_id():
	person_id = int(input("Enter ID to be deleted: "))
	return a2.delete_by_id(records, person_id)


def add_friends():
	person_id = int(input('Enter ID of person: '))
	friend_id = int(input('Enter ID of friend to be added: '))
	return a2.add_friend(records, person_id, friend_id)


def remove_friends():
	person_id = int(input('Enter ID of person: '))
	friend_id = int(input('Enter ID of friend to be removed: '))
	return a2.remove_friend(records, person_id, friend_id)


def add_an_education():
	person_id = int(input("Enter person ID: "))
	institute_name = input('Enter name of the institute: ')
	ongoing_status = input("ENTER ONGOING STATUS (True/False): ")
	while True:
		ongoing_status = input("ENTER ONGOING STATUS (True/False): ")
		if ongoing_status.upper() == 'TRUE':
			ongoing_status = True
			return a2.add_education(records, person_id, institute_name, ongoing_status, 0)
		elif ongoing_status.upper() == 'FALSE':
			percentage = float(input("ENTER PERCENTAGE: "))
			ongoing_status = False
			return a2.add_education(records, person_id, institute_name, ongoing_status, percentage)

def menu():
	print("""
********************************************
	   WELCOME USER
********************************************
Hello and welcome to my directory! You can choose from the following options:
____________________________________________
CODE |         OPTIONS                   
--------------------------------------------
  1  | read_data_from_file        
  2  | Filter By First Name              
  3  | Filter By Last Name               
  4  | Filter By Full Name
  5  | Filter By Age Range
  6  | Count By Gender
  7  | Filter By Address
  8  | Find Alumni of an Institute
  9  | Find Topper Of Each Institute
  10 | Find Compatible Blood Donors
  11 | Get Common Friends
  12 | Is Related
  13 | Delete Record By ID
  14 | Add a Friend
  15 | Remove a Friend
  16 | Add Passing Institute
------------------------------------------------
FEW INSTRUCTIONS
------------------------------------------------
1) FOR FIRST TIME ENTER 1 IN CHOICE
2) TO EXIT ENTER "-1" IN CHOICE  """)


	global records
	code = 0
	while code != -1:
		code = int(input("Enter Code from the options above: "))
		if code == 1:
			records = read_data()
		elif code == 2:
			print(filter_by_firstname())
		elif code == 3:
			print(filter_by_lastname())
		elif code == 4:
			print(filter_by_fullname())
		elif code == 5:
			print(filter_by_age())
		elif code == 6:
			print(count_gender())
		elif code == 7:
			print(filter_using_address())
		elif code == 11:
			print(find_common_friends())
		elif code == 12:
			print(related())
		elif code == 13:
			records = delete_id()
			print(records)
		elif code == 14:
			records = add_friends()
			print(records)
		elif code == 15:
			records = remove_friends()
			print(records)
		elif code == 16:
			records = add_an_education()
			print(records)
		elif code == -1:
			break
		elif code == 8:
			print(alumni())
		elif code == 9:
			print(topper_of_each_institute())
		elif code == 10:
			print(find_donors())
		else:
			print("You seem to have entered an invalid code")

	print(""" ---------
	THANK YOU FOR USING MY SERVICE
	---------""")


records = []
menu()