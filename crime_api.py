from flask import Flask, request

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    address = request.form['address']
    return "Request successful"

if __name__ == '__main__':
    app.run()