# mysql-basics
A basic python file to interact with your mysql-database

# Get started
download the folder utils and put it wherever you want
open your command shell and type:
`pip install mysql-connector`

Now you can use this like in this example:

```python
from utils import database

connection = database.create_db_connection('YOUR_HOST_NAME', 'YOUR_USERNAME', 'YOUR_PW', 'YOUR_DATABASE_NAME')

table_name = 'test'
columns = 'name TEXT, email TEXT, id INT PRIMARY KEY'

database.create_table(connection, 'YOUR_DATABASE_NAME', table_name, columns)

sql = 'INSERT INTO test (name, email, id) VALUES ('test_user_name', 'test@gmail.com' 1)'

database.execute_query(connection, sql)
```




# Functions
all functions implemented in the file


**create_server_connection(host_name, user_name, user_password)**

*enter your host_name, the username for your mysql aswell as his password (likly not really hardcoded into this but more to be in a config.py file)*

```python
from utils import database

connection = database.create_server_connection(host_name, user_name, user_password)
```


**create_db_connection(host_name, user_name, user_password, db_name)**

*enter your host_name, the username for your mysql aswell as his password and the name of the database you want to connect to*

```python
from utils import database

connection = database.create_db_connection(host_name, user_name, user_password, db_name)
```


**create_database(connection, name)**

**_requires you to create a connection first_**

*enter your connection and your new database name*

```python
from utils import database

connection = database.create_server_connection(host_name, user_name, user_password)

database.create_database(connection, 'test')
```


**create_table(connection, db_name, table_name, parameters)**

**_requires you to create a connection first_**

*enter your connection, the database you want to create the table in, the tables name and his parameters*

```python
from utils import database

connection = database.create_server_connection(host_name, user_name, user_password)

table_name = 'test'
columns = 'name TEXT, email TEXT, id INT PRIMARY KEY'

database.create_table(connection, 'YOUR_DATABASE_NAME', table_name, columns)
```


**execute_query(connection, query)**

**_requires you to create a connection to a database first_**

*enter your connection and your query (the thing you want to execute)*

```python
from utils import database

connection = database.create_server_connection(host_name, user_name, user_password)

sql = 'INSERT INTO test (name, email, id) VALUES ('test_user_name', 'test@gmail.com' 0);'

database.execute_query(connection, sql)
```


**execute_list_query(connection, query, values)**

**_requires you to create a connection to a database first_**

*enter your connection your query and the values you want input. This is ment to let you insert many rows of content at once*

```python
from utils import database

connection = database.create_db_connection('YOUR_HOST_NAME', 'YOUR_USERNAME', 'YOUR_PW', 'test')


vals = [['test1', 'test1@gmail.com', 1], ['test2', 'test2@gmail.com', 2], ['test3', 'test3@gmail.com', 3]]

sql = 'INSERT INTO test (name, email, id) VALUES (%s, %s, %s);'

database.execute_list_query(connection, sql, vals)
```


**read_query(connection, query, print_succes=True)**

**_requires you to create a connection to a database first_**

*enter your connection, your query and if you don't want to print that the read_query was successfull add a last specifier False*

```python
from utils import database

connection = database.create_db_connection('YOUR_HOST_NAME', 'YOUR_USERNAME', 'YOUR_PW', 'test')


sql = 'SELECT * FROM test WHERE id=1;'

#with printing the succes
result = database.read_query(connection, sql)

#and without printing success
result = database.read_query(connection, sql, False)


print(result)
```
