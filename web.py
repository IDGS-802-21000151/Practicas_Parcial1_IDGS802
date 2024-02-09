from flask import Flask, request, render_template
import math

import forms

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def cargarInicio():
    if request.method == "GET":
        return render_template("operaciones.html")
    
    elif request.method == "POST":
        tipoOperacion = request.form.get("tipoOperacion")
        primerNumero = request.form.get("primerNumero")
        segundoNumero = request.form.get("segundoNumero")
            
        if tipoOperacion == "sumar":
            resultado = float(primerNumero) + float(segundoNumero)
            operacion = f"{primerNumero} + {segundoNumero}"
        elif tipoOperacion == "restar":
            resultado = float(primerNumero) - float(segundoNumero)
            operacion = f"{primerNumero} - {segundoNumero}"
        elif tipoOperacion == "dividir":
            resultado = float(primerNumero) / float(segundoNumero)
            operacion = f"{primerNumero} / {segundoNumero}"
        elif tipoOperacion == "multiplicar":
            resultado = float(primerNumero) * float(segundoNumero)
            operacion = f"{primerNumero} x {segundoNumero}"
    
        return render_template("operaciones.html", resultado=resultado, tipoOperacion=tipoOperacion, operacion = operacion)

@app.route("/calculadora-resistencias", methods=["GET", "POST"])
def cargarCalculadoraInicio():
    resistenciasFormulario = forms.ResistenciaFormulario(request.form)
    
    if(request.method == "POST"):
        print("LLEGO METODO POST")
        primeraBanda = resistenciasFormulario.primeraBanda.data
        segundaBanda = resistenciasFormulario.segundaBanda.data
        
        valorBandas = int(str(primeraBanda) + str(segundaBanda))
        
        multiplicador = int(resistenciasFormulario.multiplicador.data)
        
        toleranciaCompleto = int(resistenciasFormulario.tolerancia.data)
        
        print(f"Tolerancia antes: {toleranciaCompleto}")
        
        tolerancia = float(toleranciaCompleto * 0.01)
        
        print(f"Tolerancia después: {tolerancia}")
        
        valor = valorBandas * multiplicador
        
        valorMaximo = valor + (valor * tolerancia)
        valorMinimo = valor - (valor * tolerancia)
        
        resultado = {
            "primeraBanda": str(primeraBanda),
            "segundaBanda":  str(segundaBanda),
            "multiplicador": "x" + str(multiplicador),
            "tolerancia":  str(toleranciaCompleto),
            "valor":  str(valor),
            "valorMaximo":  str(valorMaximo),
            "valorMinimo":  str(valorMinimo)
        }
        
        print(resultado)
        
        return render_template("resistencias.html", resistenciasFormulario = resistenciasFormulario, resultado = resultado)
        
    return render_template("resistencias.html", resistenciasFormulario = resistenciasFormulario)

@app.route("/distancia-entre-puntos", methods=["GET", "POST"])
def cargarAlumnos():
    distanciaFormulario = forms.distanciaFormulario(request.form)
    
    if request.method == "POST":
        x1 = int(distanciaFormulario.x1.data)
        y1 = int(distanciaFormulario.y1.data)
        x2 = int(distanciaFormulario.x2.data)
        y2 = int(distanciaFormulario.y2.data)
        
        distanciaCalculada = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        
        print(f"Primer punto: {x1}")
        print(f"Segundo punto: {y1}")
        print(f"Tercer punto: {x2}")
        print(f"Cuarto punto: {y2}")
    
    return render_template("distancias.html", form = distanciaFormulario, distanciaCalculada = distanciaCalculada)

if __name__ == "__main__":
    app.run(debug=True)