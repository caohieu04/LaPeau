import pyheif
from PIL import Image


 def decodeImage(bytesIo):
     i = pyheif.read_heif(bytesIo)

     # Extract metadata etc
     for metadata in i.metadata or []:
         if metadata['type']=='Exif':
             # do whatever

     # Convert to other file format like jpeg
     s = io.BytesIO()
     pi = Image.frombytes(
            mode=i.mode, size=i.size, data=i.data)

     pi.save(s, format="jpeg")
