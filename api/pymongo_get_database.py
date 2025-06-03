from pymongo import MongoClient
def get_database():
 
   CONNECTION_STRING = "mongodb://localhost:27017/sample_lib_db"

   client = MongoClient(CONNECTION_STRING)
 
   return client['sample_lib_db']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()