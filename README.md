# Documentation Package

## Sommaire 

- 1 Générer les tables
- 2 Modification du code généré
- 3 Ajout des nouvelles tables aux classes
- 4 Versionning
- 5 Génération de la Wheel
- 6 Déploiement en local
- 7 Déploiement en live
- ADDENDUM Ajouter une base au package 

## 1 Générer les tables

Se diriger dans *_OutilCreation\creClassFromBdd.py*, décommenter la configuration de base correspondante à la base qu'on veut atteindre, et bien penser à commenter les autres.

Exemple :
```py

...

"""
nomBase = 'projeqtor'
nomRep = f'db{nomBase}'
nomImport = f'Bdd.db{nomBase}.{nomBase}'
cnxString = 'cnx.projeqtor_my'
nomTbl = ''
oCnx = cnx.CNX.projeqtor_my()
typeBdd = "MYSQL"
"""

#"""
nomBase = 'SALESKY'
nomRep = f'db{nomBase}'
nomImport = f'Bdd.db{nomBase}.{nomBase}'
cnxString = 'cnx.Salesky_ms'
nomTbl = ''
oCnx = cnx.CNX.Salesky_ms()
typeBdd = "MSSQL"
#"""

"""
nomBase = 'BPW'
nomRep = f'db{nomBase}'
nomImport = f'Bdd.db{nomBase}.{nomBase}'
cnxString = 'cnx.BPW_ms'
nomTbl = ''
oCnx = cnx.CNX.BPW_ms()
typeBdd = "MSSQL"
"""

...

```

Lancer le script.

Récuperer les fichier générées dans le répertoire *_OutilCreation\fichierClass*. Chaque nom de fichier sont l'équivalent du nom de la table en base. Les déplacer dans le répertoire correspondant à la base :

Exemple pour dbSALESKY : 

*SaleskyBdd\dbSALESKY*

## 2 Modification du code généré

Ouvrir le fichier de la table généré, et modifier les requêtes suivante :

UPDATE : 
Insérer l'id dans le where 

```py
    ... code généré
	def update(padm_applist_o):
		_oadm_applist = padm_applist_o
		_upSQL = ("UPDATE [dbo].[adm_applist] SET "
		"appNom = " + ("null" if _oadm_applist.appNom == None else  ("'" + str(_oadm_applist.appNom) + "'")) + ", "
		"appMode = " + ("null" if _oadm_applist.appMode == None else  ("'" + str(_oadm_applist.appMode) + "'")) + ", "
		"appDetails = " + ("null" if _oadm_applist.appDetails == None else  ("'" + str(_oadm_applist.appDetails) + "'")) + ", "
		"tecTimeInsert = " + ("null" if _oadm_applist.tecTimeInsert == None else  ("'" + str(_oadm_applist.tecTimeInsert) + "'")) + " "
		"WHERE ID = ID;")
		return _upSQL

    ... code modifié
	def update(padm_applist_o):
		_oadm_applist = padm_applist_o
		_upSQL = ("UPDATE [dbo].[adm_applist] SET "
		"appNom = " + ("null" if _oadm_applist.appNom == None else  ("'" + str(_oadm_applist.appNom) + "'")) + ", "
		"appMode = " + ("null" if _oadm_applist.appMode == None else  ("'" + str(_oadm_applist.appMode) + "'")) + ", "
		"appDetails = " + ("null" if _oadm_applist.appDetails == None else  ("'" + str(_oadm_applist.appDetails) + "'")) + " "
		"WHERE idAppList = '"+str(_oadm_applist.idAppList)+"';")
		return _upSQL
```

INSERT :
Supprimer les COLONNES auto-générés, supprimer l'identifiant dans les noms de COLONNES, ajouter l'identifiant dans les VALUES si non auto-généré.

