from pyais.stream import FileReaderStream

filename = "nmea_data_sample.txt"

for msg in FileReaderStream(filename):
    decoded = msg.decode()
    json = decoded.to_json()
    print(json)
