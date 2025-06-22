import os
from flask import Flask, render_template, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Task {self.id}: {self.content}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    app_mode = os.getenv("ENV_VAR", "base")

    if app_mode == "1":
        banner = "variable is now set to 1"
    elif app_mode == "2":
        banner = "variable is now set to 2"
    else:
        banner = "No variable has been set"

    if request.method == 'POST':
        task_content = request.form['content']
        if task_content.strip():
            new_task = Task(content=task_content)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('index'))

    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks, banner=banner)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Task.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
