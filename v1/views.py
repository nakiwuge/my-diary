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
        return jsonify({'entries':all_entries}) 
              
    else:
        add_entry = request.get_json() 
        all_entries.append(add_entry)
        return jsonify({'entries':all_entries})
       
@app.route('/api/v1/entries/<int:id>' , methods=['GET','PUT'])
def content(id):
    if request.method == 'GET':
        get_content=[x for x in all_entries  if x['id'] == id] 
        return jsonify({id:get_content[0]})

    else:
        get_content=[x for x in all_entries  if x['id'] == id] 
        get_content[0]=request.get_json()
        return jsonify({id:get_content[0]})