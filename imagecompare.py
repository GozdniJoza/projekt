import imp
from PIL import Image
import imagehash

hash = imagehash.average_hash(Image.open('images/image.png'))

another_hash = imagehash.average_hash(Image.open('images/image2.png'))

cutoff = 16
print(hash)
print(another_hash)

if(hash == another_hash):
    print("Similar")
else:
    print("Not similar")