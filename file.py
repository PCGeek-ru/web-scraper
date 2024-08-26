def write_file(path, content, mode='wb'):
    with open(path, mode) as file:
        file.write(content)
