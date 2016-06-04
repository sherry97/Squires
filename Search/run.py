#!/usr/bin/env python3
import bottle

@bottle.get('/')
def index():
    return bottle.template('views/search.tpl')


@bottle.post('/searched')
def added():
    parts = bottle.request.forms

    return parts.getunicode("skills")

bottle.debug(True)
bottle.run(host='0.0.0.0', port=8090)
