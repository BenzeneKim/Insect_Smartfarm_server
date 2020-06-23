import sqlite3

conn = sqlite3.connect("sensorData.db")
cur = conn.cursor()

#code - module number, temp - temperature, hum - humidity, bat - battery remaining percentage

def addData(code, temp, hum, bat):
    cur.execute("INSERT INTO MODULEstatus values(datetime('now'), (?), (?), (?), (?))", (code, temp, hum, bat))
    conn.commit()

addData(1,30.0, 57.5, 800)
addData(2,30.0, 57.5, 800)
addData(3,30.0, 57.5, 800)
addData(4,30.0, 57.5, 800)

