# Autó Biztonsági Rendszer
## Felhasználói dokumentáció

#### Összefoglalás

Biztonági rendszerünk autókba behelyezve védelmet nyújt az esetleges balesetek megelőzése ellen. Kritikus dőlésszögeket beállítva, a Sense HAT-en elhelyezett LED-mátrix mutatja, merre dől az autó, és van lehetőség a jármű korrigálására, felborulva pedig egy segítségkérő Twitter üzenetet oszt meg. A program elindítását követően folyamatosan gyűjti az adatokat az eszköz egy helyi adatbázisba, amit grafikusan is megjelenít.

#### Környezet

* Raspberry Pi, Sense HAT, .py futtatására alkalmas operációs rendszer (Linux).
* Egeret, billentyűzetet, monitort és internetet igényel.
	
#### Használat

*A program indítása*
	
	A program	
		Ide kerül..
	néven található.

*A program eredménye*
	A program elindítja az adatok naplózását a hozzájuk tartozó dátummal.
		Felborulás esetén Twitter üzentet küld erről.
		
*Egy lehetséges kimenet*
	--------Ide jöhet egy sceenshot-------

*Hibalehetőség*
	A program leállítása nem autómatikus, mert egyéni döntés, meddig akarjuk használni. Abban az esetben, ha a programot huzamosabb ideig használjuk, a memória képes betelni és az adatokat nem rögzíteni az adatbázisba.

## Fejlesztői dokumentáció

#### Környezet
* Raspberry Pi, Sense HAT, .py futtatására alkalmas operációs rendszer (Linux).
* Python III fordítóprogram.
* Internetwebcímhelye a grafikai megjelenítésre.
* Fejlesztői Twitter felhasználó az automatikus üzenetküldésre.

#### Forráskód
	/globals.py 		- a változók inicializálása
	/Database		- az adatbázis létrehozása
	/insertdatabase.py	- az adatbázis importálása, és a megfelelő 
						formátumok beállítása
	/Arrows.py		- a dőlés függvényében a nyilak megjelnítése a 
						LED-mátrixon.
	/tweet.py		- automatikus tweetelés
	/Main.py		- végleges futtatható kód, az előző kódokat meghívva

#### Megoldás

*Fontos programrészek*
	
*Main.py*
	'''python
		...
		if (pitch>90 and pitch <270) or (roll>90 and roll <270):
			s.set_pixels( Arrows.piros_x() )
    
		elif pitch >40 and pitch <90:
			s.set_pixels( Arrows.nyil_balra())
		...
	'''
Az arrows.py függvény meghívásával és a kritikus dőlésszögek 50 fokra beállításával, jelzi ki az eszköz a dölés irányát, illetve a borulást.

	*insertdatabase*
		'''python
			import mysql.connector
			from datetime import datetime
			from sense_hat import SenseHat
			import time



			def insert(pitch,roll,yaw,x,y,z):
    				mydb=mysql.connector.connect(host="localhost", user="Raspberry", password="root", database="exampledb4")
    				mycursor=mydb.cursor()
    				now=datetime.now()
    				formatted_date=now.strftime('%Y-%m-%d %H:%M:%S')
    				sql="""INSERT INTO adatok (datum,pitch,roll,yaw,backwardforward,rightleft,updown)
    				VALUES(%s,%s,%s,%s,%s,%s,%s)"""
   				val=(formatted_date,pitch,roll,yaw,x,y,z)
    				mycursor.execute(sql,val)
    				mydb.commit()
    				time.sleep(0.2)
    				mycursor.close()
    				mydb.close()
		'''
	
	A programban szükséges deklarálni a létrehozott adatbázis elérhetőségét és szükséges a jelszót megadni a *mysql.connector.connect()* függvényben. A *mycursor=mydb.cursor()* és a *now=datetime.now()* függvényekkel a kurzort a helyére állítottuk és az időt beállítottuk.
	
