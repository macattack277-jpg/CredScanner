# CredScanner

This is a POC (proof-of-concept) tool designed to demonstrate how attackers can automate the process of trying a list of credentials on a website. This is a very real scenario, as there is a limitless supply of breached data available on the internet, and therefore bad actors who will use it to their advantage. This program was built purely for educational purposes, and therefore should be used purely for educational purposes. I'll also note that AI has not been used in this program's creation.

## Installation
This repository includes the Python library that executes the process of testing credentials, as well as an additional CLI menu to simplify the process of testing.

**Navigate to your terminal and do the following to install:**

``git clone git@github.com:macattack277-jpg/CredScanner.git credscanner``

``cd credscanner``

**Create a virtual environment (recommended):**

``python3 -m venv .venv``

``source ./.venv/bin/activate``

**Install the requirements:**

``pip install -r requirements.txt``

The program should now be ready to run.

# Basic Usage

Fortunately, I created a CLI interface to make CredScanner easy to use (credscan.py).

I created an test website on localhost with the credentials that appeared correct hardcoded:

<img width="749" height="474" alt="image" src="https://github.com/user-attachments/assets/86e9bf14-5067-418c-b4a3-025f8b0b85ed" />

- The URL should be the full URL of the login page you're testing (http/https://thissitedoesnotexist.com)

- Specify f or c to choose the browser you want to use. Note that the 'browsers' are ran headless so therefore have no output.

- For the parameters, the CLI automatically browses the site, finds every 'input' tag, and returns their 'placeholder' value. They are numbered, so choose the number values of the ones you're testing separated by commas.

- The output file is optional; If you wish, you can just print to stdout.

- For the credential file, you want your file to contain the values separated by ':'. Here's what I used in the example:

<img width="546" height="147" alt="image" src="https://github.com/user-attachments/assets/cd39805c-3ecb-4ed8-90db-871fa562714c" />

- The 'incorrect text' specifies the text that appears ONLY when the account details are incorrect. Note that on sites where there may be rate limiting and factors causing different responses, this may cause the program to be innacurate.


# Other information

Please note that this tool was created by me for educational purposes only. If you use this tool for illegal/unauthorized purposes, I am not liable. Please also note that currently this tool does not include custom proxy/user agent settings, so on the majority of sites rate limiting and other issues will likely be of concern anyway. This tool is purely proof of concept.

# To do (maybe)

- Add a command line tool using the argparse library

- Add custom threading settings so that users can use more of their computer's resources for faster results

- Add proxy/custom fingerprint features

# Conclusion

If you have any feedback or you find any issues with the program, don't hesitate to contact me :)


