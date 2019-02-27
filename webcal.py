 #!/usr/bin/python3
 # -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, request, url_for, redirect
import calc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return redirect(url_for('final'))

    return render_template('hello.html')
from test import sayHello, loop


@app.route('/final')
def final():
    eins = calc.zahl1_erzeugen()  # erzeugt Zahl, zeigt sie als Aufgabenstellung an UND speichert sie in Datei weg
    zwei = calc.zahl2_erzeugen()  # erzeugt Zahl, zeigt sie als Aufgabenstellung an UND speichert sie in Datei weg
    res = calc.ergebnis_berechnen()
    mytext = calc.aufgabe_stellen()
    return render_template('final.html', text=mytext, zahl1=eins, zahl2=zwei, resultat = res)
    

    
if __name__ == '__main__':
    app.run(debug=True)