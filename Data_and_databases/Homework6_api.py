from flask import Flask, request, jsonify
import pg8000, decimal
import json

app = Flask(__name__)

def get_data(_type, _sort):
    conn = pg8000.connect(user="paul", database="mondial")
    cursor = conn.cursor()

    sort_result = ''
    if _sort == 'name':
        sort_result = 'ORDER BY name'
    elif _sort in ('area', 'elevation'):
        sort_result = 'ORDER BY ' + _sort + ' DESC'

    if _type:
        sql = "SELECT name, elevation, area, type FROM lake WHERE type = %s " + sort_result
        cursor.execute(sql, [str(_type)])
    else:
        sql = "SELECT name, elevation, area, type FROM lake " + sort_result
        cursor.execute(sql)

    # nested function
    def get_int(value):
        if isinstance(value, decimal.Decimal):
            return int(value)
        else:
            return None

    query_result = []
    for row in cursor.fetchall():
        item = {
            "name": row[0],
            "elevation": get_int(row[1]),
            "area": get_int(row[2]),
            "type": row[3]
        }
        query_result.append(item)

    return query_result


@app.route("/lakes")
def getLakes():
    lake_type = request.args.get('type', '')
    sort_by = request.args.get('sort', '')

    if sort_by and sort_by not in ('name', 'elevation', 'area'):
        sort_by = 'name'

    result = get_data(lake_type, sort_by)

    return jsonify(result)

app.run()
