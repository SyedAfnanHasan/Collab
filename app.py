from flask import Flask, jsonify, request

app = Flask(__name__)

# simple in-memory list
tasks = []

# API 1: get all tasks
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# API 2: add a task
@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = data.get("task")

    if task:
        tasks.append(task)

    return jsonify({"message": "Task added", "tasks": tasks})

if __name__ == "__main__":
    app.run(debug=True)

#added changes