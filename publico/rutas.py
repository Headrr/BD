from flask import render_template, url_for, redirect, request

from . import publico_bp

from ejecutar import conn


@publico_bp.route('/publico/contacto')
def contacto():
    

    operacion = 2+2
    errores = ["sadfkjasdfhkjas"]
    return render_template("contacto/contacto.html", ope = operacion, errores= errores)


@publico_bp.route('/productos_bdS')
def productos_bd():
    
    cur = conn.cursor()
    cur.execute('SELECT * FROM CLIENTE')
    rows = cur.fetchall()
    cur.close()
    return render_template('productos_bdS.html', filas=rows)