```py
... code généré 
	def insert(padm_applist_o):
		_oadm_applist = padm_applist_o
		_insSQL = ("INSERT INTO [dbo].[adm_applist] (idAppList, appNom, appMode, appDetails, tecTimeInsert) "
		"VALUES ("
		 + ('null' if _oadm_applist.appNom == None else "'" + str(_oadm_applist.appNom) + "'") + ", "
		 + ('null' if _oadm_applist.appMode == None else "'" + str(_oadm_applist.appMode) + "'") + ", "
		 + ('null' if _oadm_applist.appDetails == None else "'" + str(_oadm_applist.appDetails) + "'") + ", "
		 + ('null' if _oadm_applist.tecTimeInsert == None else "'" + str(_oadm_applist.tecTimeInsert) + "')"))
		return _insSQL

... code modifié
	def insert(padm_applist_o):
		_oadm_applist = padm_applist_o
		_insSQL = ("INSERT INTO [dbo].[adm_applist] (appNom, appMode, appDetails) "
		"VALUES ("
		 + ('null' if _oadm_applist.appNom == None else "'" + str(_oadm_applist.appNom) + "'") + ", "
		 + ('null' if _oadm_applist.appMode == None else "'" + str(_oadm_applist.appMode) + "'") + ", "
		 + ('null' if _oadm_applist.appDetails == None else "'" + str(_oadm_applist.appDetails) + "'") + ")")
		return _insSQL
```

READ ID :
    Id à corriger dans le where, et supprimer les valeurs purements techniques si nécessaire.

```py
... code généré
	def readId(self, pID):
		_sSql = ("SELECT idAppList, appNom, appMode, appDetails, tecTimeInsert FROM [dbo].[adm_applist] WHERE ID = '" + pID + "'")
		cursor = self.oCnx.cursor(as_dict=True)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		oadm_applist = adm_applist(self.oCnx)
		oadm_applist.idAppList = row['idAppList']
		oadm_applist.appNom = row['appNom']
		oadm_applist.appMode = row['appMode']
		oadm_applist.appDetails = row['appDetails']
		oadm_applist.tecTimeInsert = row['tecTimeInsert']
		return oadm_applist

... code modifié 
	def readId(self, pID):
		_sSql = ("SELECT idAppList, appNom, appMode, appDetails FROM [dbo].[adm_applist] WHERE idAppList = '" + str(pID) + "'")
		cursor = self.oCnx.cursor(as_dict=True)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		oadm_applist = adm_applist(self.oCnx)
		oadm_applist.idAppList = row['idAppList']
		oadm_applist.appNom = row['appNom']
		oadm_applist.appMode = row['appMode']
		oadm_applist.appDetails = row['appDetails']
		return oadm_applist
```

READ WHERE :
Supprimer le tecTimeInsert ou autre valeurs purements techniques

```py
... code généré
	def readWhere(self, pWhere):
		_sSql = ("SELECT idAppList, appNom, appMode, appDetails, tecTimeInsert FROM [dbo].[adm_applist] WHERE " + pWhere )
		cursor = self.oCnx.cursor(as_dict=True)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		lstadm_applist = []
		for row in rows:
			oadm_applist = adm_applist(self.oCnx)
			oadm_applist.idAppList = row['idAppList']
			oadm_applist.appNom = row['appNom']
			oadm_applist.appMode = row['appMode']
			oadm_applist.appDetails = row['appDetails']
			oadm_applist.tecTimeInsert = row['tecTimeInsert']
			lstadm_applist.append(oadm_applist)
		return lstadm_applist

... code modifié
	def readWhere(self, pWhere):
		_sSql = ("SELECT idAppList, appNom, appMode, appDetails FROM [dbo].[adm_applist] WHERE " + pWhere )
		cursor = self.oCnx.cursor(as_dict=True)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		lstadm_applist = []
		for row in rows:
			oadm_applist = adm_applist(self.oCnx)
			oadm_applist.idAppList = row['idAppList']
			oadm_applist.appNom = row['appNom']
			oadm_applist.appMode = row['appMode']
			oadm_applist.appDetails = row['appDetails']
			lstadm_applist.append(oadm_applist)
		return lstadm_applist 
```

