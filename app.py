from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)


if not os.path.exists('data.json'):
    with open('data.json', 'w') as f:
        json.dump([], f)


def load_data():
    with open('data.json', 'r') as f:
        return json.load(f)


def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)


@app.route('/')
def index():
    blogs = load_data()
    return render_template('index.html', blogs=blogs)


@app.route('/blogs')
def blogs():
    blogs = load_data()
    return render_template('blogs.html', blogs=blogs)


@app.route('/blogs/<int:id>')
def blog_detail(id):
    blogs = load_data()
    blog = next((blog for blog in blogs if blog['id'] == id), None)
    if blog:
        return render_template('detail.html', blog=blog)
    return "Blog topilmadi", 404


@app.route('/add', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        blogs = load_data()
        new_blog = {
            'id': len(blogs) + 1,
            'title': title,
            'content': content,
            'created_at': '2023-10-01'  # Vaqtni avtomatik qo'shish mumkin
        }
        blogs.append(new_blog)
        save_data(blogs)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:id>')
def delete_blog(id):
    blogs = load_data()
    blogs = [blog for blog in blogs if blog['id'] != id]
    save_data(blogs)
    return redirect(url_for('index'))


@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    blogs = load_data()
    filtered_blogs = [blog for blog in blogs if query in blog['title'].lower()]
    return render_template('index.html', blogs=filtered_blogs)

if __name__ == '__main__':
    app.run(debug=True)