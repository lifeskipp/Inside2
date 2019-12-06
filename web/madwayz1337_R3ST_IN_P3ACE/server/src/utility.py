def gentext(length):
    import random
    return ''.join([chr(random.randint(65, 90)) if random.randint(0, 1) else chr(random.randint(97, 122)) for _ in range(length)])

def create_error(message):
    return dict(error=dict(message=message))

# def gen_users(quantity):
#     db = Provider
#
#     for i in range(2, quantity + 2):
#         login = gentext(8)
#         token = jwt.encode({'id': i, 'role': random.randint(0, 2)}, app.config['SECRET_KEY']).decode()
#         db.insert_users({'login': login, 'token': token})
#
#     return db.get_users()

