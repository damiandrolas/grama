from flask import Flask, render_template, url_for, request,redirect, flash
from forms import contactForm ## instancia de la clase creada en forms.py
from flask_mail import Mail, Message  # 1. Importamos la clase Mail y message
import os

app = Flask(__name__)



app.secret_key = '\x1e\xccV\x8e\xef\xa3\xa5\xfc\xfa\xa4R\xff\xfbQ\xe6\xb4\x91!\xd5\xea"\xa1B\x15HM\xd5&\x192\x82\xf1Y\x81#iS\x90\x0cO\xd7M\x96\xc2\xb2\x9a\x9d\xb6\xee\x9d'

#app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465   ## 995
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') 
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
#app.config['MAIL_DEFAUL_SENDER'] = 
app.config['MAIL_MAX_EMAILS'] = 5
#app.config['MAIL_SUPPRESS_SEND']
app.config['MAIL_ASCII_ATTACHMENT'] = False

correo = Mail(app)


@app.route('/') ## ruta para pagina principal
def home():
    return render_template('home.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
  form = contactForm() 
  if form.validate_on_submit():
    flash('Mensaje enviado exitosamente', 'success')
    email_address = form.correo.data
    texto_del_mensaje = form.message.data

    # message = texto_del_mensaje
    # subject = email_address
    # server = smtplib.SMTP('smtp.gmail.com', 465)      para usar con smtplib
    # server_ssl.ehlo()  
    # server.login('damiandrolas@gmail.com','21509329')
    # server.sendmail('damiandrolas@gmail.com')

    msg = Message(email_address, sender='damiandrolas@gmail.com', recipients=['damiandrolas@gmail.com'], body= texto_del_mensaje)
    correo.send(msg)
    return redirect(url_for('home'))

  return render_template('contacto.html', form = form)

@app.route('/pricing') ## ruta para pagina principal
def pricing():
    return render_template('pricing.html')



if __name__ == '__main__':
    app.run(debug = True)         ## mantiene abierta la app para escuchar  debug=True modo de prueba





