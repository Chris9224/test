from flask import request, Flask
import jsonapp1 = Flask(__name__)
@app1.route('/')def hello_world():
    return 'Blank Page for App2 'if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0')