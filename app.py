from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def show_links():
    links = [
        {"site_name": "OpenAI", "url": "https://openai.com/"},
        {"site_name": "GitHub", "url": "https://github.com/"},
        {"site_name": "Python", "url": "https://www.python.org/"},
    ]
    return render_template("index.html", page_title="My Links", links=links)


@app.route("/about")
def show_about():
    return render_template("about.html", page_title="About")


if __name__ == "__main__":
    app.run(debug=True)
