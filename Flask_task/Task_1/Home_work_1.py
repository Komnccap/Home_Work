from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def site():
    return render_template('shop.html')


@app.route('/gloth/')
def gloth():
    return render_template('gloth.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')


if __name__ == '__main__':
    app.run(debug=True)
