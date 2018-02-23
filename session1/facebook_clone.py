from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user')
def user():
    title = "Profile"
    profiles = [
        {
            "name":"Khanh",
            "age": 21,
            "hobbies":"code,game,music",
            "sex":"male"
        },
        {
            "name":"Nam",
            "age": 21,
            "hobbies":"csgo",
            "sex":"male"
        },
        {
            "name":"Viet",
            "age": 21,
            "hobbies":"crush",
            "sex":"male"
        },
        {
            "name":"Blah",
            "age": 45,
            "hobbies":"nothing",
            "sex":"female"
        }

    ]
    return render_template('profile.html',
                            User = title,
                            profile = profiles)

if __name__ == '__main__':
  app.run(debug=True)
