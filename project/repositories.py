# repositories.py

from django.conf import settings
import pymongo

class WeatherRepository:

	collection = ''
	
	def __init__(self, collectionName) -> None:
			self.collection = collectionName
			
	def getConnection(self):
	    stringConnection = getattr(settings, "")
	    database = getattr(settings, "")
	    client = pymongo.MongoClient()