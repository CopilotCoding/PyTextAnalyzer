import codecs

with open("input.txt", "rb") as file:
    data = file.read()
    if data.startswith(codecs.BOM_UTF8):
        print("File is UTF-8 encoded")
    elif data.startswith(codecs.BOM_UTF16_LE):
        print("File is UTF-16 (little-endian) encoded")
    elif data.startswith(codecs.BOM_UTF16_BE):
        print("File is UTF-16 (big-endian) encoded")
    else:
        try:
            data.decode('ascii')
            print("File is ANSI encoded")
        except UnicodeDecodeError:
            print("File encoding is unknown")
input()
