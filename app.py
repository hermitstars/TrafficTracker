from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    color1 = '#F14722'
    color2 = '#E67E22'
    color3 = '#F4D03F'
    color4 = '#27AE60'
    colors = [color1, color2, color3, color4]
    return render_template('index.html', colors = colors)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
