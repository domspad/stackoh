from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    import os

    app.run(host=os.environ['IP'], port=int(os.environ['PORT']), debug=True)
