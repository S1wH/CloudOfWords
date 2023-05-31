from wordcloud import WordCloud
import numpy as np
import time


x, y = np.ogrid[:300, :300]
mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)

with open("file.txt") as file:
    data = file.read()

wc = WordCloud(background_color="white", repeat=True, mask=mask).generate(data)
image = wc.to_image()
image.save('reading_from_file.jpg')

while True:
    time.sleep(1000)
