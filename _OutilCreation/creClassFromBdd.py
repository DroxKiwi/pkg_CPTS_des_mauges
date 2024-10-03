# -*- coding: utf-8 -*-
from ntpath import join
import sys
import os
import inspect
#import petl as etl
import clCnxBdd as cnx

if os.name == "nt":
    splStrg = "\\"
else:
    splStrg = "/"

repSrc = os.path.realpath(os.path.abspath(
    os.path.split(inspect.getfile(inspect.currentframe()))[0]))
srep = os.path.realpath(os.path.abspath(os.path.split(
    inspect.getfile(inspect.currentframe()))[0])).split(splStrg)
rep = splStrg.join(srep[0:len(srep)-1])
sys.path.append(rep)
nbrLi = 0
liFic = []
liImport = []
liClass = []
strLstCol = ""
# region cnx, var Glob

nomBase = 'cpts'
nomRep = f'db{nomBase}'
nomImport = f'Bdd.db{nomBase}.{nomBase}'
cnxString = 'cnx.cpts'
nomTbl = ''
oCnx = cnx.CNX.cpts_ps()
typeBdd = "postgres"

# endregion


def main():
    global nomTbl
    global oCnx
    global liFic
    global liClas
    if typeBdd == "MSSQL":
        sqlCol = "select DISTINCT TABLE_NAME from information_schema.columns  ORDER BY TABLE_NAME"
        # sqlCol = "SELECT T.name as TABLE_NAME FROM sys.dm_db_partition_stats as PS JOIN sys.tables AS T ON PS.object_id = T.object_id WHERE PS.index_id BETWEEN 0 AND 1 AND ps.row_count > 90 ORDER BY T.name;"
        cursor = oCnx.cursor()
    if typeBdd == "postgres":
        sqlCol = "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE' ORDER BY table_name;"
        cursor = oCnx.cursor()
    else:
        # MYSQL
        sqlCol = f"SELECT DISTINCT table_name as TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA = '{nomBase}' ORDER BY table_name"
        cursor = oCnx.cursor(cnx.CNX.mysqlDictCursor())  # MYSQL
    cursor.execute(sqlCol)
    rows = cursor.fetchall()
    for r in rows:
        liFic = []
        # Vérifier pourquoi ça marche pas avec un appel de nom de tuple
        if typeBdd == "postgres":
            nomTbl = r[0]
        else:
            nomTbl = r[0]
        creGlobClass()
        creFile(True, True, True, True)
    liImport.append('from . clCnxBdd import cnx')
    liImport.append("")
    # liImport.append(f"oCnx = {cnxString}()")
    # liImport.append("")
    liImport.extend(liClass)

    pFile = repSrc + splStrg + 'fichierClass' + splStrg + nomBase + '.py'
    f = open(pFile, 'w')
    for l in liImport:
        f.write('\n' + l)
    f.close()


def creGlobClass():
    global liImport
    global liClass
    liImport.append(f"from . {nomRep}.{nomBase}_{nomTbl} import {nomTbl}")
    liClass.append(f"class t{nomTbl}({nomTbl}):")
    liClass.append(f"\tdef __init__(self, pDebug=False):")
    liClass.append(f"\t\toCnx = {cnxString}(pDebug)")
    liClass.append(f"\t\tsuper().__init__(oCnx)")
    liClass.append("")


def creFile(pIns, pUpd, pDel, preadId):
    try:
        global nbrLi
        global strLstCol
        global nomTbl
        global nomBase
        global oCnx

        if typeBdd == "MSSQL":
            sqlCol = f"select TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, ORDINAL_POSITION from information_schema.columns where table_name = '{nomTbl}' ORDER BY ORDINAL_POSITION"
            cursor = oCnx.cursor(as_dict=True)
        if typeBdd == "postgres":
            sqlCol = f"select TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, ORDINAL_POSITION from information_schema.columns where table_name = '{nomTbl}' ORDER BY ORDINAL_POSITION"
            cursor = oCnx.cursor()  # MYSQL
        else:
            # MYSQL
            sqlCol = f"SELECT TABLE_SCHEMA as TABLE_CATALOG, '{nomBase}' as TABLE_SCHEMA, table_name as TABLE_NAME, column_name as COLUMN_NAME, ordinal_position as ORDINAL_POSITION FROM information_schema.columns where table_name = '{nomTbl}' ORDER BY ORDINAL_POSITION"
            cursor = oCnx.cursor(cnx.CNX.mysqlDictCursor())  # MYSQL

        cursor.execute(sqlCol)
        rows = cursor.fetchall()

        print(rows)
        nomBase = rows[0][0]
        # nomTbl = rows[0][0]

        nbrLi = len(rows)
        strLstCol = ', '.join(list(map(colListStr, rows)))
        print(strLstCol)

        Entete()
        o = list(map(creObj, rows))

        if pIns == True:
            u = list(map(creUpd, rows))
        else:
            ue = list(map(creUpdEmpty, rows))

        if pUpd == True:
            i = list(map(creIns, rows))
        else:
            ie = list(map(creInsEmpty, rows))

        if pDel == True:
            d = list(map(creDel, rows))
        else:
            de = list(map(creDelEmpty, rows))

        if preadId == True:
            s = list(map(creReadId, rows))
        else:
            se = list(map(creReadIdEmpty, rows))

        m = list(map(creReadWhere, rows))

        pFile = repSrc + splStrg + 'fichierClass' + \
            splStrg + nomBase + "_" + nomTbl + '.py'
        f = open(pFile, 'w')
        for l in liFic:
            f.write('\n' + l)
        f.close()

    except Exception as err:
        print(err)


