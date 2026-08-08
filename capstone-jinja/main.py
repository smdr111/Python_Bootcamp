from flask import Flask, render_template,url_for
import requests


app = Flask(__name__)
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
text = response.json()

@app.route('/')
def home():
    return f'''
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    ">
        <a href="{url_for("get_blog")}">Go To Blogs</a>
    </div>
    '''

@app.route('/blogs')
def get_blog():
    return render_template("index.html",data=text)

@app.route('/posts/<int:num>')
def get_post(num):
    requested = None
    for blog in text:
        if blog['id'] == num:
            requested = blog
    return render_template('post.html',post=requested)


if __name__ == "__main__":
    app.run(debug=True)
