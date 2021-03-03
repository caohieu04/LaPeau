import os
import shutil
path = f'D:\GitHub\LaPeau\LaPeauData'
folders = ['BaKhoang', 'VayNen', 'DaVayCa', 'Zona', 'UngThu']

base = 0
cnt = 0

def rename():
    for folder in folders:
        maxi = 0
        print(base)
        data_path = os.path.join(path, folder)
        files = os.listdir(data_path)
        files.sort()
        print(files)
        cnt_temp = base
        for idx in range(len(files)):
            if idx % 2 == 0:
                print(cnt_temp, (files[idx], files[idx + 1]))

                def rename(i, idx):
                    new_file_name = 'i' + str(i) + '.' + files[idx].split('.')[1]
                    old_file_path = (os.path.join(path, folder, files[idx]))
                    new_file_path = (os.path.join(path, folder, new_file_name))
                    print(old_file_path, new_file_path)
                    os.rename(old_file_path, new_file_path)
                rename(cnt_temp, idx)
                rename(cnt_temp, idx + 1)
                cnt_temp += 1
        base = cnt_temp

def transform():
    path_images = os.path.join(path, 'images')
    if not os.path.exists(path_images):
        os.makedirs(path_images)
    path_labels = os.path.join(path, 'labels')
    if not os.path.exists(path_labels):
        os.makedirs(path_labels)

    for folder in folders:
        files = os.listdir(os.path.join(path, folder))
        for file in files:
            if file.endswith('jpg'):
                shutil.move(os.path.join(path, folder, file), path_images)
            else:
                shutil.move(os.path.join(path, folder, file), path_labels)
    for folder in folders:
        path_folder = os.path.join(path, folder)
        shutil.rmtree(path_folder, ignore_errors=True)

rename()
transform()


