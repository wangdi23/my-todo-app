FILEPATH = 'file/todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list
     of to-do items
    """
    with open(filepath, 'r') as file_local:
        # this is recommended in file
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ write the to-do item in a text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print('i am from functions')
print(__name__)
if __name__ == "__main__":
    print('executed only in this file')