#!/usr/bin/env python
# coding: utf-8

# # Coleta de Dados e adicionar no MySQL
# Os arquivos estão disponiveis para downloads no site da receita federal, mas não possuem delimitadores internos, existe um arquivo com o layout para auxiliar.
# Outro trabalho será baixar os 20 arquivos fazer a leitura individual, linha por linha, separando informações que são de nosso interesse .

# ### layout da tabela receita no mySQL
# 
# ##### Este layout foi desenvolvido no mysql, coloquei aqui para facilitar na conversão do tipo durante a programação
# 
#  `id` int NOT NULL AUTO_INCREMENT,
# 
# `cnpj` varchar(14) DEFAULT NULL,
# 
# `identificador` int DEFAULT NULL,
# 
# `razao_social` varchar(150) DEFAULT NULL,
# 
# `fantasia` varchar(55) DEFAULT NULL,
# 
# `situacao_cadastral` int DEFAULT NULL,
# 
# `data_situacao` datetime DEFAULT NULL,
# 
# `motivo_situacao` int DEFAULT NULL,
# 
# `cidade_exterior` varchar(55) DEFAULT NULL,
# 
# `codigo_pais` varchar(3) DEFAULT NULL,
# 
# `nome_pais` varchar(70) DEFAULT NULL,
# 
# `natureza_juridica` int DEFAULT NULL,
# 
# `data_inicio_atividade` datetime DEFAULT NULL,
# 
# `cnea_fiscal` int DEFAULT NULL,
# 
# `tipo_logradouro` varchar(20) DEFAULT NULL,
# 
# `logradouro` varchar(60) DEFAULT NULL,
# 
# `numero` varchar(6) DEFAULT NULL,
# 
# `complemento` varchar(156) DEFAULT NULL,
# 
# `bairro` varchar(50) DEFAULT NULL,
# 
# `cep` int DEFAULT NULL,
# 
# `uf` varchar(2) DEFAULT NULL,
# 
# `codigo_municipio` int DEFAULT NULL,
# 
# `municipio` varchar(50) DEFAULT NULL,
# 
# `telefone1` varchar(12) DEFAULT NULL,
# 
# `telefone2` varchar(12) DEFAULT NULL,
# 
# `telefone3` varchar(12) DEFAULT NULL,
# 
# `email` varchar(115) DEFAULT NULL,
# 
# `qualif_responsavel` int DEFAULT NULL,
# 
# `capital_social` float DEFAULT NULL,
# 
# `porte_empresa` varchar(2) DEFAULT NULL,
# 
# `opcao_simples` varchar(1) DEFAULT NULL,
# 
# `data_opcao_simples` datetime DEFAULT NULL,
# 
# `data_exclusao_simples` datetime DEFAULT NULL,
# 
# `opcao_mei` varchar(1) DEFAULT NULL,
# 
# `situacao_especial` varchar(23) DEFAULT NULL,
# 
# `data_situacao_especial` datetime DEFAULT NULL
#  

# ## Conectar ao MySQL 

# In[1]:


#Importando conector MySQL

import mysql.connector


# 

# In[2]:


#Conectar ao MySQL Server sem selecionar um banco de dados

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='igti'
)

print(mydb)

mycursor = mydb.cursor()


# 

# In[3]:


#Retorna todos os esquemas criados no seu servidor de Banco de Dados

mycursor.execute("SHOW DATABASES") 

for db in mycursor:
    print(db)


# 

# In[2]:


#Login ao banco de dados

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='igti',
    database='db_receita'
)

print(mydb)

mycursor = mydb.cursor()


# # 

# In[3]:


#Retorna todas as tabelas criados no seu esquema de Banco de Dados 

mycursor.execute("SHOW TABLES")

for db in mycursor:
    print(db)


# 

# In[3]:


import os

from tkinter  import filedialog

filenames = filedialog.askopenfilenames()
print(filenames)
#filedialog.askopenfilenames.cancel_command()


# In[ ]:


from datetime import date

