
import urllib.request
from chemRelease.keyparser import keyParser


# class -- () {{{
# 
# 
# ****************************** #
class key:
	
	# init class variables
	# ******************** #
	baselink = r"http://www.chemical-records.co.uk/sc/servlet/Info?Track="
	catid = ""
	html = ""

	artists = ""
	titles = ""
	keys = ""

	# constructor -- __init__() {{{
	# @ catalouge ID
	# < object
	# ****************************** #
	def __init__(self,catid):
		response = urllib.request.urlopen( self.baselink + catid )
		self.html = response.read()
		self.html = self.html.decode('Latin1')
		#f = open('html',"r")
		#self.html = f.read()
		#f.close()
		
	# end of }}} #


	# method -- fetch() {{{
	# @ 
	# < list of with track names and keys
	# *********************************** #
	def fetch(self):
		keyP = keyParser()
		keyP.feed(self.html)

		self.artists = keyP.artists
		self.titles = keyP.titles
		self.keys = keyP.keys
		
	# end of }}} #

# end of }}} #
