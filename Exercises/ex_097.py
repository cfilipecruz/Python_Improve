def writePretyText(text):
    size = len(text) + 4
    print('=' * size)
    print(text.center(size))
    print('=' * size)


writePretyText('Hello World!')
writePretyText('Its not my fault that you are like that!!')