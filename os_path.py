import os
import time

# Объединить два файла

filenames = [r'C:\Python\test\text1.txt', r'C:\Python\test\text2.txt']

with open(r'C:\Python\test\output_file.txt', 'w') as outfile:
    for filename in filenames:
        with open(filename) as infile:
            for line in infile:
                outfile.write(line)

with open(r'C:\Python\test\output_file.txt') as f:
    print(f.read())


# Если файл существует, вывести его имя, директорию и время последнего доступа.

# path = r'test\text1.txt'
#
# if os.path.exists(path):
#     dirs, name = os.path.split(path)
#     access = os.path.getatime(path)
#     print(f'{name} ({dirs}) - last access time '
#           f'{time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(access))}')
#
# else:
#     print(f"File {path} doesn't exist!")

