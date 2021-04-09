# Coleta de Dados no MySQL utilizando o R

#### Para mais detalhes sobre a biblioteca RMariaDB consulte:
* https://cran.r-project.org/web/packages/RMariaDB/RMariaDB.pdf

##### Instalar o pacote RMariaDB


```python
# Instalar o pacote RMariaD se for a primeira vez que for utlizar.

install.packages("RMariaDB")
```

# Importar o pacote RMariaDB


```python
#importação do pacote deve ser SEMPRE realizada

#Importa pacote RMariaDB se ele ainda não foi carregado
if(!"RMariaDB" %in% (.packages())){require(RMariaDB)}
```

**Observação 1:** A mensagem abaixo não indica um erro, é um alerta indicando a versão do R no qual o pacote RMariaDB foi construindo.

*Loading required package: RMariaDB
Warning message:
"package 'RMariaDB' was built under R version 3.6.3"*

**Observação 2:** A mensagem abaixo indica um erro, alertando que não existe o pacote RMariaDB instalado. Para corrigir, instale o pacote.

*Loading required package: RMariaDB
Warning message in library(package, lib.loc = lib.loc, character.only = TRUE, logical.return = TRUE, :
"there is no package called 'RMariaDB'"*



```python
#Conecta ao SGBD MySQL --> Banco de dados bootcamp
con <- dbConnect(MariaDB(), user = "root", password = "igti",
                 dbname = "bootcamp", host = "localhost",serverTimezone='UTC')
```

**OBS:** Caso ocorra o erro abaixo: 
*Error: Failed to connect: Plugin caching_sha2_password could not be loaded: The specified module could not be found.*

Acesse seu SGBD MySQL Server utilizando o MySQL Workbench e execute o comando abaixo no seu esquema de BD

    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'igti';

Agora execute o comando de conexão novamente.


```python
#Para listar quais tabela existem no esquema .bootcamp. execute:

#Lê a lista de tabelas no BD
tables <- dbListTables(con) 
tables
```


```python
#Para consultar quais os dados de uma tabela execute:
# dbReadTable(nome-da-conexao,"nome-da-tabela")

#Consulta os dados da tabela *estado*
tabledata <- dbReadTable(con,"estado")
tabledata
```

**OBS:** Veja que o resultado do comando acima demonstra que a tabela 'estado' não possue dados.


```python
#Consulta os dados da tabela *tipounidade*
tabledata <- dbReadTable(con,"tipounidade")
tabledata
```

**OBS:** Veja que o resultado do comando acima demonstra que a tabela 'tipounidade' possue alguns dados.


```python
#Para executar um comando SQL execute:
#dbSendQuery(nome-da-conexao,"comando")

# Vamos inserir uma nova linha na tabela tipounidade
# Cria o comando e salva na variável query
query <-  "INSERT INTO tipounidade(idTipoUnidade,dscTipoUnidade) VALUES(7,'Loft');"

results <- dbSendQuery(con,query)
print(results)

# Limpa resultados
dbClearResult(results)
```


```python
**OBS 1:** Caso ocorra o erro: *Error: Duplicate entry '6' for key 'tipounidade.PRIMARY' [1062]*

Isso significa que você violou a chave primária, ou seja, tentou inserir uma chave que já existe. Confira o valor da chave que esta inserindo, altere, e execute novamente.

**OBS 2:** Caso ocorra o erro: *Error: Column count doesn't match value count at row 1 [1136]*
Isso significa que você esta inserindo dados não compatíveis com a definição da tabela.

```


```python
#Consulta os dados da tabela *tipounidade*
tabledata <- dbReadTable(con,"tipounidade")
tabledata
```


```python
id <- 8
desc <- 'Chácara'

query <-  paste("INSERT INTO tipounidade(idTipoUnidade,dscTipoUnidade) VALUES(",id,",'",desc,"');",sep='')

results <- dbSendQuery(con,query)
print(results)

# Limpa resultados
dbClearResult(results)
```


```python
#Consulta os dados da tabela *tipounidade*
tabledata <- dbReadTable(con,"tipounidade")
tabledata
```

##### Instalar o pacote xlsx


```python
install.packages('xlsx')
```

##### Importar o pacote xlsx


```python
#Importa pacote xlsx se ele ainda não foi carregado
if(!"xlsx" %in% (.packages())){require(xlsx)}
```


```python
#Antes de excutar esta célula, garanta que o caminho do arquivo estados.xlsx esteja correto.

filename <- "E:\igti\CientistadeDados\Módulo 2\Trabalho Prático do Módulo 2\arquivoscomplementaresTrabalhoPratico/estados.xlsx"
print(filename)

insertdata <- read.xlsx(filename, sheetIndex=1, header=TRUE,encoding="UTF-8")
print("Lista de estados existentes no arquivo:")
insertdata
```

**OBS:** As colunas da tabela estado são: *CodEstadoIBGE,NomeEstado,SiglaEstado,Regiao*



```python
dbWriteTable(con,'estado',insertdata,append = TRUE)
```


```python
#Consulta os dados da tabela *estado*
results <- dbReadTable(con,"estado")
results
```


```python
query <- "SELECT * FROM estado;"

results <- dbSendQuery(con,query)
results
```

**Obs:** O retorno do comando *dbSendQuery* indica que se o comando SQL passado para a variável *query* foi executado com sucesso ou não.


```python
# Limpa resultados
dbClearResult(results)

results <- dbGetQuery(con,query)
results
```


```python
# Verifique se o caminho do arquivo existe.

#Salvar o resultado da query no arquivo CSV
write.csv(results,"E:\igti\CientistadeDados\Módulo 2\Trabalho Prático do Módulo 2\arquivoscomplementaresTrabalhoPratico/estadosDB.csv",row.names=FALSE,quote=FALSE)

#Realizar o commit
#dbCommit(con)
```


```python
# Desconectar do banco de dados
dbDisconnect(con)
```

## A partir daqui você deve alterar seu notebook conforme orientações da atividade 8 do enunciado do trabalho prático.

Nas células abaixo foram deixadas algumas dicas para você seguir.

##### 1º) Importar as bibliotecas RMariaDB 


```python
#Se você já importou anteriormente e não resetou seu kernel, não será necessário importar

```

##### 2º) Fazer a conexão com seu banco de dados


```python

```

##### 3º) Abrir o arquivo 'caracteristicasgerais.csv'


```python

```

##### 4º) Inserir dados na tabela 'caracteristicasgerais'


```python

```

##### 5º) Consultar a tabela 'caracteristicasgerais' para verificar se os dados foram inseridos corretamente.


```python

```

##### Fim!


```python

```
