from flask import Flask

app = Flask(__name__)
hello_world_var = "<p>Hello, World!</p>"

@app.route("/")
def hello_world():
    return hello_world_var

def number(text):
    trimmed_text = text[3:-4]
    return len(trimmed_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
