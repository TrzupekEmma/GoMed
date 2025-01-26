import sqlite3
import random
from sharedProg import * 

conn = sqlite3.connect("GoMed.db")


cur = conn.cursor()
cur.execute("select pNumber from pharmacy")
pharmacies=cur.fetchall();
cur.execute("select id from prescription")
prescriptions = cur.fetchall();
i=0;
for pNumber in pharmacies:
    i=i+1;
    if(i>15):
        break;
    print("starting pharmacy "+str(pNumber[0]))
    for prescription in prescriptions:
        bar=random.randint(1,10);
        rolls = random.randint(5,20);
        for experience in range(0,rolls):
            rating=0
            if(random.randint(1,10)>=bar):
                rating=1;
            add_rating(conn,prescription[0],pNumber[0],rating);
