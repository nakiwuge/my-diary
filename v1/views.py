from flask import Flask, jsonify, request
from v1 import app
import json

all_entries = [] 


@app.route('/api/v1/entries', methods=['GET', 'POST'])
def entries():
    '''getting an entry'''
    if request.method == 'GET':
        '''check if all_entries is empty'''
        if len(all_entries) == 0:
            return jsonify("no entries added, please add an entry"), 404
        return jsonify(all_entries), 200           
    else:
        '''post an entry'''
        add_entry = request.get_json()
        for key in add_entry:
            '''check if user is not using the required keys'''
            keys = ["id","content", "date", "title"]
            if key not in keys:
                return jsonify("key should be id ,content ,date and title"), 403 
        '''check for empty values'''
        for key in add_entry:
            if add_entry[key] == "":
                return jsonify("one or more of your key values are empty. please check and try again"), 403

        all_entries.append(add_entry)
        return jsonify(all_entries), 200


@app.route('/api/v1/entries/<string:entry_id>', methods=['GET', 'PUT'])
def content(entry_id):
    '''get entry by id'''
    if request.method == 'GET':
        '''check if all_entries is empty'''
        if len(all_entries) == 0:
            return jsonify("no entries added, please add an entry"), 404
        get_content = [entry for entry in all_entries if entry['id'] == entry_id]
        return jsonify(get_content[0])
    else:
        '''#modify entry by id'''
        get_content = [entry for entry in all_entries if entry['id'] == entry_id]
        get_content = [entry for entry in all_entries if entry['id'] == entry_id]
        get_content[0]['title'] = request.json['title']
        get_content[0]['content'] = request.json['content']
        get_content[0]['date'] = request.json['date']
        return jsonify(get_content[0]), 200