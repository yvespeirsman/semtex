#!/usr/bin/python

from bottle import run, route, template, request, post, static_file, debug
import ElasticQuery

@post('/search')
def displayResults():
  queryTerm = request.forms.query
  query = ElasticQuery.ElasticQuery()
  results = query.submit("text",queryTerm)
  t = template('templates/results.tpl', q=queryTerm, r=results)
  return t

@route('/')
def show():
  t = template('templates/index.tpl')
  return t

@route('/docs/<filename:re:.*>')
def getDocument(filename):
  query = ElasticQuery.ElasticQuery()
  print "id", filename
  results = query.submit("docid",str(filename))
  print type(results)
  if len(results) > 0:
    text = " ".join(results[0]["text"])
  else:
    text = "Document not found"
  t = template('templates/doc.tpl', b=text)
  return t

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

debug(True)
run()

