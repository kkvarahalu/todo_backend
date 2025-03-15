from flask import Flask, jsonify,request,abort
from flask_cors import CORS
from database import get_db_connection

app = Flask(__name__)
CORS(app)


@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn=get_db_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute('select * from tasks')
    tasks=cursor.fetchall()
    conn.close()
    return jsonify(tasks)

@app.route('/tasks',methods=['POST'])
def add_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    title=request.json['title']
    description=request.json.get('description','')
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute('insert into tasks(title,description)values(%s,%s)',(title,description))
    conn.commit()
    conn.close()
    return jsonify({'status':'task added!'}),201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if not request.json:
        abort(400)
    completed = request.json.get('completed', False)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE task SET completed = %s WHERE id = %s', (completed, task_id))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Task updated!'})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Task deleted!'})

if __name__ == '__main__':
    app.run(debug=True)



