from flask import Flask, render_template
app = Flask("My App")
@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html",name=name.title())

app.run(debug=True)
