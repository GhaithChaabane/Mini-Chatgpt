from flask import Flask
from flask import jsonify
app=Flask(__name__)
stores=[
    {'items':'stuff'
     ,'iventories':
     [
         {'ite2':25,'itm3':'froties'
          }
          ]
          }
          ]
@app.route('/store',methods=['POST'])
def hom():
    pass
@app.route('/store')
def name_giver():
    return jsonify({'stores':stores})
app.run(port=5000)