import glob
import os
path = 'D:\Data\Vaynen'

os.chdir(r'D:\Data\Vaynen')
txt_files = glob.glob('*.txt')
print(txt_files)

# for file in txt_files:
#     os.rename(os.path.join(path, file), os.path.join(path, file + '.tmp'))
#
# for filename in txt_files:
#     with open(filename + '.tmp', "r") as f:
#         lines = f.readlines()
#         for idx, line in enumerate(lines):
#             lines[idx] = '1' + line[1:]
#         print(lines)
#     with open(filename, 'w') as f:
#         for line in lines:
#             f.write(line)

for file in txt_files:
    os.remove(os.path.join(path, file + '.tmp'))


