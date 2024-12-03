from flask import Flask, request, render_template

app = Flask(__name__, static_folder="static")

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        feedback = request.form.get('feedback')
        return render_template('formcomplete.html', fname=fname, lname=lname, feedback=feedback)
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug = True)