
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory storage for submitted tasks
tasks = []

# Index route for task submission and display
@app.route("/", methods=["GET", "POST"])
def index():
    global tasks
    if request.method == "POST":
        # Get the task from the user and append it to the task list
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect(url_for("index"))
    
    return render_template("index.html", tasks=tasks)

# Dark mode toggle route
@app.route("/toggle-dark-mode")
def toggle_dark_mode():
    # Simple toggle logic (placeholder, no actual dark mode logic yet)
    return "Dark mode toggled (This is a placeholder)."

if __name__ == "__main__":
    app.run(debug=True)
