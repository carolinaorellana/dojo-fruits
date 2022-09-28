from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    frutilla = request.form['strawberry']
    frambuesa=request.form['raspberry']
    manzana=request.form['apple']
    nombre=request.form['first_name']
    apellido=request.form['last_name']
    estudiante= request.form['student_id']
    total = int(frutilla) + int (frambuesa) + int(manzana)

    print(f"Cobrando a {nombre} por {total} frutas")
    
    return render_template("checkout.html", frutilla=frutilla, frambuesa=frambuesa, manzana=manzana, nombre=nombre, apellido=apellido, estudiante=estudiante, total=total)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")


if __name__=="__main__":   
    app.run(debug=True)    