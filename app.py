
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        with open("task_submissions.txt", "a") as task_file:
            task_file.write(f"{task}\n")
        return render_template("index.html", message="Task submitted successfully!")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
