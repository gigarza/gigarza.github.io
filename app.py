from flask import Flask, render_template

app = Flask(__name__)


# Set up the homepage
@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/cs_projects')
def cs_projects():
    return render_template("cs_projects.html")


@app.route('/dance_info')
def dance_info():
    return render_template("dance_info.html")


@app.route('/dance_gallery')
def dance_gallery():
    return render_template("dance_gallery.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)