import json
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/posts", methods=["GET", "POST"])
def blogs():
    with open("data.json") as f:
        posts = json.loads(f.read())

    if request.method == 'POST':
        title = request.form['search']
        posts = filter(lambda post: title.lower() in post['title'].lower(), posts)

    return render_template("posts.html", posts=posts)

@app.route("/posts/<int:post_id>")
def post_detail(post_id):
    with open("data.json") as f:
        posts = json.loads(f.read())
    
    post = list(filter(lambda post: post['id'] == post_id, posts))[0]
    
    return render_template('detail.html', post=post)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
