from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    countries = ['Nigeria', 'Tunisia', 'China', 'usa', 'Cameroon']
    return render_template('dashboard.html', countries=countries)

# @app.route('/')
# def hello():
#     house = ['2bedroom', '3bedroom', '4bedroom', '5bedroom', '6bedroom',]
#     return house[0]
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
