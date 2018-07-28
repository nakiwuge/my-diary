from flask import Flask, jsonify, request
from v1 import app
import json
import datetime

all_entries = [] 
now = datetime.datetime.now()

    
@app.route('/api/v1/entries', methods=['GET', 'POST'])
def entries():
    '''getting an entry'''
    if request.method == 'GET':
        '''check if all_entries is empty'''
        if len(all_entries) == 0:
            return jsonify("no entries added, please add an entry"), 200
        return jsonify(all_entries), 200           
    else:
        '''post an entry'''
        new_entry = {'id': len(all_entries)+1,"date":now.strftime("%Y-%m-%d") }
        get_entry = request.get_json() 
        
         
        '''check if title is missing'''
        if 'title' not in get_entry:
            return jsonify("please add title and try again"), 200
        elif not get_entry['title'].lower().islower():  
            return jsonify("please add title to your entry"), 200
            
            '''check for empty content'''
        elif 'content' not in get_entry:
            return jsonify("please add content and try again"), 200
        elif not get_entry['content'].lower().islower():
            return jsonify("please add write something in the content"), 200

        new_entry['title']=get_entry['title']
        new_entry['content']= get_entry['content']   
        all_entries.append(new_entry)
        return jsonify(new_entry), 200


@app.route('/api/v1/entries/<int:entry_id>', methods=['GET', 'PUT'])
def content(entry_id):
    '''get entry by id'''
    if request.method == 'GET':
        '''check if entry with specified id exists all_entries is empty'''

        get_entry = [entry for entry in all_entries if entry['id'] == entry_id]
        if len(get_entry) == 0:
            return jsonify("no entry with that id"), 200
            
        return jsonify(get_entry[0]), 200
    else:
        '''#modify entry by id'''
        get_entry = [entry for entry in all_entries if entry['id'] == entry_id]
        if len(get_entry) == 0:
            return jsonify("no entry with that id"), 200

        elif 'title' not in get_entry:
            return jsonify("please add title and try again"), 200
        elif not get_entry['title'].lower().islower():  
            return jsonify("please add title to your entry"), 200
           
            '''check for empty content'''
        elif 'content' not in get_entry:
            return jsonify("please add content and try again"), 200
        elif not get_entry['content'].lower().islower():
            return jsonify("please add write something in the content"), 200

        get_entry[0]['title'] = request.json['title']
        get_entry[0]['content'] = request.json['content']
        return jsonify(get_entry[0]), 200