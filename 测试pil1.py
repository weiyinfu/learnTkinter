from PIL import Image, ImageDraw, ImageFont
import pylab as plt


def test1():
    image = Image.new("RGBA", (600, 150), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    fontsize = 20
    txt = 'weiyinfu'
    font = ImageFont.truetype("/System/Library/Fonts/SFCompactText.ttf", fontsize)
    res = font.getmask(txt)
    print(res,dir(res),res.size)
    draw.text((10, 0), txt, (0, 0, 0), font=font)
    img_resized = image.resize((188, 45), Image.ANTIALIAS)
    plt.imshow(img_resized)
    plt.show()


def test2():
    with Drawing() as draw:
        with Image(width=1000, height=100, background=Color('lightblue')) as img:
            draw.font_family = 'Indie Flower'
            draw.font_size = 40.0
            draw.push()
            draw.fill_color = Color('hsl(0%, 0%, 0%)')
            draw.text(0, int(img.height / 2 + 20), 'Hello, world!')
            draw.pop()
            draw(img)
            img.save(filename='image.png')


test1()
