import os
path = f'D:\GitHub\LaPeau\LaPeauData\Train'
folders = ['BaKhoang', 'VayNen', 'DaVayCa', 'Zona']

base = 0
for folder in folders:
    maxi = 0
    print(base)
    data_path = os.path.join(path, folder)
    files = os.listdir(data_path)
    print(files)

    for file in files:
        idx = file.split('.')[0]
        maxi = max(maxi, int(idx))
        new_file_exten_name = 'tmp1' if file.endswith('.jpg') else 'tmp2'
        new_file = idx + '.' + new_file_exten_name
        old_file_path = (os.path.join(path, folder, file))
        new_file_path = (os.path.join(path, folder, new_file))
        os.rename(old_file_path, new_file_path)
    files = os.listdir(data_path)
    for file in files:
        idx = file.split('.')[0]
        maxi = max(maxi, int(idx))
        new_file_exten_name_rev = 'jpg' if file.endswith('tmp1') else 'txt'
        new_file = str(int(idx) + base) + '.' + new_file_exten_name_rev
        old_file_path = (os.path.join(path, folder, file))
        new_file_path = (os.path.join(path, folder, new_file))
        print(old_file_path, new_file_path)
        os.rename(old_file_path, new_file_path)
    base += maxi + 1

print()
files = os.listdir(path)


print(files)

