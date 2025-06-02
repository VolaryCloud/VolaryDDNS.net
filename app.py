from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
  return redirect("https://ddns.volary.cloud"),301

if __name__ == '__main__':
  app.run(debug=False, port=3000, host='0.0.0.0')
