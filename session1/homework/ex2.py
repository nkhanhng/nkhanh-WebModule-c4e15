from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<user_name>')
def user(user_name):
    title = "Profile"
    profiles = {
        'Khanh':{
            "name":"Khanh",
            "age": 21,
            "hobbies":"code,game,music",
            "sex":"male"
        },
        'Nam':{
            "name":"Nam",
            "age": 21,
            "hobbies":"csgo",
            "sex":"male"
        },
        'Viet':{
            "name":"Viet",
            "age": 21,
            "hobbies":"crush",
            "sex":"male"
        },
        'Blah':{
            "name":"Blah",
            "age": 45,
            "hobbies":"nothing",
            "sex":"female"
        }

    }
    if user_name in profiles:
         user_profile = profiles[user_name]
         return render_template('profile.html',
                                User = title,
                                user_profile = profiles)
    else:
        return ('User Not Found')

if __name__ == '__main__':
  app.run(debug=True)
