from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
 def login():
 if request.method == 'POST':
     do_the_login()
 else:
    show_the_login_form()

@app.route("/response")
def render_response():
    color = request.args["color"]
    if color == "blue":
        reply = "That is also my favorite color."
    else:
        reply = "That color sucks"
    return render_template("response.html", response = reply)
if __name__=="__main__":
    app.run(debug=False, port=54321)
