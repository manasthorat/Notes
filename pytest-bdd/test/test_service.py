import requests
from pytest_bdd import scenarios, parsers, given, then

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'

scenarios('../features/service.feature')

CONVERTERS = {
  'code': int,
  'phrase': str,
}

@given(
  parsers.parse('the DuckDuckGo API is queried with "{phrase}"'),
  target_fixture='ddg_response',
  converters=CONVERTERS)
def ddg_response(phrase):
  params = {'q': phrase, 'format': 'json'}
  response = requests.get(DUCKDUCKGO_API, params=params)
  return response

@then(
  parsers.parse('the response contains results for "{phrase}"'),
  converters=CONVERTERS)
def ddg_response_contents(ddg_response, phrase):
  # A more comprehensive test would check 'RelatedTopics' for matching phrases
  assert phrase.lower() == ddg_response.json()['Heading'].lower()

@then(
  parsers.parse('the response status code is "{code}"'),
  converters=CONVERTERS)
def ddg_response_code(ddg_response, code):
  assert ddg_response.status_code == code