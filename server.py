from flask import Flask, request, jsonify
import argparse
import sys
import csv
from helpers import validateAndInferAge
import shelve

people_list = []

#Web app
app = Flask(__name__)

@app.route('/ping',methods=['GET'])
def pingServer():
    '''
    Ping request to make sure server is alive, return 'pong'
    '''
    return 'pong'

@app.route('/people',methods=['GET'])
def getPeople():
    '''
    Return array of people objects
    '''
    return jsonify(people_list)
    

@app.route('/people/age',methods=['GET'])
def sortPeopleByAge():
    '''
    Return list of people sorted by age youngest to oldest
    '''
    return jsonify(sorted(people_list, key=lambda person: person['age']))    

@app.route('/ids/lastname/<lastname>',methods=['GET'])
def getIdsByLastName(lastname):
    '''
    Return array of ids found for the given last name
    '''
    return jsonify([person['id'] for person in people_list if person['last'] == lastname])

@app.route('/person',methods=['POST'])
def postPerson():
    '''
    Add person to people list if not already there, Return array of people objects
    '''
    req_data = request.get_json()
    age = validateAndInferAge(req_data['age'], req_data['graduationDate'])
    
    if req_data['id'] not in map(lambda person: person['id'], people_list):
        people_list.append({
            'id': req_data['id'],
            'first': req_data['first'],
            'last': req_data['last'],
            'age': age,
            'github': req_data['github'],
            'graduationDate': req_data['graduationDate']
        })
    return jsonify(people_list)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--debug", help="Optional Debug Mode for stack traces", action="store_true")

    parser.add_argument("port", help="Port to run local server on")
    parser.add_argument("file", help="File to import data from")
    args = parser.parse_args()

    port = args.port
    filename = args.file
    filenameWithoutExtension = filename.split('.', 1)[0]

    data_store = shelve.open(filenameWithoutExtension, writeback=True)

    if data_store.has_key(filenameWithoutExtension):
        people_list = data_store[filenameWithoutExtension]
    else:
        with open(filename, 'rb') as f:
            next(f, None)

            reader = csv.DictReader(f, restval='', fieldnames=('ID','First','Last','Age','GithubAcct','Date of 3rd Grade Graduation'))
            for line in reader:
                graduationDate = line['Date of 3rd Grade Graduation']
                age = validateAndInferAge(line['Age'], graduationDate)

                people_list.append({
                    'id': line['ID'],
                    'first': line['First'],
                    'last': line['Last'],
                    'age': age,
                    'github': line['GithubAcct'],
                    'graduationDate': graduationDate
                })
                data_store[filenameWithoutExtension] = people_list

    app.debug=args.debug
    app.run(host='0.0.0.0',port=args.port)

