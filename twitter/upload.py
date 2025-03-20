import tweepy
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw  

import textwrap
import random
import time
import re

def main():

    twitter_auth_keys = {
        "consumer_key"        : "<consumer_key>",
        "consumer_secret"     : "<consumer_secret>",
        "access_token"        : "<access_token>",
        "access_token_secret" : "<access_token_secret>"
    }
 
    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)
 
    client = tweepy.Client(
        consumer_key        = "<consumer_key>",
        consumer_secret     = "<consumer_secret>",
        access_token        = "<access_token>",
        access_token_secret = "<access_token_secret>"
    )

    # Upload image

    number = str(random.randint(1, 7000))
    image = Image.open("images/" + number + ".jpg")
    fontsize = 42  # starting font size
    font = ImageFont.truetype("fonts/LemonMilkbold.otf", fontsize)
    lines = open('quotes2.txt').read().splitlines()
    text = random.choice(lines)

    regexp = re.compile('[^A-Za-z0-9 ,.]')
    if regexp.search(text) or len(text) < 50:
        post_result = client.create_tweet(text=text)
        raise SystemExit

    if text.endswith('.'):
        text = text[:-1]

    text_color = (255, 255, 255)
    text_start_height = 70
    draw_multiple_line_text(image, text, font, text_color, text_start_height)
    image.save('generated.jpg')

    media = api.media_upload("generated.jpg")

    # Post tweet with image
    tweet = ""
    post_result = client.create_tweet(text=text, media_ids=[media.media_id])
    #post_result = client.create_tweet(text=text)

def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    '''
    From unutbu on [python PIL draw multiline text on image](https://stackoverflow.com/a/7698300/395857)
    '''
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=35)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height


if __name__ == "__main__":
    main()
