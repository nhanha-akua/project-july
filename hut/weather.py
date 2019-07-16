from flask import Flask
 
app = Flask(__name__)
 
@app.route('/today')
def whatistoday():
    return 'its a tues'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')