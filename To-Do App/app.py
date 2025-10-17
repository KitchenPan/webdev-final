from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# In-memory list to hold tasks
tasks = []

# Read the HTML file
def get_html():
    with open("index.html") as f:
        return f.read()

@app.route('/')
def index():
    html = get_html()
    return render_template_string(html, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
