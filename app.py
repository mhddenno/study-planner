from flask import Flask, render_template, request, send_file
import requests
from io import BytesIO
import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    app.logger.info('Enter')
    if request.method == 'POST':
        app.logger.warning(request.files)
        if 'text' in request.form:
            app.logger.info('text')
            text = request.form['text']
        elif 'file' in request.form:
            app.logger.info('file')
            file = request.files['file']
            text = file.read().decode('utf-8')
        elif 'url' in request.form:
            app.logger.info('url')
            url = request.form['url']
            response = requests.get(url)
            text = response.text
        else:
            app.logger.info('else')
            text = ''

        app.logger.info(f"processed_text={text}")
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
