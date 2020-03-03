from flask import Flask as flask
from flask import render_template
app = flask(__name__)

image_link_1 = str
image_link_2 = str


@app.route('/')
def index():
    checkError = str(input("change the color"))
    if (checkError == "11"):
        image_link_1 = "images/boxB.png"
        image_link_2 = "images/boxB.png"
    elif (checkError == "10"):
        image_link_1 = "images/boxB.png"
        image_link_2 = "images/boxR.png"
    elif (checkError == "01"):
        image_link_1 = "images/boxR.png"
        image_link_2 = "images/boxB.png"
    else:
        image_link = "images/boxR.png"
        image_link = "images/boxR.png"
    print(image_link_1)
    print(image_link_2)
    return render_template('index.html', image_file_1 = image_link_1, image_file_2 = image_link_2 )

@app.route('/info')
def info():
    return 'Info'

if __name__ == "__main__":
    app.run()
