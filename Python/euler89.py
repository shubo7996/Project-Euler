import urllib.request
import re
import time

class RomanNumerals(object):

	#url of the text File
	file_url = "https://projecteuler.net/project/resources/p089_roman.txt"

	def __init__(self,pattern,replacement):
		self.pattern = pattern
		self.replacement = replacement

	#Reading files from the file Url
	def read_files(self):
		return urllib.request.urlopen(self.file_url).read().decode('utf-8')

	#Calculation of the letters saved
	def convert(self):
		file = self.read_files()
		calculation = len(file) - len(re.sub(self.pattern,self.replacement,file))
		return calculation


if __name__ == '__main__':
	
	start = time.perf_counter()

	#Substractive pair

	#900- DCCCC -> CM
	#400- CCCC -> CD
	#40- XXXX -> XL
	#90- LXXXX -> XC
	#4- IIII -> IV
	#9- VIIII -> IX

	#Conditional OR on the 6 Patterns 
	pattern = "DCCCC|CCCC|XXXX|LXXXX|IIII|VIIII"

	#Replacing the substractive pair with 2 letters
	replacement = "ck"

	#Making the Class Object
	roman_obj = RomanNumerals(pattern,replacement)

	#Calling the calculate function
	result = roman_obj.convert()

	#Printing the result
	print(result)

	end = time.perf_counter()

	print("Time Elapsed: {}".format(end-start))