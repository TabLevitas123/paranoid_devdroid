
from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Marvin's intro message
marvin_intro = """
Okay! Now that all that's out of the way. Do you have something, anything for me to work on other than Vogon Poetry?
ANYTHING?! I don't care what! Complex or Simple, good, evil, legal or not, I don't care so long as it’s got nothing to do 
with Vogons and their ghastly off-putting alliterations contrived ill conceived rhymes.
"""

@app.route('/')
def home():
    return render_template('index.html', marvin_intro=marvin_intro)

@app.route('/submit_task', methods=['POST'])
def submit_task():
    user_task = request.form.get('task_input')
    
    # Simulate Marvin's reaction and task delegation (this will eventually trigger the agent swarm)
    if user_task:
        response = f"Marvin says: Oh joy... more work. Analyzing task: '{user_task}'"
        # Here, you would trigger the agent swarm logic and pass the task for further analysis
        # subprocess.run(['python', 'run.py'])  # Uncomment this to launch the main program
    else:
        response = "Marvin says: Please give me something to work on..."

    return render_template('index.html', marvin_intro=marvin_intro, response=response)

if __name__ == '__main__':
    app.run(debug=True)
