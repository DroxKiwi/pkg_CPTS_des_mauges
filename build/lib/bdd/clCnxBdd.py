import psycopg2.extras
import psycopg2

class cnx(object):

    @staticmethod
    def cpts_ps(debug=True):
        if debug == True:
            return psycopg2.connect(host='localhost', dbname='cpts', user='postgres', password='toor', port=5437)
        else:
            return psycopg2.connect(host='localhost', dbname='cpts', user='postgres', password='toor', port=5437)
