#!/usr/bin/env python3
import bottle
import sqlite3


def get_data(dbfile, table):
    db = sqlite3.connect(dbfile)
    cur = db.cursor()
    cur.execute("select * from  {0}".format(table))
    return cur.fetchall()


@bottle.get('/')
def index():
    data = get_data("food.db", "food")
    data.sort()
    return bottle.template('views/welcome.tpl', data=data)


@bottle.get('/addfruit')
def addfruit():
    return bottle.template('views/addfruit.tpl')


@bottle.post('/added')
def added():
    parts = bottle.request.forms
    db = sqlite3.connect('food.db')
    cur = db.cursor()
    cur.execute("insert into food values (?,?,?,?,?,?,?,?)",
                (parts['food'], parts['serving'], parts['satfat'],
                 parts['unsatfat'], parts['fiber'], parts['sugar'],
                 parts['starch'], parts['protein']))
    new_id = cur.lastrowid
    db.commit()
    cur.close

    message = '{0} was added to the database.'.format(parts['food'])

    return bottle.template('views/message.tpl', message=message)


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8090)
