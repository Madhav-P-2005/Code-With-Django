'''

Django-Learning.py/populate_db.py

⭐) Managing Data with SQLite and Django ORM

=> Connects to a SQLite database and retrieves data from it :- 

1) Database Setup :-  The populate_db.py script will create a table named items and insert sample data with the columns id and name.

2) Data Retrieval :-  The Django view get_items will establish a connection to the database, retrieve data, and return it via an HTTP response.

3) URL Configuration :-  The URL /get-items/ is mapped to the get_items view and can be accessed to see the items.


⭐) To populate the database (Run the population script (one-time setup):) :-   python populate_db.py   then  run the manage.py runserver .   

'''


import sqlite3
import os
# Define the path to the database file
db_path = os.path.join(os.path.dirname(__file__) , 'db.sqlite3')
# Connect to the SQLite database
connection = sqlite3.connect(db_path)
try :
    # Create table if it doesn't exit
    raw_query = 'create table if not exists items(id integer primary key, name text)'
    connection.execute(raw_query)

    # Add items to the database
    for i in range(5):
        raw_query = f"Insert into items (name) values('item{i}')"
        connection.execute(raw_query)
    connection.commit()
    '''
    Need to try :- 
    In SQL, you can use the LIKE operator to match patterns: WHERE name LIKE 'g%' will match any string that starts with 'g'
        
        raw_query = "SELECT * FROM items WHERE name LIKE 'h%'"
    
    '''
finally:
    # Close the database connection
    connection.close()



'''

# http://127.0.0.1:8000/get-items/ :- (Output)

(1, 'item0')(2, 'item1')(3, 'item2')(4, 'item3')(5, 'item4')(6, 'item0')(7, 'item1')(8, 'item2')(9, 'item3')(10, 'item4')(11, 'item0')(12, 'item1')(13, 'item2')(14, 'item3')(15, 'item4')

'''