from flask import Flask, render_template, flash, request, session, redirect, url_for
from RoomForm import RoomForm
from AddInfo import AddForm

import sqlite3
from bs4 import BeautifulSoup
import requests
roomconn=sqlite3.connect('room.db',  check_same_thread=False)
roomcurr= roomconn.cursor()
app=Flask(__name__)
app.secret_key='test'

@app.route('/', methods=['GET', 'POST'])
def index():
    room=RoomForm(request.form)
    if request.method=='POST':
        if(room.validate()):
            return redirect(url_for('room', value=request.form['text']))
    return render_template('index.html', form=room)

@app.route('/room/<value>', methods=['GET', 'POST'])
def room(value):
    add=AddForm(request.form)

    if(request.method=='POST'):
        if add.validate():
            roomcurr.execute('INSERT INTO Rooms VALUES(?,?,?,?,?)', (request.form['idd'],value, request.form['content'], request.form['typed'], request.form['group']))
            roomconn.commit()
            return redirect(url_for('room',value=value))
    roomcurr.execute("SELECT * FROM Rooms WHERE  ROOM=(?)",(value,))
    roomall=roomcurr.fetchall()
    if(len(roomall)==0):
        return render_template('roomvals.html', form=add, vals=None)
    else:
        return render_template('roomvals.html', form=add, vals=roomall)

@app.route('/room/delete/<value>')
def delval(value):
    roomcurr.execute('DELETE FROM Rooms WHERE ID=?',(value,))
    roomconn.commit()
    return redirect(url_for('room', value=value))



app.run(debug=True)
