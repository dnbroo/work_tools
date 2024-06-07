# Name: Devon Brewer
version = 0.2
# Creation Date: 08/25/2023
# Desc: A program to help find information fast on OneRoster 1.3 and SFF files.
#
#
# Projected Program Map:
#		- Find files and set working directory for the project
#		- If no files found end program
#		- determine if files are for Oneroster or SFF
#		- search user csv to find user
#		- Determine if user is teacher or student
#
#		- If Student: 
#			- search class enrollments csv and add class sourcedid to array
#			- search class csv for class sourcedid in array and get class info
#			- search class enrollments csv to get teacher
#			- searches user csv to get teacher info
#			- prints out teacher info along with class info for user
#
#		- If Teacher:
#			- search class enrollments csv and add class sourcedid to array
#			- search class csv for class sourcedid in array and get class info
#			- search class enrollments csv to get students
#			- searches user csv to get student info
#			- prints out class info along with students in the classes

# 		cool ideas
#		search all classes associated with a user.
#		search all users associated with a class
#		search all orgs associated with a user/class/etc.
#		determine whether file is SFF or oneroster

import csv
import sys
import glob
import os
import time
import zipfile as zf
import shutil

global debug
global searchTime

debug = True
searchTime = 0

#=============== DICTS ===============
#our user dictionaries to help with getting user data.
orUserDict = {
  "sourcedid":None,
  "status":None,
  "dateLastModified":None,
  "enabledUser":None,
  "orgSourceDid":None,
  "role":None,
  "username":None,
  "userIds":None,
  "givenName":None,
  "familyName":None,
  "middleName":None,
  "identifier":None,
  "email":None,
  "sms":None,
  "phone":None,
  "agentSourcedids":None,
  "grades":None,
  "password":None
}

sffUserDict = {
  "schoolYear":None,
  "role":None,
  "lasid":None,
  "sasid":None,
  "firstName":None,
  "middleName":None,
  "lastName":None,
  "grade":None,
  "username":None,
  "password":None,
  "organizationTypeId":None,
  "orgnizationId":None,
  "primaryEmail":None,
  "hmhApplications":None
}

#=================== FUNCTIONS =====================
def intro():
	clear = lambda: os.system('cls')
	clear()
	print('Welcome to the Roster Helper Version: %.1f!\n\n'% (version))
	print('Please message me with any issues.\n')
	displayRosterHelper()
	return

def menu():
	while True:
		clear = lambda: os.system('cls')
		clear()
		displayRosterHelper()
		print('Loaded: %s' % (path))
		print('Success! Necessary File(s) found! This is a %s import.\n\n' % (fileType))
		print('1) Find a User')
		print('2) Find a Class')
		print('3) Load a New File')
		print('4) Error Lookup')

		selection = input("Please select an option:> ")

		if selection == '1':
			clear = lambda: os.system('cls')
			clear()
			displayRosterHelper()
			findUser()
			break
		if selection == '2':
			clear = lambda: os.system('cls')
			clear()
			displayRosterHelper()
			findClass()
			break
		if selection == '3':
			fileGrabber()
			menu()
			break
		if selection == '4':
			errorHelper()
			break

	return

