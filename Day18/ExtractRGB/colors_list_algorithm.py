import colorgram

image_file = "C:\PY\Day18\ExtractRGB\spot_painting.jpg"

rgb_colors = ()
color_list = []

colors = colorgram.extract(image_file, 20)

for color in colors:
    rgb = color.rgb
    rgb_colors = (rgb.r, rgb.g, rgb.b)
    color_list.append(rgb_colors)

print(color_list)
