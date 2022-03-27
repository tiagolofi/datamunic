"""
Módulo para trabalhar com dados da Pesquisa de Perfil dos Municípios
"""

from pandas import read_excel
from re import sub
from json import dumps

class DataMunic(object):
	"""Módulo para trabalhar com dados da Pesquisa de Perfil dos Municípios"""
	def __init__(self, county: int, name_survey: str):
		super(DataMunic, self).__init__()
		self.county = county
		self.name_survey = name_survey

	def __read_dictionary(self):

		dictionary = read_excel('data/Base_MUNIC_2020.xlsx', sheet_name = 'Dicionário', usecols = 'A:E', skiprows = 28, header = None)

		dictionary['NameVar'] = dictionary[0].astype(str) + dictionary[1].astype(str) + dictionary[2].astype(str) + dictionary[3].astype(str)
		
		dictionary = dictionary.drop(columns = [0, 1, 2, 3])
		
		dictionary['NameVar'] = [sub('nan', '', i) for i in dictionary['NameVar']] 

		dictionary = dictionary.dropna(subset = [4])

		dictionary = dictionary[dictionary[4] != 'subtítulo link']

		dictionary.columns = ['CodeVar', 'NameVar']

		dictionary['CodeVar'] = [i.upper() for i in dictionary['CodeVar']]

		dictionary = dictionary.transpose().reset_index(drop=True)

		dictionary.columns = dictionary.iloc[0]

		dictionary = dictionary.drop([0], axis = 'index')

		dictionary = dictionary.to_dict(orient = 'records')[0]

		return dictionary

	def __read_survey(self):

		survey = read_excel('data/Base_MUNIC_2020.xlsx', sheet_name = self.name_survey)

		survey.columns = [i.upper() for i in survey.columns]

		return survey

	def get_county(self):

		survey = self.__read_survey()

		survey = survey[survey['CODMUN'] == self.county]

		survey = survey.to_dict(orient = 'records')[0]

		dictionary = self.__read_dictionary()

		name_vars = list(survey.keys())

		number_var = range(1, len(name_vars)+1)

		for i, j in zip(name_vars, number_var):

			survey[str(j) + ' - ' + dictionary.get(i)] = survey.pop(i)

		survey = dumps(survey, indent = 2, ensure_ascii = False).encode('utf-8').decode()

		return survey

if __name__ == '__main__':

	while True:

		code = int(input('Código IBGE do Município:\n'))

		name = str(input('\nNome da Pesquisa:\n'))

		DM = DataMunic(county = code, name_survey = name)

		print('\n', DM.get_county(), '\n')
