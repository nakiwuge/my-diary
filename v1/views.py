from flask import Flask,jsonify,request
from v1 import app

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
            return "no entries added , please add an entry"
        return jsonify(all_entries) 
              
    else:
        #getting an entry
        add_entry = request.get_json() 
        all_entries.append(add_entry)
        return jsonify(all_entries)
       
@app.route('/api/v1/entries/<string:entry_id>' , methods=['GET','PUT'])
def content(entry_id):
    if request.method == 'GET':
        #get_content=[x for x in all_entries  if x.values() == entry_id] 
        get_content=[x for x in all_entries for y,z in x.items()if z == entry_id]
        return jsonify(get_content[0])

    else:
        get_content=[x for x in all_entries for y,z in x.items()if z == entry_id] 
        get_content[0]=request.get_json()
        return jsonify(get_content[0])