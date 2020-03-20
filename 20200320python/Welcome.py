from Jinja2 import Template

def welcomeHtml(user):
  with open('alica.html') as f:
      s= f.read()
  return s

def main():
  user = {"name": 'Alice', "likes": 100}
  print( welcomeHtml(user))

  tmpl = Template(welcomeHtml())
  print(tmpl.render(user))

main()