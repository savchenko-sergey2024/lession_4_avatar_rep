from PIL import Image


monro = Image.open('monro.jpg')
r, g, b = monro.split()
r_monro = r
g_monro = g
b_monro = b

left_pixel_red = int(200)
left_pixel2_red = int(100)
right_pixel_red = int(596)
right_pixel_blue = int(496)
left_pixel2_blue = int(100)
right_pixel2_blue = int(596)
left_pixel_green = int(100)
right_pixel_green = int(596)

coordinates = (left_pixel_red, 0, r_monro.width, r_monro.height)
monro_crop_left_red = r_monro.crop(coordinates)

coordinates2 = (left_pixel2_red, 0, right_pixel_red, monro.height)
monro_crop_middle_red = r_monro.crop(coordinates2)

monro_unification_red = Image.blend(monro_crop_left_red, monro_crop_middle_red, 0.5)


coordinates3 = (0, 0, right_pixel_blue, monro.height)
monro_crop_right_blue = b_monro.crop(coordinates3)

coordinates4 = (left_pixel2_blue, 0, right_pixel2_blue, monro.height)
monro_crop_middle_blue = b_monro.crop(coordinates4)

monro_unification_blue = Image.blend(monro_crop_right_blue, monro_crop_middle_blue, 0.5)


coordinates5 = (left_pixel_green, 0, right_pixel_green, monro.height)
monro_crop_middle_green = g_monro.crop(coordinates5)


new_monro_rgb = Image.merge('RGB', (monro_unification_red, monro_crop_middle_green, monro_unification_blue ))

new_monro_rgb.thumbnail((80, 80) )
new_monro_rgb.save('monro_80_80.jpg')