users = {
      'badieme': {
                'first':'bright',
                'second': 'adieme',
                'location': 'london'
                 },

        'sokoro': {
                 'first': 'sunny',
                 'second': 'okoro',
                 'location': 'gravesend'
                 }         
                 }

for username, user_info in users.items():
    print(f"\nusername: {username}")
    full_name = f"{user_info['first']} {user_info['second']}"
    location = user_info['location']
    print("\tfull name:", full_name.title())
    print("\tlocation:", location.title())



