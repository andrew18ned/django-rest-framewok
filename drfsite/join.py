import sqlite3

# absolute url to file
connection_to_db = sqlite3.connect(r'/home/andrew17/Документы/django-rest-framewok/drfsite/db.sqlite3')
cursor = connection_to_db.cursor() # for CRUD 

# write query to DB
# SELECT name_fields_table1, name_table2.name_field FROM name_table1 LEFT JOIN name_table_2 ON по яких спільних понях вони будуть об*єднані;
cursor.execute('''SELECT title, women_category.name FROM women_women 
                    LEFT JOIN women_category 
                        ON women_category.id=women_women.id;''')

result = cursor.fetchall() # one or all record
print(result)