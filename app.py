from flask import Flask, render_template
from flask import request

app = Flask(__name__)




@app.route('/')  
def upload():  
    return render_template("file_upload.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename) 
    
@app.route('/index.html')
def hello_world():
    return render_template('index.html')
 


@app.route('/logIn.html')
def login():
    return render_template('logIn.html')


@app.route('/started.html')
def started():
    return render_template('started.html')

@app.route('/library.html')
def library():
    return  render_template('library.html')

@app.route('/music')
def music():
    return 'music page '

if __name__ == "__main__":
    app.run(debug=True )