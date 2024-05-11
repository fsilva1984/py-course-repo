



tuple_users = (
    ('Maria', 'Ana', 'Lucia',),
    (42, 23, 26,),
    ('Programer', 'CEO', 'Design',),
)

print(f''' 
      nome: {tuple_users[0][0]} 
      idade: {tuple_users[1][0]}
      cargo: {tuple_users[2][1]}
''')

i = 0
for users in tuple_users:
    for user in users:
        print(user)