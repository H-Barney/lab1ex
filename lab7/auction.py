class System(object):

class User(object):
	def __init__(self,name):
		self._name = name
		self._id = #random number gen
		
	def list_bids(self):
		#Sort through bids for matching seller ID and add to list
	
	def list_user_items(self):
		#Sort through items for matching seller ID and add to list

class Item(object):
	def __init__(self,name,desc,startPrice,itemType,input1,input2):
		self._bidID = #Random Number Gen
		self._sellerID = User._id
		self._itemName = name
		self._itemDesc = desc
		self._startPrice = startPrice
		self._itemType = itemType
		#Add additional info based off item type,
		#Only 2 more info pieces per item so generic store, sprted by itemtype
		self._addInfo1 = input1
		self._addInfo2 = input2		
				
	def list_all_items(self):
		#Forms a list of all items current for auction
		
class Electronic_items(Item):

class Furniture_items(Item):

class Book_items(Item):
		
	
class Bid_Info(object):
	def __init__(self):
		self._currentBid = 
		self._time = #Time remaining on bid
		self._currentBidder = 
		
	def new_bid(self):
		#Determines if a new bid is valid
		#Updates new info for current bidder
		#Calls for old info to be moved to previous bidder list
		previous_bids()
		self._currentBid = newPrice
		self._time = #Time remaining on bid
		self._currentBidder = User._bidderID
		
		
	
	def previous_bids(self):
		#After a new bid is added, old bidder info is added to database for the item
		#Only called as a new bid is introduced, so uses current info
	
	def auction_win(self):
		#Sends a message to current bidder after 48hrs of item posting
	
	