# Abrir arquivos Texto
tamanho = len(filenames)
conta = 0
selecao = 0

while(conta < tamanho):

#    print('Número do arquivo: '+str(conta))    
    arquivo = open(filenames[conta], 'r')
    #print(arquivo.name)
    print(arquivo.name + '  /  '+  "Seleção: " + str(selecao))

    for linha in arquivo:
        entrada = linha[0:2]
        
        lnh = linha[-600:]
        quintaparte =  lnh[0:173]
        codigo_municipio = quintaparte[83:87]
        
        if entrada == '1F' and codigo_municipio == '3505708':

            selecao += 1

            primeiraparte = linha[0:150]
        
            lnh = linha[-1050:]
            segundaparte =  lnh[0:150]
        
            lnh = linha[-900:]
            terceiraparte = lnh[0:150]
        
            lnh = linha[-750:]
            quartaparte =  lnh[0:150]
        
            lnh = linha[-600:]
            quintaparte =  lnh[0:173]
        
            lnh = linha[-450:]
            sextaparte =  lnh[22:175]
        
            lnh = linha[-300:]
            setimaparte =  lnh[0:150]
        
            cnpj = primeiraparte[3:18]
            razao_Social = primeiraparte[18:155]
            fantasia = segundaparte[17:72]
            situacao_Cadastral = segundaparte[72:74]
            data_Situacao = segundaparte[74:82]
#--------->                                   
            motivo_Situacao = segundaparte[82:86]
            CNAE = terceiraparte[74:81]
            data_inicio = terceiraparte[66:74]
#--------->            
            natureza_juridica = int(terceiraparte[62:66])
            logadouro = (terceiraparte[81:150] + ',' + quartaparte[11:14])
            codigo_municipio = quintaparte[83:87]
            bairro = quintaparte[23:73]
            CEP = quintaparte[73:81]
            UF = quintaparte[81:83]
            municipio = quintaparte[87:137]
            telefone1 = quintaparte[137:149]
            telefone2 = quintaparte[149:161]
            telefone3 = quintaparte[161:173]
            email = sextaparte[1:116]
            responsavel = sextaparte[116:118]
            capital_social = float(sextaparte[118:132])
            porte_emp = sextaparte[132:134]
            opcao_Simples = sextaparte[134:135]
#--------->
            data_opcao_Simples = sextaparte[135:143]
#--------->            
            data_exclusao = sextaparte[143:151]
            excAno = data_exclusao[0:4]
            excMes = data_exclusao[4:6]
            excDia = data_exclusao[6:8]
            dataexclusao = (excAno+'-'+excMes+'-'+excDia)
            if excAno != '0000' and excMes != '00' and excDia != '00':
                dataexclusao = date.fromisoformat((excAno+'-'+excMes+'-'+excDia))
            else:
                excAno = '0000'
                excMes = '00'
                excDia = '00'
           
            opcao_MEI = sextaparte[151:152]
#---------> inserindo dados na tabela
            mycursor.execute ("INSERT INTO tb_receita (cnpj, razao_social, fantasia, situacao_cadastral, data_situacao, motivo_situacao, natureza_juridica, data_inicio_atividade, cnea_fiscal, logradouro, bairro, cep, uf, codigo_municipio, municipio, telefone1, telefone2, telefone3, email, qualif_responsavel, capital_social, porte_empresa, opcao_simples, data_opcao_simples, data_exclusao_simples, opcao_mei) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s);", (cnpj, razao_Social, fantasia, situacao_Cadastral, data_Situacao, motivo_Situacao, natureza_juridica, data_inicio , CNAE, logadouro, bairro, CEP, UF, codigo_municipio, municipio, telefone1, telefone2, telefone3, email, responsavel, capital_social, porte_emp, opcao_Simples, data_opcao_Simples, dataexclusao, opcao_MEI))

# --------> Fazer a confirmação da inserção
            mydb.commit()
        
    conta += 1
    arquivo.close()
        


# In[9]:


#mycursor.execute ("DELETE  FROM db_receita.tb_receita")
#mydb.commit()

