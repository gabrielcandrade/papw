import simplejson  

x = {
  "id": 123456789,
  "nome": "Rodrigo da Cruz Fujioka",
  "login": "fujioka",
  "email": "rcf4@cin.ufpe.br"
}

y = simplejson.dumps(x)

print(y)