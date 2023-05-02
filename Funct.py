FILEPATH='Todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return list items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_write, filepath=FILEPATH):
    """ Write item in the text file."""
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_write)


#print('Hello')