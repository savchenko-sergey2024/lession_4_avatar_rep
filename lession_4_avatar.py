from PIL import Image


monro_unification_red = Image.open('monro_unification_red.jpg')
monro_crop_middle_green = Image.open('monro_middle_green.jpg')
monro_unification_blue = Image.open('monro_unification_blue.jpg')

new_monro_rgb = Image.merge('RGB', (monro_unification_red, monro_crop_middle_green, monro_unification_blue ))
new_monro_rgb.save('new_monro_rgb.jpg')

monro_80_80 = Image.open('new_monro_rgb.jpg')
monro_80_80.thumbnail((80, 80) )
monro_80_80.save('monro_80_80.jpg')