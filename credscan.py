import art
from colorama import Fore
from functions import scan_creds
import helium
import sys
#import argparse


# Start the browser depending on what the user chose as their option
def startbrowser():
	if browser == 'f':
		helium.start_firefox(url, headless=True)
	else:
		helium.start_chrome(url, headless=True)




art.tprint('CredScanner')

# The URL for the page to be stuffed
url = input('> Login Page URL: ').strip()


# Allow the user to choose the browser
browser = input('> Firefox (f) or Chrome (c) [Use Chrome if neither specified] ')


# This part of the code is for the user to choose their parameters
# --------------------------------------------------------------------------------------------------------------------------------------

# Start the browser and search for parameters, put them in a number indexed dictionary
startbrowser()
fields = helium.find_all(helium.S('input'))

# Get the name of each param, important because it defines HTTP post request parameters
fields_names = []
for field in fields:
	temp = field.web_element.get_attribute('placeholder')
	fields_names.append(temp)

fields_names = dict(enumerate(fields_names, start=1))

# Show the user the displayable fields
for x in fields_names:
	print(f'{x}: {fields_names[x]}')


# Allow the user to choose the available parameters

choosing_params = True
while choosing_params:
	field_options = input('> Enter the numbered fields for the username and password, separated by commas [e.g 1,2] ').strip().split(',')


	try:
		# Add the available site to the list
		chosen_fields = []
		for x in field_options:
			if int(x) in fields_names.keys():
				chosen_fields.append(fields_names[int(x)])
				choosing_params = False
			else:
				choosing_params = True
				break

	# Error handling
	except (TypeError, ValueError):
		print(Fore.YELLOW + '[!] You must enter numbers' + Fore.RESET)
		continue



# --------------------------------------------------------------------------------------------------------------------------------------



# Allow the user to specify the file with the credentials they would like to use
outputfile = input('Enter the output file ')
if outputfile != '':

	try:
		open(outputfile, 'r')

	except FileNotFoundError:
		print(Fore.YELLOW + '[!] This file does not seem to exist' + Fore.RESET)
		sys.exit()

	except PermissionError:
		print(Fore.YELLOW + '[!] Insufficient permissions' + Fore.RESET)
		sys.exit()

else:
	outputfile = None

# Allow the user to specify the output of the file they would like
credfile = input('> Enter the file you would like to read the credentials from: ')


# Enter the text that is visible ONLY when incorrect credentials are entered:
wrong_text = input('> Enter text that appears upon incorrect credential submission: ')


scan_creds(url=url, params=chosen_fields, credential_file=credfile, incorrect_text=wrong_text, outfile=outputfile)


# AI was not used in the creation of this program
