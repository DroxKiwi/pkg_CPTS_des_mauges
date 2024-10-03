#import pymysql
#import pymssql
#import pyodbc
#import sqlite3
import psycopg
import psycopg2.extras

class CNX():

    @staticmethod
    def cpts_ps(debug=True):
        if debug == True:
            return psycopg.connect(host='localhost', dbname='cpts', user='postgres', password='toor', port=5437)
        else:
            return psycopg.connect(host='localhost', dbname='cpts', user='postgres', password='toor', port=5437)
        
    @staticmethod
    def postgresDictCursor():
        return psycopg2.extras.RealDictCursor
