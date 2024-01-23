from flask import Flask, render_template
import os

app = Flask(__name__)

# Establece la ubicación de las plantillas
template_dir = os.path.abspath(os.path.dirname(__file__))
app.template_folder = template_dir

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
