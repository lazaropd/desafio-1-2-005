from read_file import CSVFile
from opencage.geocoder import OpenCageGeocode
import geopy.distance

key = '09aadb1b1d8840acacfa0fcece0acb13'
geocoder = OpenCageGeocode(key)

class geoCode:

	def __init__(self,data):
		self.data = data
		self.topics = ["country","state","state_code","city"]

	def check_localization(self):
		indlat = self.data[0].index("Latitude")	
		indpais = self.data[0].index("Pais")

		result = []
		for line in self.data[33:36]:

			lat = self.parse_float(line[indlat])
			lon = self.parse_float(line[indlat+1])

			geo = geocoder.reverse_geocode(lat,lon)   # retorna info de lat,lon
			comp = geo[0]['components']               # separa info de localizacao
			info = self.get_info(comp)		  
			
			res = self.info_compare(line[indpais:indpais+3],info)
			
			if not res:
				rlat,rlon = self.get_latlon(line[indpais:indpais+3])
				dist = self.get_distance((lat,lon),(rlat,rlon))
				result.append(dist)
			else:
				result.append(res)
		
		return result



	# tenta a leitura de numeros float para latitude e longitude 
	def parse_float(self,info):
		try:
			value = float(info)
		except:
			value = 0.0
		return value


	# separa as informacoes de país, estado, código de estado e cidade
	def get_info(self,components):
		aux = []
		for elem in self.topics:
			try:
				value = components[elem]
			except:
				value = "Sem Informações"
			aux.append(value)
		return [aux[0],(aux[1],aux[2]),aux[3]]


	# compara as informacoes existentes
	def info_compare(self,line,info):

		correct = True
		for i, elem in enumerate(line):
			if line[i]!="Sem Informações" and info[i]!= "Sem Informações":
				if i==1:
					if (line[i]!=info[i][0] and line[i]!=info[i][1]):
						correct = False
				elif line[i]!=info[i]:
					correct = False
		return correct 


	# busca a latitude e longitude de um endereco
	def get_latlon(self,line):
		
		address = self.concat_info(line) 
		geo = geocoder.geocode(address)
		lat,lon = geo[0]['geometry']['lat'], geo[0]['geometry']['lng']
		return lat,lon
		

	# concatena info em string para fazer a busca no geocode
	def concat_info(self,line):
		aux = ""
		for elem in line:
			if elem != "Sem Informações":
				aux += elem + ","
		return aux[:-1]
	

	# calcula distancia entre duas coordenadas
	def get_distance(self,coord1, coord2):
		return geopy.distance.geodesic(coord1,coord2).km
	
			


if __name__ == "__main__":
	cfile = CSVFile()
	cfile.read_file("portalbio_export_16-10-2019-14-39-54.csv")

	g = geoCode(cfile.data)
	result = g.check_localization()
	print(result)
