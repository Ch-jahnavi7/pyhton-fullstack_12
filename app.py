from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/course')
def course():
    return render_template("courses.html")

@app.route('/trainers')
def trainers():
    return rnder_template("trainers.html")

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form.get["name"]
        email=request.form.get["email"]
        password=request.form.get["password"]
        dob=request.form.get["dob"]
        gender=request.form["gender"]
        course=request.form["course"]
        return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)

