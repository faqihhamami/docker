
#best practice python read postgres
import psycopg2

try:
   connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="172.17.0.2",
                                  port="5432",
                                  database="postgres")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select * from playground"

   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from playground using cursor.fetchall")
   mobile_records = cursor.fetchall() 
   
   print("Print each row and it's columns values")
   for row in mobile_records:
       print("equip_id = ", row[0], )
       print("type = ", row[1])
       print("color = ", row[2], )
       print("location = ", row[3])
       print("install_date  = ", row[4], "\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
