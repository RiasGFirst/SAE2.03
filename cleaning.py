import os


def remove_null_bytes(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
    cleaned_content = content.replace(b'\x00', b'')
    with open(file_path, 'wb') as file:
        file.write(cleaned_content)

project_dir = 'C:/Users/Rias/PycharmProjects/SAE2.03/drive'
for root, dirs, files in os.walk(project_dir):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            print(f'Cleaning {file_path}')
            remove_null_bytes(file_path)

print("Cleaning complete.")
