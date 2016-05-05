from flask import Flask
import flask
import subprocess
import nltk

app = Flask(__name__)

@app.route("/")
def hello():
    product_name = "Dell E1916HV 18.5-inch LED Monitor (black)"    
    query = "inurl:" + product_name
    cmd = ["python","crawler.py", "-n", "10"] + query.split(" ")
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

@app.route("/crawl/", methods=['POST'])
def crawl():
    print "hello"
    product_name = flask.request.json["product_name"]
    print product_name
    query = "inurl:" + product_name
    cmd = ["python","crawler.py", "-n", "10"] + query.split(" ")
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

@app.route('/crawl_result/')
def send():
    return flask.send_from_directory('data_files', 'stat.log')

if __name__ == "__main__" :
    app.run()
