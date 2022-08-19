from time import clock_settime
from pyais.stream import FileReaderStream

filename = "sample.ais"

for msg in FileReaderStream(filename):
    decoded = msg.decode()
    json = decoded.to_json()
    print(json)
clock_settime