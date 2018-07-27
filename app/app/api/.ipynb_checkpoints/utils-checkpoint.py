from ..main import app
from flask import jsonify, request
import pandas as pd
import os

@app.route('/xlsxtojson', methods=['GET'])
def xlsxtojson():
    file = request.args.get('file')
    df = pd.read_excel(os.path.join(app.static_folder, 'io', file))
    return jsonify(df.to_dict(orient='list'))