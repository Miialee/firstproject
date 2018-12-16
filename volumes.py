def volume():
    volumes=[1, 5, 8, 6, 45, 18, 2, 8, 85]
    for name in volumes:
        if name>40:
            print(str(name) + "is too loud")
        else:
            print(str(name) + "is too low")
volume()
