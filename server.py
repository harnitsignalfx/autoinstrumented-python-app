from flask import Flask, request
import json
import requests
import os
import sys

app = Flask(__name__)



@app.route('/request', methods=['GET'])
def requestCheck():
    '''Sends dummy event'''

    #headers = {'X-SF-TOKEN' : os.environ['SF_TOKEN'],'Content-Type' : 'application/json'}
    #headers = {'X-SF-TOKEN' : token,'Content-Type' : 'application/json'}

    return "OK"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)
