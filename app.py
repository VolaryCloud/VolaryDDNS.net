from flask import Flask, redirect

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect_all(path):
    return redirect("https://ddns.volary.cloud", code=301)

if __name__ == '__main__':
  app.run(debug=False, port=3000, host='0.0.0.0')
