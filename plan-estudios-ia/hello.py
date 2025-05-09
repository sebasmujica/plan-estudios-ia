# render_template ----> Nos permite retornar el Html en el return de las funciones
from flask import Flask, render_template, request, redirect, url_for
from dicc_converter import lista_a_dicc
from config import PREGUNTAS_AISLADAS , RESPUESTAS_DIC
from Deepseek import Open_IA, Open_IA_eval, Open_IA_nivel
import re
dic = {}
# def funcion_ruta2(dic):  #Funcion que debe correr dentro de la ruta 2
    
#     if request.method == "POST":
#       for i in range(len(PREGUNTAS_AISLADAS)):
#           respuesta = request.form.get(f"respuesta{i}")
#           dic[PREGUNTAS_AISLADAS[i]] = respuesta
#       return redirect(url_for("part3"))
    

# preguntas_de_la_IA = [{'role': 'system', 'content': 'generas 5 preguntas simples(solo las preguntas) sobre python'}, 
#              {
#                  'role': 'assistant', 
#                  'content': '1. ¿Qué es Python y para qué se utiliza?  \n2. ¿Cuál es la diferencia entre una lista y una tupla en Python?  \n3. ¿Cómo se define una función en Python?  \n4. ¿Qué tipos de bucles existen en Python y cómo funcionan?  \n5. ¿Qué es un módulo en Python y cómo se importa?'
                 
                 
#                  }]
    
# preguntas = preguntas_de_la_IA[1]['content']
promp_default = "generas 5 preguntas simple sobre python(solo preguntas) para evaluar el nivel"
preguntas_ia = Open_IA(promp_default)
PREGUNTAS_AISLADAS = re.findall(r"\d+[.] (.+)",preguntas_ia)
#Instancia creada con el argumetro __name__. Permite a la aplicacion saber si esta siendo ejecutada desde un archivo principal o esta siendo importada. 
#Sabe donde buscar los archivos Html gracias a el parametro 
app= Flask(__name__)  
#Creamos la ruta, que en este caso sera la pagina principal de nuestra web ya que su 'direccion' solo es "/"
#Como por ejemplo en www.google.com'/'
@app.route("/") # Cuando accedamos a la ruta '/' se ejecuta las funciones debajo
def index():
    #Se ejecuta la funcion de generar preguntas
    return render_template("parte1.html")
#el nombre de la derecha es la variable que estoy extrayendo de mi funcion y el nombre de la izquierda es la variable que el archivo Html
# va a recibir


#Creamos la ruta '/contacto' y se pasamos la variable de tipo String 'nombre'
@app.route("/Parte2.html",methods = ["GET","POST"])
def contacto():
  if request.method == "POST":
    for i in range(len(PREGUNTAS_AISLADAS)):
      respuesta = request.form.get(f"respuesta{i}")
      dic[PREGUNTAS_AISLADAS[i]] = respuesta
      print("Diccionario final:",dic )
    return redirect(url_for("part3"))
  return render_template("parte2.html",PREGUNTAS_AISLADAS=PREGUNTAS_AISLADAS)



@app.route("/part3")
def part3():
    # evaluacion_IA_nivel = Open_IA_nivel(dic)
    evaluacion_IA_plan = Open_IA_eval(dic)
    print(evaluacion_IA_plan)

    return render_template("parte3.html", evaluacion_IA_plan=evaluacion_IA_plan)

''' Si queremos unicamente variables usamos {{ }} pero si queremos usar (if - else), (for) debemos usar {% %}, esto es de Jinja para los archivos 
Html '''







#Basicamente permite actiovar el debbuger para que al realizar un cambio no tengamos que 
# cerrar la base de datos y volverla a activar en la terminal
if __name__ == "__main__":
    app.run(debug=True)
