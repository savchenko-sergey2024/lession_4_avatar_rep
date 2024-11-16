

from PIL import Image

#
# image = Image.open("example.jpg")
# rotated_image = image.rotate(45)
# rotated_image.save("rotated.jpg", format="JPEG" )
# # print(rotated_image.mode)
# # print(rotated_image.height)
# print(rotated_image.width)
# image_lenna = Image.open("lenna.jpg")
# image_lenna_rgb = image_lenna.convert("RGB")
# image_lenna_rgb.save("lenna_rgb.jpg")
# print(image_lenna_rgb.mode)
#
# image_monro_blue = Image.open("blue_monro.jpg",)
# image_monro_green = Image.open("green_monro.jpg",)
# image_monro_red = Image.open("red_monro.jpg",)
#
# # r, g, b = image_monro.split()
# # r.save("red_monro.jpg")
# # g.save('green_monro.jpg')
# # b.save('blue_monro.jpg')
# # image_monro.split('red')
# # image_monro.save(("11.jpg"))
#
# new_monro = Image.merge("RGB", (image_monro_red, image_monro_green, image_monro_blue))
# new_monro.save('new_monro.jpg')

# monro_unification = Image.open("red_monro.jpg")

left_pixel = int(200)
left_pixel2 = int(100)
right_pixel = int(596)
# coordinates = (left_pixel, 0, monro_unification.width, monro_unification.height)
# monro_unification_left = monro_unification.crop(coordinates)
# monro_unification_left.save('monro_left.jpg')

# monro_unification2 = Image.open("red_monro.jpg")
# coordinates2 = (left_pixel2, 0, right_pixel, 522)
# monro_unification2_middle = monro_unification2.crop(coordinates2)
# monro_unification2_middle.save('monro_middle.jpg')
# monro_unification_left = Image.open('monro_left.jpg')
# monro_unification2_middle = Image.open('monro_middle.jpg')
# monro_unification3 = Image.blend(monro_unification_left, monro_unification2_middle, 0.5)
# monro_unification3.save('monro_unification3.jpg')



# monro_unification = Image.open("blue_monro.jpg")

right_pixel = int(496)
left_pixel2 = int(100)
right_pixel2 = int(596)
# coordinates = (0, 0, right_pixel, monro_unification.height)
# monro_unification_left = monro_unification.crop(coordinates)
# monro_unification_left.save('monro_left_blue.jpg')
#
# monro_unification2 = Image.open("blue_monro.jpg")
# coordinates2 = (left_pixel2, 0, right_pixel2, 522)
# monro_unification2_middle = monro_unification2.crop(coordinates2)
# monro_unification2_middle.save('monro_middle_blue.jpg')
# monro_unification_left = Image.open('monro_left_blue.jpg')
# monro_unification2_middle = Image.open('monro_middle_blue.jpg')
# monro_unification3 = Image.blend(monro_unification_left, monro_unification2_middle, 0.5)
# monro_unification3.save('monro_unification_blue.jpg')


# monro_unification_green = Image.open('green_monro.jpg')
# coordinates2 = (left_pixel2, 0, right_pixel2, 522)
# monro_crop_middle_green = monro_unification_green.crop(coordinates2)
# monro_crop_middle_green.save('monro_middle_green.jpg')

# monro_crop_middle_green = Image.open('monro_middle_green.jpg')
# monro_unification_red = Image.open('monro_unification_red.jpg')
# print(monro_crop_middle_green.width, monro_crop_middle_green.height, '\n', monro_unification_red.width, monro_unification_red.height)

# monro_unification_red = Image.open('monro_unification_red.jpg')
# monro_crop_middle_green = Image.open('monro_middle_green.jpg')
# monro_unification_blue = Image.open('monro_unification_blue.jpg')
# print(monro_unification_red.mode, monro_crop_middle_green.mode, monro_unification_blue.mode)
# new_monro_rgb = Image.merge('RGB', (monro_unification_red, monro_crop_middle_green, monro_unification_blue ))
# new_monro_rgb.save('new_monro_rgb.jpg')

monro_80_80 = Image.open('new_monro_rgb.jpg')
monro_80_80.thumbnail((80, 80) )
monro_80_80.save('monro_80_80.jpg')