from flask import Flask,jsonify,request
from v1 import app
import json

all_entries = []

@app.route('/' )
def home():
    return "<h1>welcome to my diary<h1>"         

  
@app.route('/api/v1/entries' , methods=['GET','POST'])
def entries():
    #getting an entry
    if request.method == 'GET':
        #check if all_entries is empty
        if not all_entries:
            return "no entries added, please add an entry",404
        return jsonify(all_entries),200
              
    else:
        #getting an entry
        add_entry = request.get_json()
        for key in add_entry:
            #check if user is not using the required keys
            if key not in ["id","content","date","title"]:
                return "key should either be id ,content ,date and title",403
            
        all_entries.append(add_entry)
        return jsonify(all_entries),200
      
@app.route('/api/v1/entries/<string:entry_id>' , methods=['GET','PUT'])
def content(entry_id):
    #get entry by id
    if request.method == 'GET':
       
        #check if all_entries is empty
        if not all_entries:
            return "no entries added , please add an entry",404
        #check if id entered is in the data base
        for entry in all_entries:
                if entry_id!=entry["id"]:
                    return "the is no entry with that the provided id",404
    
        get_content =[entry for entry in all_entries if entry['id']==entry_id]
        return jsonify(get_content[0])

    else:
        #modify entry by id
        get_content =[entry for entry in all_entries if entry['id']==entry_id]
        get_content =[entry for entry in all_entries if entry['id']==entry_id]
        get_content[0]['title']=request.json['title']
        get_content[0]['content']=request.json['content']
        get_content[0]['date']=request.json['date']

        return jsonify(get_content[0]),200