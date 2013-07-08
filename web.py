#!/usr/bin/python

from bottle import run, route, template, request, post
import ElasticQuery

@post('/search')
def displayResults():
  queryTerm = request.forms.query
  query = ElasticQuery.ElasticQuery()
  results = query.submit(queryTerm)
  print results
  t = template('templates/results.tpl', q=queryTerm, r=results)
  return t

@route('/')
def show():
  t = template('templates/index.tpl')
  return t

run()

