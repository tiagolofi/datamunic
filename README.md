# API para dados da Pesquisa dos Municípios

1. Selecionando um município

* Alguns municípios: 

- São Luís: 2111300
- São Paulo: 3550308
- Rio de Janeiro: 3304557

2. Selecionando uma pesquisa

* Nomes das pesquisas:

- Recursos humanos
- Habitação
- Transporte
- Agropecuário
- Meio ambiente
- Gestão de riscos
- COVID-19

3. Um simples programa

```python

from datamunic import DataMunic

while True:

	code = int(input('Código IBGE do Município:\n'))

	name = str(input('\nNome da Pesquisa:\n'))

	info = DataMunic(county = code, name_survey = name)

	print('\n', info.get_county(), '\n')

```

4. A fazer

- Link entre pergunta e resposta
- API Rest
