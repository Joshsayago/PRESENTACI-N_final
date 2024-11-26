from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista para agregar las tareas
tareas = []


@app.route('/')
def index():
    return render_template('página.html', tareas=tareas)


@app.route('/add_tarea', methods=['POST'])
def manage_tarea():
    actividad = request.form.get('actividad')
    categoria = request.form.get('categoria')

    if actividad and categoria:
        if actividad == 'robar':
            actividad = 'Actividad no programable'
        tareas.append({'actividad': actividad, 'categoria': categoria})
    return render_template('página.html', tareas=tareas)

@app.route('/get_tarea', methods=['GET'])
def get_tarea():
    actividades = [tarea['actividad'] for tarea in tareas]
    return jsonify(actividades)

@app.route('/delete_tarea', methods=['POST'])
def delete_tarea():
    actividad_a_eliminar = request.form.get('actividad')

    global tareas
    tareas = [tarea for tarea in tareas if tarea['actividad'] != actividad_a_eliminar]
    return render_template('página.html', tareas=tareas)


if __name__ == '__main__':
    app.run(debug=True)
