from flask import Flask as flask
from flask import render_template
app = flask(__name__)

image_link = str


@app.route('/')
def index():
    checkError = str(input("change the color (y/n)"))
    if (checkError == "y"):
        image_link = "images/boxB.png"

    else:
        image_link = "images/boxR.png"

    print(image_link)
    return render_template('index.html', image_file = image_link )

@app.route('/info')
def info():
    return 'Info'

if __name__ == "__main__":
    app.run()
