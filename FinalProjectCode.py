import wikipedia
import mysql.connector

mydb = mysql.connector.connect(host='sql9.freemysqlhosting.net', user='sql9365318', passwd='JeklLWZw9Y', database='sql9365318')
print(mydb)

if (mydb):
    print("Connection Successful")
else:
    print("Connection Unsuccessful")

mycursor = mydb.cursor()

#sql = "DROP TABLE testJean"
#mycursor.execute(sql)

#sql = "DELETE FROM testJean where actorid = '17'"
#mycursor.execute(sql)

#sql = "UPDATE testJean SET actorid = '5' WHERE actorid = '9'"
#mycursor.execute(sql)

#mycursor.execute("SELECT * FROM testJean")
#for x in mycursor:
    #print(x)

#mycursor.execute("ALTER TABLE testJean ADD COLUMN imdbID VARCHAR(255)")

#mycursor.execute("CREATE TABLE testJean (actorid INT AUTO_INCREMENT PRIMARY KEY, actorname VARCHAR(255), charname VARCHAR(255))")


#sql = "INSERT INTO testJean (actorname, charname, actorage, DOB, Mdistrict, HomeState, NumberOfSib, imdbID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#val = ("Jennifer Lawrence", "Katniss Everdeen", "30", "8/15/1990", "District 12", "Massachusetts", "2", "tt1951266")
#val1 = ("Josh Hutcherson", "Peeta Mellark", "28", "10/12/1992", "District 12", "Massachusetts", "1", "tt1951266")
#val2 = ("Liam Hemsworth", "Gale Hawthorne", "30", "1/13/1990", "District 12", "Massachusetts", "2", "tt1951265")
#val3 = ("Woody Harrelson", "Haymitch Abernathy", "59", "7/23/1961", "District 12", "Massachusetts", "2", "tt1951266")
#val4 = ("Elizabeth Banks", "Effie Trinket", "46", "2/10/1974", "District 12", "Massachusetts", "3", "tt1951266")
#mycursor.execute(sql, val2)

#mydb.commit()
#print(mycursor.rowcount, "Record Inserted")
mycursor.execute("SELECT * FROM testJean")
for x in mycursor:
    print(x)


#print(wikipedia.summary("The Hunger Games(film)", sentences=3))
#print()
#print(wikipedia.summary("The Hunger Games: Catching Fire", sentences=4))
#print()
#print(wikipedia.summary("The Hunger Games: Mockingjay - Part 1", sentences=3))
#print()
#print(wikipedia.summary("The Hunger Games: Mockingjay - Part 2", sentences=4))


#actor = wikipedia.summary("The Hunger Games(film)")

print(wikipedia.summary("The Hunger Games (film series)", sentences=3))

#print(wikipedia.page("List of The Hunger Games characters").content)

#print(wikipedia.page("List of The Hunger Games cast members").content)