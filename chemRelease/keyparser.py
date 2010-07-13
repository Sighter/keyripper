
from html.parser import HTMLParser


# class -- () {{{
# 
# 
# ****************************** #
class keyParser(HTMLParser):
	# init all variables
	nameFound = False
	titleFound = False
	entryFound = False
	keyFound = False
	tdCount = 0
	artistname = ""
	titlename = ""
	key = ""
	artists = []
	titles = []
	keys = []

	def handle_starttag(self, tag, attrs):
		# look for an entry and set flag
		if ( tag == "tr" and len(attrs) != 0 and attrs[0][0] == "class" ):
			self.entryFound = True
			self.tdCount = 0
		# if entry is found the data is organized in tables
		# so count the td
		if ( tag == "td" and self.entryFound == True):
			self.tdCount +=  1
			# the name is in the first td
			if ( self.tdCount == 2 ): # 
				self.nameFound = True
			# title at second
			if ( self.tdCount == 3 ):
				self.titleFound = True
		
		# key is in the first href
		if ( self.entryFound == True and self.tdCount == 4 and tag == "a" ):
			self.keyFound = True


	def handle_endtag(self,tag):
		if ( tag == "tr" and self.entryFound == True):
			self.entryFound = False
			self.nameFound == False
		if ( tag == "td" and self.nameFound == True):
			self.artists.append( self.artistname.lstrip('\n\r ').rstrip('\n\r ') )
			self.artistname = ""
			self.nameFound = False
		if ( tag == "td" and self.titleFound == True):
			self.titles.append( self.titlename.lstrip('\n\r ').rstrip('\n\r ') )
			self.titlename = ""
			self.titleFound = False
		if ( tag == "a" and self.keyFound == True):
			self.keys.append( self.key.lstrip('\n\r ').rstrip('\n\r ') )
			self.key = ""
			self.keyFound = False

	def handle_data(self,data):
		if ( self.nameFound == True):
			self.artistname += data
		if ( self.titleFound == True):
			self.titlename += data
		if ( self.keyFound == True):
			self.key = data
# end of }}} #

