from _functions import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("base.html", candidates=data, message=message)


@app.route('/resume/')
def resume():
    return render_template("resume.html")


@app.route('/candidate/<name>/')
def candidate_page(name):
    return render_template("base.html", candidates=get_candidate(name))


@app.route('/search/')
def search():
    candidates, message = find_candidates()
    return render_template("base.html", candidates=candidates, message=message)


if __name__ == '__main__':
    app.run(debug=True)
