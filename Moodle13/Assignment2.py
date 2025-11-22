
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='airports',
    autocommit=True,
)



cursor = conn.cursor()

cursor.execute("SELECT * FROM flight")
airport_rows = cursor.fetchall()
airport_columns = [desc[0] for desc in cursor.description]



def store_data():
    flight = {}
    for row in airport_rows:
        row_dict = dict(zip(airport_columns, row))

        airport_name = row_dict.get('name', 'unknown')
        city = row_dict.get('municipality', 'unknown')


        flight[row_dict['ident']] = {
            "ICAO": row_dict['ident'],
            "Name": airport_name,
            "Location": city
        }

    return flight


flightdata = store_data()


@app.route('/airport/<ICAO>', methods=['GET'])
def airports(ICAO):
    ICAO = ICAO.upper()
    if ICAO in flightdata:
        airport = flightdata[ICAO]


        response = {
            "ICAO": airport["ICAO"],
            "Name": airport["Name"],
            "Location": airport["Location"]
        }

        return jsonify(response)
    else:
        return jsonify({"error": "Airport not found"}), 404


app.run(debug=True, port=9000)
