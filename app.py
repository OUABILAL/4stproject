from flask import Flask, render_template, request, redirect

# Create the Flask app
app = Flask(__name__)

# Initialize an empty list to store tasks
tasks = []

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route for adding a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:  # If the user entered a task
        tasks.append(task)  # Add the task to the list
    return redirect('/')  # Redirect back to the home page

# Route for deleting a task
@app.route('/delete/<int:task_id>', methods=['GET'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):  # Check if the task ID is valid
        tasks.pop(task_id)  # Remove the task from the list
    return redirect('/')  # Redirect back to the home page

if __name__ == '__main__':
    app.run(debug=True)
