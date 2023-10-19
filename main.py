# This is a demo project for ACME Corportaion API

from flask import Flask, request, send_file, abort
from config import api_key

app = Flask(__name__)

# Define a dictionary to store valid API tokens and their associated file paths.
valid_tokens = {
    api_key: "sample_file.txt"
}

@app.route('/get_file', methods=['GET'])
def get_file():
    api_token = request.args.get('token')

    if api_token in valid_tokens:
        file_path = valid_tokens[api_token]
        return send_file(file_path, as_attachment=True)
    else:
        return abort(401)  # Unauthorized

if __name__ == '__main__':
    app.run(debug=True)
