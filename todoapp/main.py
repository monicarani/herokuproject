#This is the main page from where everything starts.
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/")

def introduce():
    return render_template('index.html',
           question={'key':"name","text":"Please ENTER YOUR NAME to start..."}
        )

@app.route("/message",methods=['POST'])

def user_message():
    if request.method == 'POST':
        from .intents import handle
        return handle(request.form)
    else:
        return "INVALID"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

