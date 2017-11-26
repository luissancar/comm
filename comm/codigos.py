class Codigos:
	codigo = {'a': '00', 'b': '01','c': '10', 'd': '11'}
	
	def getCodigo(self, cod):
		return self.codigo[cod]
		
	def getCodigoSecuencia(self, cod):
	    primera=self.codigo[cod][0]
	    segunda=self.codigo[cod][1]
	    return primera, segunda
	    
	def getCaracter(self,cod):
		for secuencia in self.codigo:
			if cod == self.codigo[secuencia]:
				return secuencia
		return "error"		    
	    	
