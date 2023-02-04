import zipfile

with zipfile.ZipFile("example.jar", "r") as jar:
    jar.extractall()

with open("example.txt", "w") as text_file:
    with open("example.jar", "r") as jar_file:
        text_file.write(jar_file.read())