def colListStr(pRow):
    lstCol = []
    #lstCol.append(pRow[3])
    lstCol.append(pRow[3])
    return pRow[3]


def Entete():
    global liFic
    global nomTbl
    liFic.append('# -*- coding: utf-8 -*-')
    if typeBdd == "MYSQL":
        liFic.append(f'from pymysql.cursors import DictCursor')
    liFic.append('')
    liFic.append(f'class {nomTbl}(object):')


def creObj(pRow):
    global liFic
    col = pRow[3]
    tbl = pRow[0]
    pos = pRow[4]
    if pos == 1:
        liFic.append(f'\tdef __init__(self, pCnx):')
        liFic.append(f'\t\tself.oCnx = pCnx')
        liFic.append(f'\t\tself.{col} = None')
    elif pos < nbrLi:
        liFic.append(f'\t\tself.{col} = None')
    elif pos == nbrLi:
        liFic.append(f'\t\tself.{col} = None')
        liFic.append('')


def creUpd(pRow):
    global liFic
    col = pRow[3]
    tbl = pRow[0]
    pos = pRow[4]
    sch = pRow[1]
    if pos == 1:
        liFic.append(f'\tdef update(p{tbl}_o):')
        liFic.append(f'\t\t_o{tbl} = p{tbl}_o')
        if typeBdd == "MSSQL":
            liFic.append(f'\t\t_upSQL = ("UPDATE [{sch}].[{tbl}] SET "')
        else:
            liFic.append(f'\t\t_upSQL = ("UPDATE `{sch}`.`{tbl}` SET "')
    elif pos < nbrLi:
        liFic.append('\t\t"{} = " + ("null" if _o{}.{} == {} else  ("{}" + str(_o{}.{}) + "{}")) + ", "'.format(
            col, tbl, col, "None", "'", tbl, col, "'"))
    elif pos == nbrLi:
        liFic.append('\t\t"{} = " + ("null" if _o{}.{} == {} else  ("{}" + str(_o{}.{}) + "{}")) + " "'.format(
            col, tbl, col, "None", "'", tbl, col, "'"))
        liFic.append('\t\t"WHERE ID = ID;")')
        liFic.append('\t\treturn _upSQL')
        liFic.append('')


def creUpdEmpty(pRow):
    global liFic
    pos = pRow[4]
    if pos == 1:
        liFic.append(f'\tdef update():')
        liFic.append(f'\t\treturn ""')
        liFic.append('')


def creIns(pRow):
    global liFic
    col = pRow[3]
    tbl = pRow[0]
    pos = pRow[4]
    sch = pRow[1]
    if pos == 1:
        liFic.append(f'\tdef insert(p{tbl}_o):')
        liFic.append(f'\t\t_o{tbl} = p{tbl}_o')
        if typeBdd == "MSSQL":
            liFic.append(
                f'\t\t_insSQL = ("INSERT INTO [{sch}].[{tbl}] ({strLstCol}) "')
        else:
            liFic.append(
                f'\t\t_insSQL = ("INSERT INTO `{sch}`.`{tbl}` ({strLstCol}) "')
        liFic.append('\t\t"VALUES ("')
    elif pos < nbrLi:
        liFic.append(
            f'\t\t + (\'null\' if _o{tbl}.{col} == None else "\'" + str(_o{tbl}.{col}) + "\'") + ", "')
    elif pos == nbrLi:
        liFic.append(
            f'\t\t + (\'null\' if _o{tbl}.{col} == None else "\'" + str(_o{tbl}.{col}) + "\')"))')
        liFic.append('\t\treturn _insSQL')
        liFic.append('')


