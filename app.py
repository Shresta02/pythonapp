from flask import Flask
app=Flask(__name__)
@app.route('/')
def run():
    return "Hello,World!"
if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=8000)
