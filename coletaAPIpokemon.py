#!/usr/bin/env python
# coding: utf-8

# # 1. Python

# ## 1.1. Coleções

# As coleções permitem armazenar múltiplos itens dentro de uma única unidade. As três coleções mais utilizadas em Python, são: **listas**, **tuplas** e **dicionários**.

# ### 1.1.1. Listas

# Lista é uma coleção de valores indexada, em que cada valor é identificado por um índice. O primeiro item na lista está no índice 0, o segundo no índice 1 e assim por diante.

# In[1]:


nomes = [] # Criar uma lista vazia
nomes.append('Daniel Viana') # Append adiciona um item no fim da lista
print(nomes) #imprime a lista na tela


# In[2]:


nomes.append('Ana Maria')
nomes.append('Carlos')


# In[3]:


print(type(nomes)) # imprime o tipo de dado
print(len(nomes)) #imprime o tamanho da lista
print(nomes)
print(nomes[1]) #imprime o item que está na posição 1 da lista


# In[4]:


nomes[1] = 'Bia'
print(nomes)


# In[5]:


nomes.insert(1, 'Rafael') #insere um elemento na lista em uma posição específica
print(nomes)


# In[6]:


nomes.remove('Bia') #remove um elemento da lista
print(nomes)


# In[7]:


nomes.pop(1) #remove um elemento com base no índice
print(nomes)


# ### 1.1.2. Tuplas

# Tupla é uma estrutura de dados semelhante a lista. Porém, ela tem a característica de ser **imutável**, ou seja, após uma tupla ser criada, ela **não pode ser alterada**.

# In[9]:


nomes = ('Carlos', 'Henrique', 'Gabriel') #cria um tupla


# In[10]:


print(type(nomes))
print(len(nomes))
print(nomes)


# In[11]:


print(nomes[2])


# In[12]:


nomes.append('Ana') # NÃO FUNCIONA - TUPLA NÃO PODE SER ALTERADA


# In[13]:


nomes[1] = 'Bia' # NÃO FUNCIONA - TUPLA NÃO PODE SER ALTERADA


# ### 1.1.3. Dicionários

# Os dicionários representam coleções de dados que contém na sua estrutura um conjunto de pares chave/valor, nos quais cada chave individual tem um valor associado.

# In[14]:


cliente = {
    'Nome': 'Carla',
    'Endereco': 'Rua Python',
    'Cidade':'BH',
    'Telefone': '9900005555'
} # Cria um dicionário


# In[15]:


print(type(cliente))
print(len(cliente))
print(cliente)


# In[16]:


print(cliente['Cidade']) # imprime o valor que está na chave Cidade


# In[17]:


print(cliente['Nome']) # imprime o valor que está na chave Nome


# In[18]:


cliente['Idade'] = 45 # Adiciona um novo elemento no dicionário
print(cliente)


# In[19]:


del cliente['Cidade']
print(cliente)


# In[20]:


cliente2 = {
    'Nome': 'Carla',
    'Endereco': 'Rua Python',
    'Cidade':'BH',
    'Telefone': ['9900005555', '8844446666']
} # Cria um dicionário
print(cliente2)


# In[21]:


print(type(cliente2))


# In[22]:


tel = cliente2['Telefone']
print(type(tel))
print(len(tel))
print(tel)


# In[23]:


print(tel[1])


# In[26]:


print(cliente2['Telefone'][0])


# ### 1.1.4. Resumo

# In[27]:


nomes = ['Carla', 'Daniel', 'Ingrid', 'Roberto']
estacoes = ('Primavera', 'Verão', 'Outono', 'Inverno')
pessoa = {
    'Nome': 'Ana',
    'email' : 'ana@ana123.com.br'
}

print(type(nomes)) # list
print(type(estacoes)) # tuple
print(type(pessoa)) # dict


# # Coleta de dados de API

# ## API Pokémon

# In[28]:


# Se as bibliocas não forem instaladas, fazer a instalação das mesmas
import json
import requests


# In[29]:


response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")


# In[30]:


print(response.status_code) #imprime o status da requisição


# In[31]:


print(response.content) #imprime o conteúdo do retornado pela API


# In[32]:


print(type(response.content))   # consultar o tipo de dados


# In[33]:


dados = json.loads(response.content) #serializa a resposta obtida


# In[34]:


print(type(dados))    # consultar o tipo de dados


# 

# In[35]:


for pokemon in dados: #percorre o JSON 
    print(pokemon)


# 

# In[36]:


print(dados["id"]) #id
print(dados["name"]) #nome
print(dados["height"]) #altura
print(dados["weight"]) #peso
print(dados["types"]) #tipos


# In[37]:


pokemon = {}

pokemon["name"] = dados["name"]
pokemon["id"] = dados["id"]
pokemon["height"] = dados["height"]
pokemon["weight"] = dados["weight"]


tipo_pok = []

for tipo in dados["types"]:
    tipo_pok.append(tipo["type"]["name"])

pokemon["type"] = tipo_pok


# In[38]:


print(pokemon)


# # Coleta os dados para armazenar no Mysql

# In[39]:


nomes_pokemons = ["charmander","squirtle","rattata","pikachu","clefairy","meowth","psyduck","poliwag","ponyta","cubone","horsea","electabuzz","magmar","porygon","snorlax","dratini","dragonair"]


# In[40]:


pokemon_list = []
for nome in nomes_pokemons:
    data = requests.get("https://pokeapi.co/api/v2/pokemon/"+nome)
    data_json = json.loads(data.content)
    
    pokemon = {}

    pokemon["name"] = data_json["name"]
    pokemon["id"] = data_json["id"]
    pokemon["height"] = data_json["height"]
    pokemon["weight"] = data_json["weight"]  

    tipo_pok = []

    for tipo in data_json["types"]:
        tipo_pok.append(tipo["type"]["name"])

    pokemon["type"] = tipo_pok
    
    pokemon_list.append(pokemon)   


# In[42]:


print(pokemon_list)


# In[43]:


import mysql.connector


# In[44]:



mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='igti',
    database='db_pokemon'
)

print(mydb)

mycursor = mydb.cursor()


# In[45]:


mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)


# 

# In[46]:


for pokemon in pokemon_list:
    tipo_pok = pokemon["type"][0]
    
    query = "INSERT INTO tb_type (type) SELECT * FROM (SELECT '%s') AS tmp " % tipo_pok
    query += "WHERE NOT EXISTS (SELECT type FROM tb_type WHERE type = '%s') LIMIT 1;"  % tipo_pok

    mycursor.execute(query)

    #Fazer a confirmação da inserção
    mydb.commit()

    print(mycursor.rowcount, "registro(s) inserido(s).")


# In[47]:


for pokemon in pokemon_list:
    tipo_pok = pokemon["type"][0]
    
    query = "INSERT INTO tb_pokemon VALUES(%s, '%s', %s, %s, (SELECT id FROM tb_type WHERE type LIKE '%s')) " % (pokemon["id"], pokemon["name"], pokemon["height"], pokemon["weight"], tipo_pok)
    
    mycursor.execute(query)

    #Fazer a confirmação da inserção    
    mydb.commit()

    print(mycursor.rowcount, " registro inserido.")


# In[48]:


mydb.close() #Fechar o banco de dados

