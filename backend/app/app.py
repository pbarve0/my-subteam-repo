from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def officer_roles() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'convergent'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM officers')
    results = [{name: role} for (id, name, role) in cursor]
    cursor.close()
    connection.close()

    return results

def update_officers(update_string):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'convergent'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO officers (name, role) VALUES (' + update_string  + ')')
    results = [{name: role} for (name, role) in cursor]
    cursor.close()
    connection.close()

    return results
# Step one: simple route

def get_roles_fromdb():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'convergent'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM officers')
    results = [role for (name, role) in cursor]
    cursor.close()
    connection.close()

    return results

def get_roles_fromdb_id(id):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'convergent'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query = f"SELECT * FROM officers WHERE oid = '{id}'" # SQL QUERY
    cursor.execute(query)
    results = [name for (oid, name, role) in cursor]
    cursor.close()
    connection.close()

    return results

@app.route('/')
def index() -> str:
    return_string = 'This is a basic route. This is what the database has right now: /n ' + json.dumps({'Officers': officer_roles()})
    return return_string

#Step two: build a unique GET route
@app.route('/getroles')
def get_roles() ->str:
    return json.dumps({'Officers': get_roles_fromdb()})

#Step three: build a unique GET route with an <id> parameter
@app.route('/getroles/<id>')
def get_name_by_id(id) ->str:
    return json.dumps({'Names': get_roles_fromdb_id(id)})
#Step four: build a POST route

#@app.route('/officers', methods=['POST'])
#def post_route():
    #update_officers()
 #   incomes.append(request.get_json())
  #  return '', 204
if __name__ == '__main__':
    app.run(host='0.0.0.0')
