from flask import Flask, jsonify
import requests
from score import getdata
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    # x={"all":"https://inshorts-news.vercel.app/all","national":"https://inshorts-news.vercel.app/national","business":"https://inshorts-news.vercel.app/business","sports":"https://inshorts-news.vercel.app/sports","world":"https://inshorts-news.vercel.app/world","politics":"https://inshorts-news.vercel.app/politics","technology":"https://inshorts-news.vercel.app/technology","startup":"https://inshorts-news.vercel.app/startup","entertainment":"https://inshorts-news.vercel.app/entertainment","science":"https://inshorts-news.vercel.app/science","automobile":"https://inshorts-news.vercel.app/automobile"}
    x = getdata()

    return x


@app.route("/<string>/<string1>")
def nat(string, string1):
	x = getdata()
	return x


if __name__ == "__main__":
    # app.debug = True
    app.run()