## 3 Ajout des nouvelles tables aux classes

Ouvrir le fichier correspondant à la table sur laquelles on travaille :

Exemple pour la base SALESKY

**SaleskyBdd\SALESKY.py**

Ajouter l'import et la définition de classe correspondant. Le nom de la classe doit commencer par un "t" suivit du nom de la table.

```py
    ...

from . dbSALESKY.SALESKY_adm_applist import adm_applist

    ...

class tadm_applist(adm_applist):
	def __init__(self, pDebug=False):
		oCnx = cnx.Salesky_ms(pDebug)
		super().__init__(oCnx)

    ...
```

## 4 Versionning

Dans le cas où une table est ajoutée ou supprimée, incrémenter la version du package.

3 fichier à modifier :

**./setup.py**

```py
    version='1.1.8', (à modifier)
```

**./Dockerfile**

```dockerfile
    FROM python:3.8-alpine
    RUN mkdir /pkg
    WORKDIR /pkg

    (à modifier)
    ADD SaleskyDal-1.1.8-py3-none-any.whl /pkg 

    RUN apk add --no-cache --virtual .build-deps mariadb-dev freetds-dev freetds g++ gcc unixodbc-dev zlib-dev libjpeg jpeg-dev libffi-dev py3-requests
    RUN /usr/local/bin/python -m pip install --upgrade pip
    RUN pip3 install cython==0.29.35
    RUN pip3 install --no-build-isolation pymssql==2.1.5

    (à modifier)
    RUN pip3 install SaleskyDal-1.1.8-py3-none-any.whl

    CMD ["ls"]
```

**./docker-compose.yml**

```yml
version: '3'
services:
  pkg:
    build:
      context: .
      dockerfile: Dockerfile
    image: salesky/pkgsaleskydal:1.1.8 (à modifier)
    volumes:
      - .:/pkg

```

## 5 Génération de la Wheel

/!\ Nécessaire d'avoir installé avec pip wheel /!\

```
pip install wheel
```

Enfin executer cette commande

```
py ./setup.py bdist_wheel
```

## 6 Déploiement en local

Désinstaller la wheel précédente (si existe)

```
pip uninstall ./chemin/de/wheel/nom_wheel.whl
```

Installer la nouvelle wheel dans le projet python

```
pip install ./chemin/de/wheel/nom_wheel.whl
```

## 7 Déploiement en live

Si nom de version non modifié :

Sur le serveur qui heberge votre application, remplacer le fichier wheel par le nouveau généré.

Si nom de version modifié :

Sur le serveur qui heberge votre application, créer un nouveau dossier portant le numéro de version, y déplacer le fichier **docke-compose.yml**, **Dockerfile** et le fichier wheel généré dedans.

Créer l'image du nouveau package :

```
docker build --tag salesky/pkgsalesky{dal|ws|tool}:n°version {path}
```

Pour la version 1.1.5 :

Le "." à la fin de la commande correspond au chemin où se trouve le package. Dans l'exemple le prompt se trouve dans le répertoire du fichier package.

```
docker build --tag salesky/pkgsaleskydal:1.1.5 .
```

## ADDENDUM Ajouter une base au package 

Dans le fichier de configuration **setup.py** ajouter le nom de la nouvelle base dans le tableau packages :

```py
      packages=['SaleskyBdd', 'SaleskyBdd.dbflxSalesky', 'SaleskyBdd.dbOPENTRM', 'SaleskyBdd.dbREPORTSALESKY', 'SaleskyBdd.dbDBI_FR11',
                'SaleskyBdd.dbSALESKY', 'SaleskyBdd.dbdwhSalesky', 'SaleskyBdd.dbGESTEDI', 'SaleskyBdd.dbwrkOPENTRM', 'SaleskyBdd.dbBPW'],
```

Dans le fichier **_OutilCreation\creClassFromBdd.py** ajouter la configuration de cette nouvelle base.

Enfin executer ce dernier.