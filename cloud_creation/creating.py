import numpy as np
from wordcloud import WordCloud
import time

text = "I love docker"

x, y = np.ogrid[:300, :300]
mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)

wc = WordCloud(background_color="white", repeat=True, mask=mask).generate(text)
image = wc.to_image()
image.save('image.jpg')
while True:
    time.sleep(1000)
