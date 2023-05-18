import sys
import os
from flask import Flask, request, jsonify, render_template, flash
from torch_utils import get_prediction


app = Flask(__name__)

result = ''

def helper_func(data):
    return render_template('result.html', result=data)

ALLOWED_EXTENSIONS = {'jpg'}
def allowed_file(filename):
    #function checks the extension of the file. has to be jpg
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
app.secret_key = "eiuweuy_wbnd628_wh70"

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    if file:
        # Save the file to a directory
        file.save('newData/image.jpg')
        return render_template('uploadsuccess.html')
    else:
        return 'No file uploaded'

@app.route('/predict', methods=['POST', 'GET'])
def predict(): 
    result = get_prediction()

    return jsonify({'redirect': '/result'})

@app.route('/result', methods=['POST', 'GET'])
def result(): 
    result, accuracy = get_prediction()
    #Show only two digits after decimal point
    accuracy = accuracy.item()
    accuracy=accuracy*100
    accuracy=accuracy//1
    accuracy=accuracy/100

    return render_template('result.html', result=result, accuracy=accuracy)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
        #except:
           # return jsonify({'error': 'error during prediction'})