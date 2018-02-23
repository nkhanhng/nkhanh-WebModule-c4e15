from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world!"

@app.route('/Hello')
def hello():
    return("blah blah")

@app.route('/chao/<int:num1>/<int:num2>')
def hiK(num1,num2):
    return str(num1+ num2)

@app.route('/html')
def heading():
    return render_template("index.html")

@app.route('/blog')
def blog():
    title = 'No name'
    posts = [
        {
            "content":"jdwldhwa",
            "author":"Niko"
        },
        {
            "content":"ahfilnhef",
            "author":"s1mple"
        },
        {
            "content":"fhalefahw",
            "author":"coldzera"
        }
    ]
    return render_template("blog.html", article_title = title,
                            post = posts)

if __name__ == '__main__':
  app.run(debug=True)
