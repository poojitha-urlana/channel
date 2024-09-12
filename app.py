from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/channel/etv')
def etv():
    return render_template('etv.html')

@app.route('/channel/maatv')
def maatv():
    return render_template('maatv.html')

@app.route('/channel/zeetelugu')
def zeetelugu():
    return render_template('zeetelugu.html')

@app.route('/channel/gemini')
def gemini():
    return render_template('gemini.html')

if __name__ == '__main__':
    app.run(debug=True)
