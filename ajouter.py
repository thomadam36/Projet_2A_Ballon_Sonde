def ajouter ( donnee ):

	f = open('donnees.txt','a')
	f.write(str(donnee)+';')
	f.close()
	
