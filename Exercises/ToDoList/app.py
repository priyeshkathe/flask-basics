from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

TASKS = []
task_id_counter = 1


@app.route('/')
def home():
    return render_template('index.html', tasks=TASKS)


@app.route('/add', methods=['GET', 'POST'])
def add_task():
    global task_id_counter

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        due_date = request.form.get('due_date', '')

        TASKS.append({
            'id': task_id_counter,
            'title': title,
            'description': description,
            'priority': priority,
            'status': 'Pending',
            'due_date': due_date,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
        })

        task_id_counter += 1
        return redirect(url_for('home'))

    return render_template('add_task.html')


@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((t for t in TASKS if t['id'] == task_id), None)

    if not task:
        return redirect(url_for('home'))

    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        task['priority'] = request.form['priority']
        task['status'] = request.form['status']
        task['due_date'] = request.form.get('due_date', '')
        return redirect(url_for('home'))

    return render_template('edit_task.html', task=task)


@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in TASKS:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            break
    return redirect(url_for('home'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global TASKS
    TASKS = [t for t in TASKS if t['id'] != task_id]
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)