def fileGrabber():
	#sets to -1 in case it doesn't find anything
	#set to global so that we can use it oustide this function
	global path_userFile
	global path_classFile
	global path_classAssignmentFile
	global path_orgsFile
	global fileType
	global path

	path_userFile = -1
	path_classFile = -1
	path_classAssignmentFile = -1

	#OR is users, classes, enrollments, orgs, 
	#gets path for whole project
	path = input('Drag zip file or un-zipped folder location here and press:\n').strip('"')

	#TODO: check file directoy and check if file then if zip then unzip ============

	#if its a zip, unzip it and open newly created folder. 
	if zf.is_zipfile(path):
		print('is zip')
		# loading the temp.zip and creating a zip object
		with zf.ZipFile(path, 'r') as zObject:
			print('created zip object')

			# Extracting all the members of the zip 
			# into a specific location.
			path = path.rstrip('.zip')

			#attempts to delete conflicting directory. if it fails, creates dir_new
			if os.path.isdir(path):
				print('Removing conflicting folder.')
				try:
					shutil.rmtree(path)
				except:
					print('Failed to delete all necessary files.\nCreating new directory for files.')
					path = path + '_new'


			#creates directory at path
			try:
				print('Creating folder at: %s' % path)
				os.mkdir(path)
			except:
				print('Failed to unzip file. Please remove any existing files and close out of any open files for this directory and try again...')
				input('Press enter to continue...')
				fileGrabber()
				return

			#unzips files into new directory
			zObject.extractall(path)

	#checks file to see if it is bigger than 7 files. (oneroster will have max 8 files.)
	if len(os.listdir(path)) > 10:
		print('\n\n\nFile count larger than 9 (Imports will have MAX 9 files).\nlease check your file/folder and try again...\n\n\n')
		fileGrabber()
		return

	if debug:
		print(os.listdir(path))

	for file in os.listdir(path):
		if file.lower() == 'enrollments.csv':
			fileType = 'OneRoster'
		if file.lower() == 'classassignment.csv':
			fileType = 'SFF'
		if file.lower() == 'classassignments.csv':
			fileType = 'SFF'
		if file == 'CLASSASSIGNMENT.csv':
			fileType = 'SFF'
		if file == 'CLASSASSIGNMENTS.csv':
			fileType = 'SFF'

	print('This seems to be a %s format.\n' % (fileType))


	if fileType == 'SFF':
		print('Checking SFF files...\n')
		for file in os.listdir(path):
			#gets user file
			if file.lower() == 'user.csv':
				path_userFile = path + "\\" + file
			if file.lower() == 'users.csv':
				path_userFile = path + "\\" + file
			if file == 'USER.csv':
				path_userFile = path + "\\" + file
			if file == 'USERS.csv':
				path_userFile = path + "\\" + file

			#gets class file
			if file.lower() == 'class.csv':
				path_classFile = path + "\\" + file
			if file.lower() == 'classes.csv':
				path_classFile = path + "\\" + file
			if file == 'CLASS.csv':
				path_classFile = path + "\\" + file
			if file == 'CLASSES.csv':
				path_classFile = path + "\\" + file

			#gets classAssignment file
			if file.lower() == 'classassignment.csv':
				path_classAssignmentFile = path + "\\" + file
			if file.lower() == 'classassignments.csv':
				path_classAssignmentFile = path + "\\" + file
			if file == 'CLASSASSIGNMENT.csv':
				path_classAssignmentFile = path + "\\" + file
			if file == 'CLASSASSIGNMENTS.csv':
				path_classAssignmentFile = path + "\\" + file

	if fileType == 'OneRoster':
		print('Checking OneRoster files...\n')
		for file in os.listdir(path):
			if file.lower() == 'users.csv':
				path_userFile = path + "\\" + file

			if file.lower() == 'classes.csv':
				path_classFile = path + "\\" + file

			if file.lower() == 'enrollments.csv':
				path_classAssignmentFile = path + "\\" + file

			if file.lower() == 'orgs.csv':
				path_orgsFile = path + "\\" + file


	if path_userFile == -1:
		print('User file not found. Please try again...')
		fileGrabber()
		return

	print('Found User file.\n')

	if path_classFile == -1:
		print('Class file not found. Please try again...')
		fileGrabber()
		return

	print('Found Class file.\n')
		
	if path_classAssignmentFile == -1:
		print('ClassAssignment file not found. Please try again...')
		fileGrabber()
		return

	print('Found Class Assignment file.\n')
	return

def errorHelper():
	clear = lambda: os.system('cls')
	clear()
	displayRosterHelper()

	global path_errorFile

	print('Currently only working for Ed error reports')
	print('Supported Codes: 1296\n\n')
	path = input('Drag error file here:\n').strip('"')

	if path.lower().endswith('.csv'):
		print('Success! Loaded %s Error File!' % (path))
		path_errorFile = path
	else:
		print('\n\nError: This file does not end with .CSV. Please try again...\n\n')
		input('Press Enter to Continue...')
		errorHelper()
		return

	#displaySearchQuestions('error')

	errorList = gatherErrors()
	
	searchErrorSource(errorList)

	print('1) Return to Menu')

	while True:
			selection = input('rosterHelper:> ')

			if selection == '1':
				menu()
				break

	return

