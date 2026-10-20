from flask import Flask, send_file

pudim = r"C:\Users\joao.vsalves25\Downloads\pudim-de-chocolate-como-fazer-o-pudim-mais-cremoso-e-saboroso-que-voce-ja-provou.jpg"

app = Flask(__name__)

@app.route("/api/ping", methods=["GET"])
def ping():
    return send_file(pudim, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True, port=5000)