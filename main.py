from flask import Flask, render_template
from scrape import gorsel

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def anasayfa():
  try:
    x = gorsel()
    print(x)
    return render_template('index.html', resm = x)
  except:
    return anasayfa()

if __name__ == '__main__':
    app.run(debug=True)

# larei was here