def creInsEmpty(pRow):
    global liFic
    pos = pRow[4]
    if pos == 1:
        liFic.append(f'\tdef insert():')
        liFic.append(f'\t\treturn ""')
        liFic.append('')


def creReadId(pRow):
    global liFic
    col = pRow[3]
    tbl = pRow[0]
    pos = pRow[4]
    sch = pRow[1]
    if pos == 1:
        liFic.append(f'\tdef readId(self, pID):')
        if typeBdd == "MSSQL":
            liFic.append(
                f'\t\t_sSql = ("SELECT {strLstCol} FROM [{sch}].[{tbl}] WHERE ID = \'" + pID + "\'")')
            liFic.append(f'\t\tcursor = self.oCnx.cursor(as_dict=True)')
        if typeBdd == "postgres":
            liFic.append(
                f'\t\t_sSql = ("SELECT {strLstCol} FROM [{sch}].[{tbl}] WHERE ID = \'" + pID + "\'")')
            liFic.append(f'\t\tcursor = self.oCnx.cursor(as_dict=True)')
        else:
            liFic.append(
                f'\t\t_sSql = ("SELECT {strLstCol} FROM `{sch}`.`{tbl}` WHERE ID = \'" + pID + "\'")')
            liFic.append(f'\t\tcursor = self.oCnx.cursor(DictCursor)')
        liFic.append('\t\tcursor.execute(_sSql)')
        liFic.append('\t\trow = cursor.fetchone()')
        liFic.append(f'\t\to{tbl} = {tbl}(self.oCnx)')
        liFic.append(f'\t\to{tbl}.{col} = row[\'{col}\']')
    elif pos < nbrLi:
        liFic.append(f'\t\to{tbl}.{col} = row[\'{col}\']')
    elif pos == nbrLi:
        liFic.append(f'\t\to{tbl}.{col} = row[\'{col}\']')
        liFic.append(f'\t\treturn o{tbl}')
        liFic.append('')


def creReadIdEmpty(pRow):
    global liFic
    pos = pRow[4]
    if pos == 1:
        liFic.append(f'\tdef readId():')
        liFic.append(f'\t\treturn ""')
        liFic.append('')


def creReadWhere(pRow):
    global liFic
    col = pRow[3]
    tbl = pRow[0]
    pos = pRow[4]
    sch = pRow[1]
    if pos == 1:
        liFic.append(f'\tdef readWhere(self, pWhere):')
        if typeBdd == "MSSQL":
            liFic.append(
                f'\t\t_sSql = ("SELECT {strLstCol} FROM [{sch}].[{tbl}] WHERE " + pWhere )')
            liFic.append(f'\t\tcursor = self.oCnx.cursor(as_dict=True)')
        if typeBdd == "postgres":
            liFic.append(
                f'\t\t_sSql = ("SELECT {strLstCol} FROM [{sch}].[{tbl}] WHERE " + pWhere )')
            liFic.append(f'\t\tcursor = self.oCnx.cursor(as_dict=True)')
        else:
            liFic.append(
                f'\t\t_sSql = ("SELECT {strLstCol} FROM `{sch}`.`{tbl}` WHERE " + pWhere )')
            liFic.append(f'\t\tcursor = self.oCnx.cursor(DictCursor)')
        liFic.append('\t\tcursor.execute(_sSql)')
        liFic.append('\t\trows = cursor.fetchall()')
        liFic.append(f'\t\tlst{tbl} = []')
        liFic.append('\t\tfor row in rows:')
        liFic.append(f'\t\t\to{tbl} = {tbl}(self.oCnx)')
        liFic.append(f'\t\t\to{tbl}.{col} = row[\'{col}\']')
    elif pos < nbrLi:
        liFic.append(f'\t\t\to{tbl}.{col} = row[\'{col}\']')
    elif pos == nbrLi:
        liFic.append(f'\t\t\to{tbl}.{col} = row[\'{col}\']')
        liFic.append(f'\t\t\tlst{tbl}.append(o{tbl})')
        liFic.append(f'\t\treturn lst{tbl}')
        liFic.append('')


def creDel(pRow):
    global liFic
    pos = pRow[4]
    if pos == 1:
        liFic.append(f'\tdef delete():')
        liFic.append(f'\t\treturn ""')
        liFic.append('')


def creDelEmpty(pRow):
    global liFic
    pos = pRow[4]
    if pos == 1:
        liFic.append(f'\tdef delete():')
        liFic.append(f'\t\treturn ""')
        liFic.append('')


if __name__ == "__main__":
    main()
