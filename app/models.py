class Collection:
   'Common base class for all collections'
   collectionCount = 0

   def __init__(self, xid, name, description):
      self.xid = xid
      self.name = name
      self.description = description
      Collection.collectionCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Collection.collectionCount)

   def displayCollection(self):
      print ("Name : ", self.name,  ", xid: ", self.xid)
		

