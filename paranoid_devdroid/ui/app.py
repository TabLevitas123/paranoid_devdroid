
from flask import Flask, render_template, request, redirect, url_for
from paranoid_devdroid.plugins.core.agent_prompting import AgentPrompting

app = Flask(__name__)

# Initialize the Agent Prompting system
agent_prompting = AgentPrompting()

# Index route for task submission and agent management
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the task from the user and create a new agent for it
        task = request.form.get("task")
        if task:
            agent_prompting.create_agent(task)
        return redirect(url_for("index"))
    
    # Retrieve active agents and their statuses
    active_agents = agent_prompting.get_active_agents()
    return render_template("index.html", tasks=active_agents)

# Dark mode toggle route (placeholder)
@app.route("/toggle-dark-mode")
def toggle_dark_mode():
    return "Dark mode toggled (This is a placeholder)."

if __name__ == "__main__":
    app.run(debug=True)
