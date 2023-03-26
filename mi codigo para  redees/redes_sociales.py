from flask import Flask

app = Flask(__name__)

# Definir las rutas que devuelven los enlaces a las redes sociales
@app.route('/instagram')
def instagram():
    return '<a href="https://www.instagram.com/"><i class="fab fa-instagram"></i></a>'

@app.route('/facebook')
def facebook():
    return '<a href="https://www.facebook.com/emerzon.zacarias.75/"><i class="fab fa-facebook-f"></i></a>'

@app.route('/twitter')
def twitter():
    return '<a href="https://twitter.com/"><i class="fab fa-twitter"></i></a>'

@app.route('/youtube')
def youtube():
    return '<a href="https://www.youtube.com/"><i class="fab fa-youtube"></i></a>'

@app.route('/whatsapp')
def whatsapp():
    return '<a href="https://web.whatsapp.com/"><i class="fab fa-whatsapp"></i></a>'

@app.route('/tiktok')
def tiktok():
    return '<a href="https://www.tiktok.com/"><i class="fab fa-tiktok"></i></a>'

# Iniciar la aplicación
if __name__ == '__main__':
    app.run()
