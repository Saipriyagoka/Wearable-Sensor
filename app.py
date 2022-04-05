
# Externam Imoprts
from flask import Flask, request, jsonify

# Internal Imports
from simulator import *

app = Flask(__name__)  

@app.route('/ping')
def ping():
   return 'PONG'

@app.route('/vitals_input',  methods=['POST'])
def vitals_input():
    patient_data = request.json
    return generate_values(patient_data)

@app.route('/vitals_output',  methods=['GET'])
def vitals_output():
    user_id = request.args.get('user_id', '')
    aggregate_min_level = request.args.get('aggregate_min_level', 15)

    if not user_id:
        return "User id is missing", status.HTTP_400_BAD_REQUEST
    
    aggregate_df = caluclate_aggregate_data(user_id, segments=aggregate_min_level)
    
    return aggregate_df

if __name__ == '__main__':
   app.run()