from flask import Flask, render_template, request, redirect, url_for
import json
import os
import subprocess

# Web (Flask) setup
app = Flask(__name__)
JSON_FILE = '/home/pi/tke_speaker_ai/api_key_tke.json'

def read_parameters():
    """Đọc các tham số từ file JSON."""
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def write_parameters(params):
    """Ghi các tham số vào file JSON."""
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(params, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    """Hiển thị trang chính với các tham số."""
    parameters = read_parameters()
    return render_template('index.html', parameters=parameters)

@app.route('/update_parameter/<param>', methods=['POST'])
def update_parameter(param):
    """Cập nhật các tham số hoặc khởi động lại hệ thống."""
    parameters = read_parameters()
         
    data = request.get_json()
    if data and data.get('reset') == True:
        # Chạy lệnh reboot
        subprocess.Popen(['sudo', 'reboot'], shell=False)
        return jsonify({"status": "rebooting"}), 200
    return jsonify({"status": "failed"}), 400     
         
            
    # Cập nhật giá trị của tham số
    new_value = request.form.get(param)
    if new_value:
        parameters[param] = new_value

    # Cập nhật các tham số khác nếu có
    api_gemini = request.form.get('api_gemini')
    api_chatgpt = request.form.get('api_chatgpt')
    active_home = request.form.get('active_home')
    
    if api_gemini:
        parameters['api_gemini'] = api_gemini
        if api_gemini == "true":
            parameters['api_chatgpt'] = "false"  # Nếu chọn Gemini thì tắt ChatGPT

    if api_chatgpt:
        parameters['api_chatgpt'] = api_chatgpt
        if api_chatgpt == "true":
            parameters['api_gemini'] = "false"  # Nếu chọn ChatGPT thì tắt Gemini

    if active_home:
        parameters['active_home'] = active_home

    # Ghi lại các tham số đã cập nhật vào file
    write_parameters(parameters)
    return redirect(url_for('index'))

