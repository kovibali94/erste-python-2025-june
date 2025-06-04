def generate_id(n):
    id = n + 1
    while True:
        yield id
        id += 1
    

ids = generate_id(10)

for id in ids:
    print(id)
    # if id > 255:
    #     ids.throw(ValueError('Can not store larger values than 255'))

    if id > 255:
        ids.close()