def gatherErrors():
	currentCSV = csv.reader(open(path_errorFile, "r"), delimiter=",")
	errorDict = None
	errorList = []

	#skips past first row (headers)
	next(currentCSV)

	print('\nSearching Error file...')
	time.sleep(searchTime)


	#current support error number:
	# 1296 - Value is missing for field(s) used in OneRoster Username formula
	# 1961 - User already exists in the organization you are trying to add them to. Please choose a different username and import again.

	for row in currentCSV:
			if '1296' == row[0].lower():
				errorDict = dict(errorCode = row[0],
											errorMess = row[1],
											lookupCode = row[3].lower(),
											userSourcedid = '')

				errorList.append(errorDict)



	return errorList

def searchErrorSource(errorList):
	#user errors
	currentCSV = csv.reader(open(path_userFile, "r"), delimiter=",")

	next(currentCSV)

	print('\nSearching User file for Errored Users...')
	time.sleep(searchTime)

	index = 1

	if fileType == 'OneRoster':
		for row in currentCSV:
				for error in errorList:
					if error['lookupCode'] == row[0].lower():
						userDict = dict(sourcedid = row[0],
											status = row[1],
											dateLastModified = row[2],
											enabledUser = row[3],
											orgSourceDid = row[4],
											role = row[5],
											username = row[6],
											userIds = row[7],
											givenName = row[8],
											familyName = row[9],
											middleName = row[10],
											identifier = row[11],
											email = row[12],
											sms = row[13],
											phone = row[14],
											agentSourcedids = row[15],
											grades = row[16],
											password = row[17],
											index = index)

						print('============= Error For User Below %d of %d =============' % (errorList.index(error) + 1, len(errorList)))
						printError(error, userDict)
						input('\nPress enter to continue...')

					else:
						index += 1
		print('\n\nAll Errors have been reviewed.\n\n')
	return

def printError(error, userDict):

	
	print('{:<20}  {:<40}'.format('Error Number:', error['errorCode']))
	print('{:<20}  {:<40}'.format('Error Message:', error['errorMess']))
	print('{:<20}  {:<40}'.format('Error Lookup ID:', error['lookupCode']))

	printUserInfo(userDict)

	return

def findUser():
	print('\n\n\n')
	displaySearchQuestions('user')


	#get search term
	searchTerm = input('rosterHelper:> ').strip().lower()

	if searchTerm == '':
		input('Please enter a search term. Press enter to try again...')
		findUser()
		return

	userDict = searchCSVForUser(searchTerm)

	if userDict == None:
		print("No user found.\n\n")

		print('1) Try Again')
		print('2) Return to Menu')

		while True:
			selection = input('rosterHelper:> ')

			if selection == '1':
				findUser()
				break
			elif selection == '2':
				menu()
				break

	else:
		printUserInfo(userDict)

		print('1) Search All Associated Classes')
		print('2) New Search')
		print('3) Return to Menu')

		while True:
			selection = input('rosterHelper:> ')

			if selection == '1':
				findAssociatedClasses(userDict)
				break
			elif selection == '2':
				findUser()
				break
			elif selection == '3':
				menu()
				break


	return

def findAssociatedClasses(userDict):

	classAssociationsList = []

	if fileType == 'OneRoster':
		currentCSV = csv.reader(open(path_classAssignmentFile, "r"), delimiter=",")

		#skips past first row (headers)
		next(currentCSV)

		print('\nSearching Class Assignment file...')
		time.sleep(searchTime)

		for row in currentCSV:
			if userDict["sourcedid"] == row[5]:
				classAssociationsList.append(row[3])


		if len(classAssociationsList) > 0:
			print('Found %d associated class(es).' % len(classAssociationsList))
		else:
			print('No classes found for this user...\n\n\n')
			print('1) Search for a Different User')
			print('2) Return to Menu')

			while True:
				selection = input('rosterHelper:> ')

				if selection == '1':
					findUser()
					break
				elif selection == '2':
					menu()
					break
			return

		print('\nSearching Class File...')

		currentCSV = csv.reader(open(path_classFile, "r"), delimiter=",")

		#skips past first row (headers)
		next(currentCSV)

		for row in currentCSV:
			if row[0] in classAssociationsList:
				classDict = dict(sourcedid = row[0],
								status = row[1],
								dateLastModified = row[2],
								title = row[3],
								grades = row[4],
								courseSourcedid = row[5],
								classCode = row[6],
								classType = row[7],
								location = row[8],
								schoolSourcedid = row[9],
								termSourcedid = row[10],
								subjects = row[11],
								subjectCodes = row[12],
								periods = row[13],
								classAssignmentIndex = classAssociationsList.index(row[0]),
								teacherSourcedid = '',
								teacherUsername = '',
								studentsSourcedid = [],
								studentsUsername = [])

				printClassInfo(classDict, userDict['role'])

	print('1) New Search')
	print('2) Return to Menu')

	while True:
			selection = input('rosterHelper:> ')

			if selection == '1':
				findUser()
				break
			if selection == '2':
				menu()
				break

	return

