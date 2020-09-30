from flask import Flask, render_template, url_for, request,redirect, flash
from forms import contactForm ## instancia de la clase creada en forms.py
from flask_mail import Mail, Message  # 1. Importamos la clase Mail y message

app = Flask(__name__)



app.secret_key = 'clavesecreta'

#app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 465   ## 995
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = False
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = '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'
app.config['MAIL_DEFAUL_SENDER'] = 'apikey'
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
    texto_del_mensaje = form.message.data + form.correo.data

    # message = texto_del_mensaje
    # subject = email_address
    # server = smtplib.SMTP('smtp.gmail.com', 465)      para usar con smtplib
    # server_ssl.ehlo()  
    # server.login('damiandrolas@gmail.com','21509329')
    # server.sendmail('damiandrolas@gmail.com')

    msg = Message( recipients=['damiandrolas@gmail.com'], body= texto_del_mensaje)
    correo.send(msg)
    return redirect(url_for('home'))

  return render_template('contacto.html', form = form)

@app.route('/pricing') ## ruta para pagina principal
def pricing():
    return render_template('pricing.html')



if __name__ == '__main__':
    app.run()         ## mantiene abierta la app para escuchar  debug=True modo de prueba





