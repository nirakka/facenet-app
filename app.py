import os
import sys
from flask import Flask, send_file, request
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename
import subprocess
import pickle
from scipy import spatial

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
app = Flask(__name__)


@app.route('/<path:path>')
def style_transfer(path):
    return "akari"

@app.route('/<path:path>', methods=["POST"])
def upload(path):
    f = request.files['file1']
    input_filepath = os.path.join('./file1.jpeg' )
    f.save(input_filepath)

    f2 = request.files['file2']
    input_filepath2 = os.path.join('./file2.jpeg' )
    f2.save(input_filepath2)
    check = subprocess.run(["python", "compare2.py", "/images/20170512-110547", "file1.jpeg", "file2.jpeg"])
        
    pkl_path = "/output/img_facenet.pkl"

    with open(pkl_path, 'rb') as f:
        data_face = pickle.load(f)

        A = data_face['file1.jpeg']
        B = data_face['file2.jpeg']

        return str(spatial.distance.euclidean(A, B))
if __name__ == '__main__':
    app.run(host='0.0.0.0')
