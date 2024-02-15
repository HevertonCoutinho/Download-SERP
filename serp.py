from googlesearch import search
import pandas as pd
from datetime import datetime

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

print('================================================')
print('GOOGLE SEARCH')
print('================================================')
# Get user search keyword.
searchKeyWord = input('Digite a sua pesquisa Google: ')
# Get Total number of records.
totalNoOfRecords = input('Quantos resultados de busca você deseja salvar em seu arquivo CSV? ')
print('Por favor aguarde. Sua requisição está sendo processada. \n')
resultLinks = []
# minha parte aqui
for result in search(searchKeyWord, tld="co.in", num=int(totalNoOfRecords), stop=None, pause=12):
    print(result)
    resultLinks.append[result]
# Search the keyword in google.
#results = search(searchKeyWord, num_results=int(totalNoOfRecords))-->
#results = '\n'.join([str(elem) for elem in results])
# Convert result into data frame.
df = pd.DataFrame(resultLinks)
now = datetime.now()
outputFileName = 'SearchOutput' + now.strftime("%d-%m-%Y") + '.csv'
# Write output in CSV format.
df.to_csv(outputFileName,mode='a', encoding='utf-8', index=False , header=False)
print('================================================\n')
print('Pesquisa concluida com sucesso!!. Por favor, cheque o arquivo output criado em sua pasta!!\n')
print(outputFileName + '\n')
print('================================================\n')
