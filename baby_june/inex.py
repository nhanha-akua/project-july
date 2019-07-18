from flask import *
app = Flask(__name__)
items = []
@app.route('/')
def index():
    return render_template('form.html',items=items)

@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)
    
    
@app.route('/add_todo')
def add_todo():
    item = request.args.get("item")
    items.append(item)
    return redirect('http://localhost:5000/',code=302)
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



