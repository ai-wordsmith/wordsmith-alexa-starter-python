import json
try:
  # Load lib assets for Python3
  import urllib.request as ul
  from urllib.error import HTTPError
  python_version = 3
except ImportError:
  # Load lib assets for Python2
  import urllib2 as ul
  from urllib2 import HTTPError
  python_version = 2

def generate(key, proj_slug, temp_slug, data):
  url = 'https://api.automatedinsights.com/v1/projects/{}/templates/{}/outputs'.format(proj_slug, temp_slug)
  headers = {
    'Authorization': 'Bearer {}'.format(key),
    'User-Agent': 'Wordsmith Python Basic SDK',
    'Content-Type': 'application/json'
  }
  if python_version == 3:
    request = ul.Request(url, data=json.dumps({ 'data': data }).encode('utf-8'), headers=headers)
  elif python_version == 2:
    request = ul.Request(url, json.dumps({ 'data': data }), headers)
  else:
    raise ValueError('Error detecting Python version.')
  try:
    response = ul.urlopen(request)
    response_body = response.read().decode('utf-8')
  except HTTPError as err:
    response_body = err.read().decode('utf-8')
  return json.loads(response_body)
