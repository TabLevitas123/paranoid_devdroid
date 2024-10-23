
from flask import Flask, render_template, request
from marvin_orchestration import Marvin

app = Flask(__name__)

# Marvin initialization
marvin = Marvin(name="Marvin", task="Orchestrate Agent Swarm")

@app.route('/')
def home():
    return render_template('index.html', marvin_intro=marvin.task)

@app.route('/submit_task', methods=['POST'])
def submit_task():
    user_task = request.form.get('task_input')
    
    # Marvin processes the user's task
    if user_task:
        final_decision = marvin.decide(user_task)
        response = f"Marvin's Decision: {final_decision}"
        marvin.communication_protocol.display_message_log()  # Display communication logs in the console for now
    else:
        response = "Marvin says: Please provide a valid task."

    return render_template('index.html', marvin_intro=marvin.task, response=response)

if __name__ == '__main__':
    app.run(debug=True)