def findAssociatedTeacher(classDict):

	currentCSV = csv.reader(open(path_classAssignmentFile, "r"), delimiter=",")

	#skips past first row (headers)
	next(currentCSV)

	#opens enrollment file and finds teacher for that classsourcedid
	for row in currentCSV:
		if row[3].lower() == classDict["sourcedid"].lower() and row[6].lower() == 'teacher':
			classDict['teacherSourcedid'] = row[5]

	if classDict['teacherSourcedid'] != '':

		currentCSV = csv.reader(open(path_userFile, "r"), delimiter=",")

		for row in currentCSV:
			if row[0].lower() == classDict['teacherSourcedid'].lower():
				classDict['teacherUsername'] = row[6]
				classDict['teacherEmail'] = row[12]

	return classDict

def findAssociatedStudents(classDict):

	lasidOfStudents = []

	currentCSV = csv.reader(open(path_classAssignmentFile, "r"), delimiter=",")

	#skips past first row (headers)
	next(currentCSV)

	#opens enrollment file and finds teacher for that classsourcedid
	for row in currentCSV:
		#if row[3].lower() == '8bdc8197-ba12-3067-8dc2-2718764ecb68-62468':
			#print(row[3].lower() + ' to ' + classDict["sourcedid"].lower())
			#print(row[3].lower() == classDict["sourcedid"].lower())
		if row[3].lower() == classDict["sourcedid"].lower() and row[6].lower() == 'student':
			lasidOfStudents.append(row[5])

	listOfStudents = []

	if len(lasidOfStudents) > 0:

		currentCSV = csv.reader(open(path_userFile, "r"), delimiter=",")

		for row in currentCSV:				
			if row[0] in lasidOfStudents:
				student = []
				student = dict(sourcedid = row[0],
												username = row[6],
												email = row[12])
				listOfStudents.append(student)

	return listOfStudents

def findClass():
	print('\n\n\n')
	displaySearchQuestions('class')


	#get search term
	searchTerm = input('rosterHelper:> ').strip().lower()

	if searchTerm == '':
		input('Please enter a search term. Press enter to try again...')
		findUser()
		return

	classDict = searchCSVForClass(searchTerm)

	if classDict == None:
		print("No class found.\n\n")

		print('1) Try Again')
		print('2) Return to Menu')

		while True:
			selection = input('rosterHelper:> ')

			if selection == '1':
				findClass()
				break
			elif selection == '2':
				menu()
				break

	else:
		printClassInfo(classDict, '')

		print('1) Search Teacher and Students for the Class')
		print('2) New Search')
		print('3) Return to Menu')

		while True:
			selection = input('rosterHelper:> ')

			if selection == '1':
				searchAllAssociatePeopleToTheClass()
				break
			elif selection == '2':
				findClass()
				break
			elif selection == '3':
				menu()
				break
	return 

def searchCSVForClass(searchTerm):

	classDict = None

	if fileType == 'OneRoster':
		#opens user file
		currentCSV = csv.reader(open(path_classFile, "r"), delimiter=",")

		#skips past first row (headers)
		next(currentCSV)

		print('\nSearching User file...')
		time.sleep(searchTime)

		for row in currentCSV:
			if searchTerm == row[0].lower() or searchTerm == row[3].lower():

				if debug:
					print(row)

				print('\n')
				print()

				classDict = dict(sourcedid = row[0],
												status = row[1],
												dateLastModified = row[2],
												title = row[3],
												grades = row[4],
												courseSourcedid = row[5],
												classCode = row[6],
												classType = row[7],
												location = row[8],
												schoolSourcedid = row[9],
												termSourcedid = row[10],
												subjects = row[11],
												subjectCodes = row[12],
												periods = row[13])

				continue

	if fileType == 'SFF':
		#opens user file
		currentCSV = csv.reader(open(path_userFile, "r"), delimiter=",")

		#skips past first row (headers)
		next(currentCSV)	

		print('\nSearching User file...')
		time.sleep(searchTime)



		for row in currentCSV:
			if searchTerm == row[1].lower() or searchTerm == row[5].lower():

				if debug:
					print(row)

				print('\n')
				print()

				classDict = dict(schoolYear = row[0],
												classLocalid = row[1],
												courseid = row[2],
												courseName = row[3],
												courseSubject = row[4],
												className = row[5],
												classDescription = row[6],
												classPeriod = row[7],
												organizationTypeid = row[8],
												organizationid = row[9],
												grade = row[10],
												termid = row[11],
												hmhApplications = row[12])

				continue

	return classDict

