from flask import Flask, request, jsonify
import argparse
import sys
import csv

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
    Return a standard JSON block of people in any order of format. Must be valid JSON
    '''
    # TODO
    pass
    

@app.route('/people/age',methods=['GET'])
def sortPeopleByAge():
    '''
    Returns Json block containing a list of people sorted by age youngest to oldest
    TODO: If age does not exist, infer age from date of 3rd grade graduation
    '''
    # TODO
    pass

@app.route('/ids/lastname/<lastname>',methods=['GET'])
def getIdsByLastName(lastname):
    '''
    Returns Json block of ids found for the given last name
    Using path params
    '''
    # TODO
    pass


# TODO Create an endpoint POST that accepts a 'person' and appends it to our people (write to the file and update the store). 
# Returns the newley updated JSON block of all people.
# New endpoint goes here.


# Optional Challenge: Persist the data somehow


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--debug", help="Optional Debug Mode for stack traces", action="store_true")

    parser.add_argument("port", help="Port to run local server on")
    parser.add_argument("file", help="File to import data from")
    args = parser.parse_args()

    # TODO: Initialize any pre-application start code here if needed

    port = args.port
    filename = args.file

    # store people in dict where key is id and value is dict of attributes
    people_list = []
    with open(filename, 'rb') as f:
        # skip first line
        next(f, None)

        reader = csv.DictReader(f, restval='', fieldnames=('ID','First','Last','Age','GithubAcct','Date of 3rd Grade Graduation'))
        for line in reader:
            personId = line['ID']
            if personId:
                people_list.append({
                    personId: {
                        'first': line['First'],
                        'last': line['Last'],
                        'age': line['Age'],
                        'github': line['GithubAcct'],
                        'graduationDate': line['Date of 3rd Grade Graduation']
                    }
                })
    print people_list

    app.debug=args.debug
    app.run(host='0.0.0.0',port=args.port)

