from PIL import Image, ImageDraw

secret = "https://postimg.cc/RWbXnRfy"
binary_rows = [format(ord(c), '08b') for c in secret]
print(binary_rows)

dot_radius = 15
dot_spacing = 50
row_spacing = 50
padding = 40


color_1 = (0, 191, 255)
color_0 = (128, 128, 128)
bg_color = (10, 10, 10)


scale = 4


img_width = (8 * dot_spacing + 2 * padding) * scale
img_height = (len(binary_rows) * row_spacing + 2 * padding) * scale


dot_radius *= scale
dot_spacing *= scale
row_spacing *= scale
padding *= scale


img_large = Image.new("RGB", (img_width, img_height), bg_color)
draw = ImageDraw.Draw(img_large)


for row_idx, byte in enumerate(binary_rows):
    for bit_idx, bit in enumerate(byte):
        cx = padding + bit_idx * dot_spacing
        cy = padding + row_idx * row_spacing
        color = color_1 if bit == '1' else color_0
        draw.ellipse(
            [cx - dot_radius, cy - dot_radius, cx + dot_radius, cy + dot_radius],
            fill=color
        )


img_final = img_large.resize(
    (img_width // scale, img_height // scale),
    resample=Image.LANCZOS
)


img_final.save("dots.png")
