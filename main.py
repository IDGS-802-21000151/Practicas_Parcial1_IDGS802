from flask import Flask, request, render_template

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

if __name__ == "__main__":
    app.run(debug=True)