import os

path = 'D:/GitHub/LaPeau/LaPeauData/'
for x in ['val', 'train']:
    files = os.listdir(os.path.join(path, 'labels', x))
    for file in files:
        t = os.path.join(path,'labels', x, file)
        boo = False
        with open(t, encoding='utf-8-sig') as f:
            tag = f.readlines()[0][0]
            print(tag)
            if int(tag) == 4:
                p = os.path.join(path, 'images', x, file.split('.')[0] + '.jpg')
                print(p)
                if os.path.exists(p):
                    print(p)
                    os.remove(p)
                boo = True
        if boo:
            os.remove(t)
