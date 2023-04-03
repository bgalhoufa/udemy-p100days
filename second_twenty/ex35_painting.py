import colorgram as cg

my_colors = [(207, 160, 82), (54, 89, 130), (145, 91, 40), (139, 27, 49), (222, 206, 109), (132, 176, 202)]
my_extract = cg.extract('hirst_image.jpg', 10)
#my_color = cg.Color.rgb
my_list = []

for i in my_extract:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    my_list.append((r, g, b))

print(my_list)
