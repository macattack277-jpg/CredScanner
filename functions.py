import helium
import sys
from colorama import Fore

# The function
def scan_creds(url, params, credential_file, incorrect_text, browser='firefox', outfile=None):
	

	# Open the browser depending on what's specified by the user
	def open_browser(link):
		if browser == 'firefox':
			helium.start_firefox(url=link, headless=True)
		elif browser == 'chrome':
			helium.start_chrome(url=link, headless=True)
		else:
			print('You need to specify chrome or firefox')
			sys.exit()




	# Just some error handling
	try:
		open(credential_file, 'r')
	except PermissionError:
		print(Fore.YELLOW + f'[!] Insufficient permissions for {credential_file}' + Fore.RESET)
		sys.exit()

	
	if outfile is not None:
		try:
			open(outfile, 'w+')
		except PermissionError:
			print(Fore.YELLOW + f'[!] Insufficient permissions for {outfile}' + Fore.RESET)

	# Open the credential file for reading
#	try:
	with open(credential_file, 'r+') as file:
		while True:
			line = file.readlines()
			# Read through every line in the file containing credentials split by ':', enter them into their respective parameters, and enter them
			# If Stop the program once there's no more credentials to go through
			if not line:
				print('Finished')
				file.close()
				break

			for data in line:
				open_browser(url)
				creds = data.strip('\n').split(':')
				# Write the credentials into their respective parameters and enter
				for num, param in enumerate(params):
					helium.write(creds[num], into=param)
				helium.press(helium.ENTER)
				
			# If the text that is specified to appear upon an incorrect submission appears, return negative
				if helium.Text(incorrect_text).exists():
					print(Fore.RED + '[X] ' + data + Fore.RESET)

				# If the text that is specifited to appear upon an incorrect submission DOES NOT appear, return positive
				# and add the correct credentials to the file IF the user specified one
				else:
					print(Fore.GREEN + '[✔] ' + data + Fore.RESET)
					if outfile is not None:
						with open(outfile, 'w+') as file2:
                                       			file2.write(':'.join(line))
						file2.close()
				helium.kill_browser()


#	except:
#		pass
#		print(Fore.YELLOW + '[!]  Unspecified error' + Fore.RESET)
#		sys.exit(1)



# No AI was used in the creation of this program
# scan_creds(url='localhost', params=['Enter your username', 'Enter your password'], credential_file='accounts.txt', incorrect_text='Invalid username or password.', browser='chrome', outfile=None)
