# Assignment - 2
# Name - Shivam Gupta
# Roll No - 2020406

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''
	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):
	'''
	Description: Searches the records to find all persons with the given first name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	fn = []
	for i in range(len(records)):
		if records[i]['last_name'].lower() == first_name.lower():
			fn.append(records[i]['id'])
		
	return fn
			
		
def filter_by_last_name(records, last_name):
	'''
	Description: Searches the records to find all persons with the given last name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	ln = []
	for i in range(len(records)):
		if records[i]['last_name'].lower() == last_name.lower():
			ln.append(records[i]['id'])
		
	return ln



def filter_by_full_name(records, full_name):
	'''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	ffl = []
	fn = full_name[0]
	ln = full_name[1]
	for i in range(len(records)):
		if records[i]['first_name'].lower()==fn.lower() and records[i]['last_name'].lower()==ln.lower():
			ffl.append(records[i]['id'])
		
	return ffl


def filter_by_age_range(records, min_age, max_age):
	'''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''

	agei = []
	for i in range(len(records)):	
		if min_age<=records[i]['age'] <=max_age and 0 < min_age<=max_age:
			agei.append(records[i]['id'])
	return agei

	


def count_by_gender(records):
	'''
	Description: Counts the number of males and females

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
	'''
	gender=["male","female"]
	mcount=0
	fcount=0
	for i in range(len(records)):
		if records[i]['gender']=="male":
			mcount+=1
		if records[i]['gender']=="female":
			fcount+=1
	
	final_count=[mcount, fcount]
	bge = dict (zip(gender,final_count))
	return bge

	
			


def filter_by_address(records, address):
	'''
	Description: Filters the person records whose address matches the given address. 

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
		Some examples are:
			Case 1: {} 
				=> All records match this case
			
			Case 2: { "block": "AD", "city": "Delhi" } 
				=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
			
			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
	'''
	f = []; keys_f = []
	for keys in address.keys():
		keys_f.append(keys)
	for i in records:
		dic = {}
		if address == {}:
			dic.update({'first_name': i['first_name']})
			dic.update({'last_name' : i['last_name']})
			f.append(dic)
		else:
			flag = True
			for j in keys_f:
				if str(i['address'][j]).lower() == str(address[j]).lower():
					continue
				else:
					flag = False
					break
			if flag:
				dic.update({'first_name':i['first_name']})
				dic.update({'last_name':i['last_name']})
				f.append(dic)
	return f

def find_alumni(records, institute_name):
	'''
	Description: Find all the alumni of the given institute name (case-insensitive). 
	
	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)

	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
	'''

	alum_lst= []
	for i in range(len(records)):
		for entries in records[i]['education']:
			if entries['ongoing'] == False and entries['institute'].lower() == institute_name.lower():
				alum_lst.append({'first_name': records[i]['first_name'], 'last_name': records[i]['last_name'], 'percentage': entries['percentage']})

	return alum_lst


def find_topper_of_each_institute(records):
	'''
	Description: Find topper of each institute

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	'''


	dicts_top = {}
	institutes = []
	for x in records:
		for y in x['education']:
			institutes.append(y['institute'])

	institutes = list(set(institutes))
	id = -1
	for names in institutes:
		max = -1.0
		for entries in records:
			for edu in entries['education']:
				if edu['institute'] == names and edu['ongoing'] == False:
					if max < edu['percentage']:
						max = edu['percentage']
						id = entries['id']
		if id != -1 and max !=-1:
			dicts_top[names] = id

	return dicts_top

	
def find_blood_donors(records, receiver_person_id):
	'''
	Description: Find all donors who can donate blood to the person with the given receiver ID.

		Note: 
		- Possible blood groups are "A", "B", "AB" and "O".

		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
	'''
	bg = 'na'
	donors={}
	for i in range(len(records)):
		if records[i]['id']==receiver_person_id:
			bg = records[i]['blood_group']
	
	for i in range(len(records)):
		if bg =="A" or (records[i]['blood_group'] == 'A' or records[i]['blood_group'] == 'O'):
			donors[ records[i]['id'] ] = records[i]['contacts']

		elif bg == 'B' and (records[i]['blood_group'] == 'B' or records[i]['blood_group'] == 'O'):
			donors[records[i]['id']] = records[i]['contacts']

		elif bg == 'AB':
			donors[records[i]['id']] = records[i]['contacts']

		elif bg =='O' and records[i]['blood_group'] == 'O':
			donors[records[i]['id']] = records[i]['contacts']
	
	for i in records:
		if i['id'] == receiver_person_id:
			del donors[receiver_person_id]

	return donors
			


def get_common_friends(records, list_of_ids):
	'''
	Description: Find the common friends of all the people with the given IDs

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
	'''
	com_f=[] ; lst = [] ; list_of_ids = list(set(list_of_ids))

	for i in (records):
		if i['id'] in list_of_ids:
			lst.extend(i['friend_ids'])
	
	for n in lst:
		if lst.count(n) == len(list_of_ids):
			com_f.append(n)
	com_f = list(set(com_f))

	return com_f

			


def is_related(records, person_id_1, person_id_2):
	'''
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID

	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
	'''
	



def delete_by_id(records, person_id):
	'''
	Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	f123 = []
	for i in range(len(records)):
		if records[i]['id']==person_id:
			f123 = records[i]['friend_ids']
			records.remove(records[i])
		
	if len(f123) != 0:
		for i in records:
			for f234 in f123:
				if i['id'] == f234:
					i['friends_ids'].remove(person_id)
	
	return records

def add_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''

	for i in range(len(records)):
		if person_id == (records[i])['id'] and not(friend_id in (records[i])['friend_ids']):
			(records[i])['friend_ids'].append(friend_id)
		if friend_id == (records[i])['id'] and not(person_id in (records[i])['friend_ids']):
			(records[i])['friend_ids'].append(person_id)
	return records



def remove_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''

	for i in range(len(records)):
		if person_id == (records[i])['id'] and (friend_id in (records[i])['friend_ids']):
			(records[i])['friend_ids'].remove(friend_id)
		if friend_id == (records[i])['id'] and (person_id in (records[i])['friend_ids']):
			(records[i])['friend_ids'].remove(person_id)
	return records


def add_education(records, person_id, institute_name, ongoing, percentage):
	'''
	Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	for i in range(len(records)):
		if person_id == records[i]['id']:
			if ongoing:
				records[i]['education'].append({'institute': institute_name.upper(), 'ongoing': ongoing})
			else:
				records[i]['education'].append({'institute': institute_name.upper(), 'ongoing': ongoing, 'percentage': percentage})

	return records


