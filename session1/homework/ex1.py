from flask import Flask, render_template,redirect,url_for
app = Flask(__name__)


@app.route('/about-me')
def profile():
    title = "My Profile"
    return render_template('profile.html',
                            title = title)

@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)
if __name__ == '__main__':
  app.run(debug=True)