def searchCSVForUser(searchTerm):

	userDict = None

	if fileType == 'OneRoster':
		#opens user file
		currentCSV = csv.reader(open(path_userFile, "r"), delimiter=",")

		#skips past first row (headers)
		next(currentCSV)

		print('\nSearching User file...')
		time.sleep(searchTime)

		for row in currentCSV:
			if searchTerm == row[0].lower().lstrip("0") or searchTerm == row[0].lower() or searchTerm == row[6].lower() or searchTerm == row[12].lower():
				#lasid = row[lasidColumn].lstrip("0")
				#print('Row: ' + str(excelCount + 1))
				#print(first_col)

				#if debug:
				#	print(row)

				print('\n')
				print()

				userDict = dict(sourcedid = row[0],
								status = row[1],
								dateLastModified = row[2],
								enabledUser = row[3],
								orgSourceDid = row[4],
								role = row[5],
								username = row[6],
								userIds = row[7],
								givenName = row[8],
								familyName = row[9],
								middleName = row[10],
								identifier = row[11],
								email = row[12],
								sms = row[13],
								phone = row[14],
								agentSourcedids = row[15],
								grades = row[16],
								password = row[17])

				continue

	if fileType == 'SFF':
		#opens user file
		currentCSV = csv.reader(open(path_userFile, "r"), delimiter=",")

		#skips past first row (headers)
		next(currentCSV)	

		print('\nSearching User file...')
		time.sleep(searchTime)



		for row in currentCSV:
			if searchTerm == row[2].lower() or searchTerm == row[8].lower() or searchTerm == row[12].lower():

				if debug:
					print(row)

				print('\n')
				print()

				userDict = dict(schoolYear = row[0],
								role = row[1],
								lasid = row[2],
								sasid = row[3],
								firstName = row[4],
								middleName = row[5],
								lastName = row[6],
								grade = row[7],
								username = row[8],
								password = row[9],
								organizationTypeID = row[10],
								organizationID = row[11],
								primaryEmail = row[12],
								hmhApplications = row[13])

				continue

	return userDict

def printAssociatedTeacher(classDict):
	classDict = findAssociatedTeacher(classDict)

	if classDict['teacherSourcedid'] != '':
		print('{:<40}  {:<40}'.format('Teacher Found:',''))
		print('{:<40}  {:<40} {:<40}  {:<0}'.format('','Username', 'Email', 'SourceDID\n'))
		print('{:<40}  {:<40} {:<40}  {:<0}'.format('', classDict['teacherUsername'], classDict['teacherEmail'], classDict['teacherSourcedid']))
	
	return

def printAssociatedStudents(classDict):

	studentList = findAssociatedStudents(classDict)

	if len(studentList) > 0:
		print('{:<40}  {:<40}'.format('%d Student(s) Found:' % (len(studentList)), ''))
		print('{:<40}  {:<40}  {:<40}  {:<0}'.format( '','Username', 'Email', 'SourceDID\n'))

		for student in studentList:
			print('{:<40}  {:<40}  {:<40}  {:<0}'.format('', student['username'], student['email'], student['sourcedid']))
	
	return

def printAssociatedOrg(classDict):
	currentCSV = csv.reader(open(path_orgsFile, "r"), delimiter=",")

	for row in currentCSV:
		#this checks is the sourcedid in classCSV file contains a substring of the org sourcedid.
		if classDict["schoolSourcedid"].__contains__(row[0]):
			orgName = row[3]
			print('{:<40} {:<40}'.format('Org Name (found in Orgs File):', orgName))
	return

