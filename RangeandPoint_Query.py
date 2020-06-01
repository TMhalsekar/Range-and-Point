
import psycopg2
import os
import sys
# Donot close the connection inside this file i.e. do not perform openconnection.close()
def RangeQuery(ratingMinValue, ratingMaxValue, openconnection, outputPath):
    rangep = 'rangeratingspart'
    roundR = 'roundrobinratingspart'
    file = open(outputPath, "w+")

    cur = openconnection.cursor()
    cur.execute("select count(*) from information_schema.tables where table_name LIKE '" + rangep + "%';")
    openconnection.commit()

    range_part = cur.fetchone()[0]
    for i in range(0, range_part):
        part = rangep + str(i)
        cur.execute("select * from " + part + " where Rating >= " + str(ratingMinValue) + " and Rating <= " + str(
            ratingMaxValue) + ";")
        openconnection.commit()
        values = cur.fetchall()

        for each in values:
            temp = str(part) + ',' + str(each[0]) + ',' + str(each[1]) + ',' + str(each[2]) + '\n'
            file.write(temp)


    cur.execute("select count(*) from information_schema.tables where table_name like '" + roundR + "%';")
    openconnection.commit()

    rrobin_part = cur.fetchone()[0]
    for i in range(0, rrobin_part):
        part = roundR + str(i)
        cur.execute("select * from " + part + " where Rating >= " + str(ratingMinValue) + " AND Rating <= " + str(
            ratingMaxValue) + ";")
        openconnection.commit()
        values = cur.fetchall()
        for each in values:
            temp = str(part) + ',' + str(each[0]) + ',' + str(each[1]) + ',' + str(each[2]) + '\n'
            file.write(temp)
    file.close()
     #Remove this once you are done with implementation

def PointQuery(ratingValue, openconnection, outputPath):
    rangeP = 'rangeratingspart'
    roundR = 'roundrobinratingspart'
    file = open(outputPath, "w+")

    cur = openconnection.cursor()
    cur.execute("select count(*) from information_schema.tables where table_name like '" + rangeP + "%';")
    openconnection.commit()

    range_part = cur.fetchone()[0]
    for i in range(0, range_part):
        part = rangeP + str(i)
        cur.execute('select * from ' + part + ' where Rating = ' + str(ratingValue) + ';')
        openconnection.commit()
        values = cur.fetchall()
        for each in values:
            temp = str(part) + ',' + str(each[0]) + ',' + str(each[1]) + ',' + str(each[2]) + '\n'
            file.write(temp)

    cur.execute("select count(*) from information_schema.tables where table_name like '" + roundR + "%';")
    openconnection.commit()

    rrobin_part = cur.fetchone()[0]
    for i in range(0, rrobin_part):
        part = roundR + str(i)
        cur.execute('select * from ' + part + ' where Rating = ' + str(ratingValue) + ';')
        openconnection.commit()
        values = cur.fetchall()
        for each in values:
            temp = str(part) + ',' + str(each[0]) + ',' + str(each[1]) + ',' + str(each[2]) + '\n'
            file.write(temp)
    file.close()
    #Implement PointQuery Here.

     # Remove this once you are done with implementation
