import hashlib

original_file = 'Zespol2.bmp'
modified_file = 'Zespol2_modified.bmp'

with open(original_file, 'rb') as file:
    original_data = file.read()
    original_hash = hashlib.sha256(original_data).hexdigest()

print(f"Hash SHA256 dla oryginalnego obrazu: {original_hash}")

data = bytearray(original_data)

data[0] = data[0] ^ 0x01

with open(modified_file, 'wb') as file:
    file.write(data)

print(f"Zmiana jednego bajtu została wykonana i zapisana w pliku: {modified_file}")

with open(modified_file, 'rb') as file:
    modified_data = file.read()
    modified_hash = hashlib.sha256(modified_data).hexdigest()

print(f"Hash SHA256 dla zmodyfikowanego obrazu: {modified_hash}")