def printClassInfo(classDict, role):

	if fileType == 'OneRoster':
		try:
			print('\n\n============ Class found: %d ============' % (classDict["classAssignmentIndex"] + 1))
		except:
			print('\n\n============ Class found: ===============')

		print('{:<20}  {:<40}'.format('SourceDID:', classDict["sourcedid"]))
		print('{:<20}  {:<40}'.format('Status:', classDict["status"]))
		print('{:<20}  {:<40}'.format('Date Last Modified:', classDict["dateLastModified"]))
		print('{:<20}  {:<40}'.format('Title:', classDict["title"]))
		print('{:<20}  {:<40}'.format('Grades:', classDict["grades"]))
		print('{:<20}  {:<40}'.format('Course SourceDID:', classDict["courseSourcedid"]))
		print('{:<20}  {:<40}'.format('Class Code:', classDict["classCode"]))
		print('{:<20}  {:<40}'.format('Class Type:', classDict["classType"]))
		print('{:<20}  {:<40}'.format('Location:', classDict["location"]))
		print('{:<20}  {:<40}'.format('School SourceDID:', classDict["schoolSourcedid"]))

		if classDict["schoolSourcedid"] != '':
			printAssociatedOrg(classDict)

		print('{:<20}  {:<40}'.format('Term SourceDID:', classDict["termSourcedid"]))
		print('{:<20}  {:<40}'.format('Subjects:', classDict["subjects"]))
		print('{:<20}  {:<40}'.format('Subject Codes:', classDict["subjectCodes"]))
		print('{:<20}  {:<40}'.format('Periods:', classDict["periods"]))


		if role == 'student':
			printAssociatedTeacher(classDict)

		elif role == 'teacher':
			printAssociatedStudents(classDict)

		elif role == 'both':
			printAssociatedTeacher(classDict)
			printAssociatedStudents(classDict)

		print('========================================\n\n')

	if fileType == 'SFF':
		print('\n\n============ Class found: ===============')
		print('{:<20}  {:<40}'.format('SourceDID:', classDict["sourcedid"]))
		print('{:<20}  {:<40}'.format('Status:', classDict["status"]))
		print('{:<20}  {:<40}'.format('Date Last Modified:', classDict["dateLastModified"]))
		print('{:<20}  {:<40}'.format('Title:', classDict["title"]))
		print('{:<20}  {:<40}'.format('Grades:', classDict["grades"]))
		print('{:<20}  {:<40}'.format('Course SourceDID:', classDict["courseSourcedid"]))
		print('{:<20}  {:<40}'.format('Class Code:', classDict["classCode"]))
		print('{:<20}  {:<40}'.format('Class Type:', classDict["classType"]))
		print('{:<20}  {:<40}'.format('Location:', classDict["location"]))
		print('{:<20}  {:<40}'.format('School SourceDID:', classDict["schoolSourcedid"]))
		print('{:<20}  {:<40}'.format('Term SourceDID:', classDict["termSourcedid"]))
		print('{:<20}  {:<40}'.format('Subjects:', classDict["subjects"]))
		print('{:<20}  {:<40}'.format('Subject Codes:', classDict["subjectCodes"]))
		print('{:<20}  {:<40}'.format('Periods:', classDict["periods"]))
		print('========================================\n\n')

	return

