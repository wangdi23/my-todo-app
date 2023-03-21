contents = ['a is the sky', 'b is the space', 'c is the earth']
filenames = ['a,txt', 'b.txt', 'c.txt']

for content, filename in zip(contents, filenames):
    file = open(f"{filename}", 'w')
    file.write(content)

