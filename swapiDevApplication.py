import json
import os
import pathlib

from flask import Flask, jsonify

path_ = pathlib.Path().resolve()
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'dataFiles')


@app.route('/')
def get_homepage():
    return 'Welcome to Homepage'


@app.route('/people/<peopleId>', methods=['GET'])
def get_people(peopleId):
    with open(data_file+'/people.json', 'r') as f:
        data = f.read()
        people = json.loads(data)
        if int(peopleId) in range(1, 100):
            app.logger.info('People data found with ID: %s', peopleId)
            return jsonify(people)
        else:
            app.logger.info('People data not found with ID: %s', peopleId)
            return jsonify({'error': 'data not found'}), 404


@app.route('/planets/<planetId>')
def get_planets(planetId):
    with open(data_file+'/planets.json', 'r') as f:
        data = f.read()
        people = json.loads(data)
        if int(planetId) in range(1, 100):
            app.logger.info('Planet data found with ID: %s', planetId)
            return jsonify(people)
        else:
            app.logger.info('Planet data not found with ID: %s', planetId)
            return jsonify({'error': 'data not found'}), 404


@app.route('/starships/<starshipId>')
def get_starships(starshipId):
    with open(data_file+'/starships.json', 'r') as f:
        data = f.read()
        people = json.loads(data)
        if int(starshipId) in range(1, 100):
            app.logger.info('Planet data found with ID: %s', starshipId)
            return jsonify(people)
        else:
            app.logger.info('Planet data not found with ID: %s', starshipId)
            return jsonify({'error': 'data not found'}), 404


if __name__ == '__main__':
    import logging

    logging.basicConfig(filename=basedir+'/serverLogs/server_logs.log', level=logging.DEBUG)

    app.run(debug=True, port=5050, host='0.0.0.0')
