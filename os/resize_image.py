# Resize Images
# pip install python-resize-image
# pip install Pillow
from PIL import Image
from resizeimage import resizeimage
# Resize by Crop
img = Image.open('image.jpg')
img = resizeimage.resize_crop(img, [100, 100])
img.save('image_resized_crop.jpg', img.format)
# Resize by Cover
img = Image.open('image.jpg')
img = resizeimage.resize_cover(img, [100, 100])
img.save('image_resized_cover.jpg', img.format)
# Resize by Thumbnail
img = Image.open('image.jpg')
img = resizeimage.resize_thumbnail(img, [100, 100])
img.save('image_resized_thumbnail.jpg', img.format)
# Resize by Width
img = Image.open('image.jpg')
img = resizeimage.resize_width(img, 100)
img.save('image_resized_width.jpg', img.format)
# Resize by Height
img = Image.open('image.jpg')
img = resizeimage.resize_height(img, 100)
img.save('image_resized_height.jpg', img.format)