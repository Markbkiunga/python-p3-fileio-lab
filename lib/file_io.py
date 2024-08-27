def write_file(file_name, file_content):
    pass
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as f:
        f.write(file_content)


def append_file(file_name, append_content):
    pass
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as f:
        f.write(append_content)


def read_file(file_name):
    pass
    with open(f'{file_name}.txt', encoding='utf-8') as f:
        file_content_read = f.read()
    return file_content_read
