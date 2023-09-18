# nome = input("digite um nome: \n")

# def teste(name):
#     print("teste: ", name)

# teste(nome)

users = [
  {
    "id": 1, 
    "name": "Allan", 
    "age": 27, 
    "profile_picture": "http://…", 
    "city": "São Paulo"
  },
  {
    "id": 2, 
    "name": "Julie", 
    "age": 29, 
    "profile_picture": "http://…", 
    "city": "Curitiba"
  },
  {
    "id": 3, 
    "name": "Pedro", 
    "age": 31, 
    "profile_picture": "http://…", 
    "city": "Rio de Janeiro"
  }
]

filtered_users = filter(lambda user: user["age"] == 27, users)

print(list(filtered_users))