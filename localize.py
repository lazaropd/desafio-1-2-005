from read_file import CSVFile
from opencage.geocoder import OpenCageGeocode

key = '09aadb1b1d8840acacfa0fcece0acb13'
geocoder = OpenCageGeocode(key)

class geoCode:

	def __init__(self,data):
		self.data = data
		self.topics = ["country","state","state_code","city"]

	def check_localization(self):
		indlat = self.data[0].index("Latitude")	
		indpais = self.data[0].index("Pais")
		
		for line in self.data[1:]:

			lat = self.parse_float(line[indlat])
			lon = self.parse_float(line[indlat+1])

			# retorna informacoes de lat,lon
			geo = geocoder.reverse_geocode(lat,lon)
			# separa as informacoes de localizacao
			comp = geo[0]['components']
			# separa as info de pais, estado, codigo de estado, cidade
			info = self.get_info(comp)
			#print(info)

			res = []
			# compara as informacoes da tabela com a da api
			result = self.info_compare(line,info,indpais)
			res.append(result)
		return res


	# tenta a leitura de numeros float para latitude e longitude 
	def parse_float(self,info):
		try:
			value = float(info)
		except:
			value = 0.0
		return value

	def get_info(self,components):
		aux = []
		for elem in self.topics:
			try:
				value = components[elem]
			except:
				value = "Sem Informações"
			aux.append(value)
		return aux
	
	# compara as informacoes existentes
	def info_compare(self,line,info,indpais):
		correct = True
		i=0
		while i<4:
			if line[indpais+i]!="Sem Informações":
				if i==1 and (line[indpais+i]!=info[1] and line[indpais+i]!=info[2]):
					i+=2
					correct = False
				elif line[indpais+i]!=info[i]:
					correct = False
			i+=1
		return correct	 			


if __name__ == "__main__":
	cfile = CSVFile()
	cfile.read_file("portalbio_export_16-10-2019-14-39-54.csv")

	g = geoCode(cfile.data)
	result = g.check_localization()
	print(result)



