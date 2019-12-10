from flask import request, jsonify, abort, redirect, url_for

from src import app
from src.constants import *
from src.utility import create_error
from src.models import db
from sys import stderr

import re
import jwt

@app.route('/')
def redirect_to_api():
    return redirect(url_for('api_error'))

@app.route('/api/nothing')
def api_error():
    return abort(418)

@app.route('/api')
@app.route('/api/')
def get_api():
    return jsonify(dict(data=[
        dict(route='/admin', method='POST'),
        dict(route='/api/users', method='GET'),
        dict(route='/api/user_details/<HASH>', method='GET'),
        dict(route='/access/check', method='GET')
    ]))

@app.route('/api/users')
def get_users():
    return jsonify(db.get_users())

@app.route('/api/user_details')
def get_user_error():
    return jsonify(create_error('HASH is required in URL'))

@app.route('/api/user_details/<HASH_ID>')
def get_user(HASH_ID):
    user_id = db.get_id(HASH_ID)
    if not user_id:
        return jsonify(create_error('Bad hash'))

    return jsonify(db.get_user(HASH_ID))

@app.route('/access/check')
def admin_access_check():
    if not request.args:
        return jsonify(create_error("GET parameters is required"))
        
    if ACCESS_TOKEN not in request.args:
        return jsonify(create_error(f'Field {ACCESS_TOKEN} is required in json!'))

    if not request.args[ACCESS_TOKEN]:
        return jsonify(create_error(f'Field {ACCESS_TOKEN} can\'t be empty!'))

    try:
        access_token_decoded = jwt.decode(
            request.args['access_token'],
            verify=False,
            algorithms=None)
    except jwt.exceptions.DecodeError:
        return jsonify(create_error('Check failed'))

    if ROLE not in access_token_decoded or ID not in access_token_decoded:
        return jsonify(create_error(f'Key {ROLE} or {ID} doesn\'t exist in {ACCESS_TOKEN}'))

    isRoot = access_token_decoded[ROLE] == ROOT_ID and access_token_decoded[ID] == 1
    return jsonify(dict(status=isRoot))

@app.route('/admin', methods=['POST'])
def admin():
    if not request.json:
        return jsonify(create_error(f'Fields {ACCESS_TOKEN} and {LOGIN} is required in json!'))

    if ACCESS_TOKEN not in request.json or LOGIN not in request.json:
        return jsonify(create_error(f'Fields {ACCESS_TOKEN} and {LOGIN} is required in json!'))

    if not request.json[ACCESS_TOKEN] or not request.json[LOGIN]:
        return jsonify(create_error(f'Fields {ACCESS_TOKEN} and {LOGIN} can\'t be empty!'))
    
    try:
        atdecoded = jwt.decode(
            request.json['access_token'],
            verify=False, 
            algorithms=None)
    except jwt.exceptions.DecodeError:
        return jsonify(create_error('Check failed'))

    if not atdecoded:
        return jsonify(create_error('Whoops! Some problems with decoding JWT token'))


    if not ID in atdecoded or not ROLE in atdecoded:
        return jsonify(create_error(f'Key {ID} or {ROLE} doesn\'t exist in {ACCESS_TOKEN}'))

    if not atdecoded[ROLE] or not atdecoded[ID]:
        return jsonify(create_error(f'Fields {ROLE} and {ID} can\'t be empty!'))

    if atdecoded[ROLE] != ROOT_ID:
        return jsonify(create_error(f'ACCESS DENIED! You must be Elon Mask or at least know the number of his position'))

    if not VULNERABLE_NAME in request.args:
        return jsonify(create_error(f'{VULNERABLE_NAME} is required in GET parameters!'))

    vulned_arg = request.args[VULNERABLE_NAME]
    PATTERN = r'(b64|base64|decode|encode|rm|environ|mkdir|mkdirs|walk|hex|b16|base16|ascii|popen|system|truncate|removedirs|rmdirs|subprocess|remove|docker|cp|mv|nc|shell|bash|sh|server|tmp)'
    if re.findall(PATTERN, vulned_arg):
        return jsonify(create_error('ACCESS DENIED! You can\'t use destructive methods'))

    try:
        response = str(eval(vulned_arg))
    except Exception as err:
        return create_error(str(err))
    return response