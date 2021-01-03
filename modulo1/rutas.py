from flask import render_template, url_for, redirect, request

from . import modulo1_bp

from ejecutar import conn

from flask_login import current_user

class Persona:
    
    nombre = ""
    apellido = ""
    
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


@modulo1_bp.route('/modulo1/contacto')
def contacto():
    
    if current_user.is_authenticated:
        return 'wena llego'
    
    p1 = Persona("Daniel","Moran")
    operacion = 2+2
    errores = ["sadfkjasdfhkjas"]
    print(url_for('publico.contacto'))
    return render_template("contacto/contacto.html", ope = operacion, persona = p1, errores= errores)


