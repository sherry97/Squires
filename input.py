import re
from mechanize import Browser

def main():
	# http://stackoverflow.com/questions/8377055/submit-data-via-web-form-and-extract-the-results
	browser = Browser()
	browser.open("http://bookblog.net/gender/genie.php")

if __name__ == '__main__': main()