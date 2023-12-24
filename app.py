from flask import Flask, render_template, request, send_file
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            text = file.read().decode('utf-8')
        elif 'text' in request.form:
            text = request.form['text']
        elif 'url' in request.form:
            url = request.form['url']
            response = requests.get(url)
            text = response.text
        else:
            text = ''

        processed_text = text.upper()
        return render_template('index.html', processed_text=processed_text)
    else:
        return render_template('index.html', processed_text=None)

@app.route('/download', methods=['POST'])
def download():
    text = request.form['processed_text']
    buffer = BytesIO()
    buffer.write(text.encode('utf-8'))
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, attachment_filename='text.txt', mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)