from pyais.stream import FileReaderStream

filename = "2018090407.txt"

for msg in FileReaderStream(filename):
    decoded = msg.decode()
    json = decoded.to_json()
    print(json)
