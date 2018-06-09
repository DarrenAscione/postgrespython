import psycopg2
from pprint import pprint

class DatabaseConnection:
	def __init__(self, dbname, user, password):
		try:
			self.connection = psycopg2.connect(
				"dbname='%s' user='%s' host='localhost' password='%s' port='5432'"%(dbname, user, password))
			self.connection.autocommit = True
			self.cursor = self.connection.cursor()
		except:
			pprint("Failure to connect to DataBase")

	def create_table(self, table_name, variables):
		sql = "CREATE TABLE %s(%s)"%(table_name, variables)
		self.cursor.execute(sql)

	def insert_record(self, table_name, record):
		sql = "INSERT INTO %s VALUES('%s');"%(table_name, record)
		pprint(sql)
		self.cursor.execute(sql)

if __name__ == '__main__':
	database_connection = DatabaseConnection('savings_db', 'phantomband2503', '')
	database_connection.create_table('testing', 'test TEXT')
	database_connection.insert_record('testing', 'fuck you')


