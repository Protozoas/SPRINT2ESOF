import openpyxl, pprint #Importa o modulo

wb = openpyxl.load_workbook('censuspopdata.xlsx')     #Abre o arquivo
sheet = wb.get_sheet_by_name('Population by Census Tract')        #Abre a pagina pelo nome
countyData = {}

for row in range(2, sheet.max_row() + 1):      #Fixa o valor nas linhas, começando da 2ª e indo até a maior + 1
    state = sheet['B' + str(row)].value      #Pega o valor na celula Brow
    county = sheet['C' + str(row)].value     #Pega o valor na celula Crow
    pop = sheet['D' + str(row)].value        #Pega o valor na celula Drow
    countyData.setdefault(state, {})         #Confere se o nome do estado existe no dicionario
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})     #Confere se existe a chave para esse municipio existe
    countyData[state][county]['tracts'] += 1 #Pra contar quantas linhas tem o municipio
    countyData[state][county]['pop'] += int(pop)    #Pra somar a população no municipio
    
resultFile = open('census2010.py', 'w') 
resultFile.write('allData = ' + pprint.pformat(countyData))  #Abre um novo arquivo e escreve os resultados do countyData lá
resultFile.close()
print('Done.')
