from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename



UPLOAD_FOLDER = '/Users/fujimotoikki/media_upload/static'
ALLOWED_EXTENSIONS = set({'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'})

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  


@app.route('/upload', methods=['POST'])
def upload_media():
    if 'file' not in request.files:
        return jsonify({'error': '画像が提供されていません'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'ファイルが選択されていません'}), 400
    if file and allowed_file(file.filename):
        filename =  secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return jsonify({'msg': '画像が正常にアップロードされました'}) 
    else:
        return jsonify({'msg': '許可されていないファイル形式です'}),400



if __name__ == '__main__':
    app.run(debug=True, port=5000)