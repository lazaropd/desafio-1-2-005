

			
class CSVFile():

	def __init__(self):
		self.arquivo = None
		self.data = list()

	# self.data armazena uma lista contendo as linhas do arquivo csv
	def read_file(self, filePath):

		try: 
			f = open(filePath,"r", encoding='utf-8')
			data = f.readlines()
			self.data = list(  map(lambda line: line.strip("\n").split(";"), data) )
			f.close()

		except IOError as e:
			print (e.args)			
			return None



"""
filePath = input("File path: ")
cfile = CSVFile()
cfile.read_file(filePath)
print(cfile.data)
"""






