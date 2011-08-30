def save_file(f):
    print(f.name)
    print(f.size)
    destination = open('test', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