def printUserInfo(userDict):
	if fileType == 'OneRoster':
		print('\n\n============== User found ==============')
		print('{:<20}  {:<40}'.format('SourceDID:', userDict["sourcedid"]))
		print('{:<20}  {:<40}'.format('Status:', userDict["status"]))
		print('{:<20}  {:<40}'.format('Date Last Modified:', userDict["dateLastModified"]))
		print('{:<20}  {:<40}'.format('Enabled User:', userDict["enabledUser"]))
		print('{:<20}  {:<40}'.format('Org SourceDID:', userDict["orgSourceDid"]))

		currentCSV = csv.reader(open(path_orgsFile, "r"), delimiter=",")

		for row in currentCSV:
			#if debug:
				#print('checking %s with %s' % (userDict["orgSourceDid"], row[0]))

			#this checks is the sourcedid in classCSV file contains a substring of the org sourcedid.
			if userDict["orgSourceDid"].__contains__(row[0]):
				orgName = row[3]
				print('{:<40} {:<40}'.format('Org Name:', orgName))

		print('{:<20}  {:<40}'.format('Role:', userDict["role"]))
		print('{:<20}  {:<40}'.format('Username:', userDict["username"]))
		print('{:<20}  {:<40}'.format('UserIDs:', userDict["userIds"]))
		print('{:<20}  {:<40}'.format('Given Name:', userDict["givenName"]))
		print('{:<20}  {:<40}'.format('Family Name:', userDict["familyName"]))
		print('{:<20}  {:<40}'.format('Middle Name:', userDict["middleName"]))
		print('{:<20}  {:<40}'.format('Identifier:', userDict["identifier"]))
		print('{:<20}  {:<40}'.format('Email:', userDict["email"]))
		print('{:<20}  {:<40}'.format('Sms:', userDict["sms"]))
		print('{:<20}  {:<40}'.format('Phone:', userDict["phone"]))
		print('{:<20}  {:<40}'.format('Agent SourceDIDs:', userDict["agentSourcedids"]))
		print('{:<20}  {:<40}'.format('Grades:', userDict["grades"]))
		print('{:<20}  {:<40}'.format('Password:', userDict["password"]))
		print('========================================\n\n')

	if fileType == 'SFF':
		print('\n\n============== User found ==============')
		print('{:<20}  {:<40}'.format('School Year:', userDict["schoolYear"]))
		print('{:<20}  {:<40}'.format('Role:', userDict["role"]))
		print('{:<20}  {:<40}'.format('LASID:', userDict["lasid"]))
		print('{:<20}  {:<40}'.format('SASID:', userDict["sasid"]))
		print('{:<20}  {:<40}'.format('First Name:', userDict["firstName"]))
		print('{:<20}  {:<40}'.format('Middle Name:', userDict["middleName"]))
		print('{:<20}  {:<40}'.format('Last Name:', userDict["lastName"]))
		print('{:<20}  {:<40}'.format('Grade:', userDict["grade"]))
		print('{:<20}  {:<40}'.format('Username:', userDict["username"]))
		print('{:<20}  {:<40}'.format('Password:', userDict["password"]))
		print('{:<20}  {:<40}'.format('OrganizationTypeID:', userDict["organizationTypeID"]))
		print('{:<20}  {:<40}'.format('OrganizationID:', userDict["organizationID"]))
		print('{:<20}  {:<40}'.format('Primary Email:', userDict["primaryEmail"]))
		print('{:<20}  {:<40}'.format('HmhApplications:', userDict["hmhApplications"]))
		print('========================================\n\n')

	return

def displaySearchQuestions(question):

	if question == 'user':
		print('Please enter a searchable piece of info for the user below:')

		if fileType == 'OneRoster':
			print('Columns searched: SourceDid, Username, Email')
		elif fileType == 'SFF':
			print('Columns searched: LASID, Username, Primary Email')


	if question == 'class':
		print('Please enter a searchable piece of info for the class below:')

		if fileType == 'OneRoster':
			print('Columns searched: SourceDID, Title')
		elif fileType == 'SFF':
			print('Columns searched: ClassLocalID, ClassName')

	if question == 'error':
		print('Please enter a searchable piece of info for the class below:')

		if fileType == 'OneRoster':
			print('Columns searched: SourceDID, Title')
		elif fileType == 'SFF':
			print('Columns searched: ClassLocalID, ClassName')


	return

def displayRosterHelper():
	print('=========================================')
	print('______              _               ')
	print('| ___ \\            | |              ')
	print('| |_/ /  ___   ___ | |_   ___  _ __ ')
	print('|    /  / _ \\ / __|| __| / _ \\| \'__|')
	print('| |\\ \\ | (_) |\\__ \\| |_ |  __/| |   ')
	print('\\_| \\_| \\___/ |___/ \\__| \\___||_|   ')
	print('| | | |      | |                    ')
	print('| |_| |  ___ | | _ __    ___  _ __  ')
	print('|  _  | / _ \\| || \'_ \\  / _ \\| \'__| ')
	print('| | | ||  __/| || |_) ||  __/| |    ')
	print('\\_| |_/ \\___||_|| .__/  \\___||_|    ')
	print('                | |                 ')
	print('                |_|                 \n')
	print('======================================%.1f'% (version))
	return

#============== BEGINNING OF PROGRAM ================
#clears the cmd prompt
intro()
fileGrabber()
menu()