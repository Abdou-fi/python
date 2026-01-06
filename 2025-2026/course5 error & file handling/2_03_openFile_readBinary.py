# f = open("Al-Aqsa.jpg", "br")
# print(f.read())
# f.close()

from PIL import Image
img=Image.open('Al-Aqsa.jpg')  #original image
img.show()
mirror_image=img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_image.save('Al-Aqsa_mirror.jpg')
Image.open('Al-Aqsa_mirror.jpg').show()  #mirrored image
