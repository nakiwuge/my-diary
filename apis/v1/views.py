from flask import Flask,jsonify,request
from v1 import app

all_entries = [ 
    {'id':1 ,'title':'learning flask' ,'date':'4-june-2018','content':'i have started learning flask'}, 
    {'id':2, 'title':'andela boot camp','date':'14-july-2018','content':'i am going to be part of the andela bootcamp'},
    {'id':3, 'title':'templating' ,'date':'25-july-2018','content':'i learnt thow to make templates'}
    ]
@app.route('/' )
def home():
    return "<h1>welcome to my diary<h1>"         
   
@app.route('/api/v1/entries' , methods=['GET','POST'])
def entries():
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
        pass
