from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thankyou')
def thankyou():
    first = request.args.get("first")
    last = request.args.get("last")
    return render_template('thankyou.html', first=first, last=last)



if __name__ == '__main__':
    app.run(debug=True)