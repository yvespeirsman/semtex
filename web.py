#!/usr/bin/python

from bottle import run, route, template, request, post

@post('/search')
def displayResults():
  query = request.forms.query
  t = template('results.tpl', q=query)
  return t

@route('/')
def show():
  t = template('test.tpl')
  return t

run()

