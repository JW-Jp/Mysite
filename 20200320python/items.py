from jinja2 import Template

def getHtml(user):
  with open('alica.html') as f:
      s= f.read()
  return s

def main():
  item_list = [
    {"name": 'apple', "count": 50}
    {"name": 'papaya', 'count': 90}
    {"name": 'melon', 'count': 20}
  ]

  tmpl = Template(welcomeHtml())
  print(tmpl.render(user))

main()