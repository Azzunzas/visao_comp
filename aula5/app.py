from flask import Flask, render_template, request, jsonify, send_from_directory
import cv2
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/processed'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files[' ']
    
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return filepath

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    image_path = data.get('image_path')
    action = data.get('action')
    
    image = cv2.imread(image_path)
    
    if action == 'blur':
        processed_image = cv2.GaussianBlur(image, (15, 15), 0)
    elif action == 'sharpen':
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        processed_image = cv2.filter2D(image, -1, kernel)
    elif action == 'rotate':
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
        processed_image = cv2.warpAffine(image, matrix, (w, h))
    
    processed_path = os.path.join(PROCESSED_FOLDER, f'processed_{os.path.basename(image_path)}')
    cv2.imwrite(processed_path, processed_image)
    
    return processed_path

if __name__ == '__main__':
    app.run(debug=True)
