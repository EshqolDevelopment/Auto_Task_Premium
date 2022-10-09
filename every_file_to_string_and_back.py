import base64

def convert_to_bytes(path):
    with open(path, "rb") as f:
        converted_string = base64.b64encode(f.read())

    with open(path, "w") as f:
        f.write(str(converted_string))

def convert_to_source(path):
    with open(path, "r") as f:
        string_to_file = f.read()

    string_to_file = string_to_file[2:-1]
    string_to_file_final = bytes(string_to_file.encode("utf-8"))

    decodeit = open(path, "wb")
    decodeit.write(base64.b64decode(string_to_file_final))

