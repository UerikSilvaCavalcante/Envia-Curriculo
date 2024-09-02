from flask import Flask, render_template, redirect, request, flash
from time import sleep
from envio_email import enviar_email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'UERIK'

@app.route('/')
def home():
    return render_template('envia.html')

@app.route('/envia', methods=['POST'])
def envia():
    email = request.form.get('email') 
    assunto = request.form.get('assunto') 
    vaga = request.form.get('Vaga') 

    # print(email, vaga, assunto)
    resp = enviar_email(email, assunto, vaga)
    
    flash(resp)

    return redirect('/')



if __name__ in '__main__':
    app.run(debug=True)