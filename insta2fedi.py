import sys
import requests
import os.path
from mastodon import Mastodon

url = 'https://www.instagram.com/' + sys.argv[1] + '/'
r = requests.get(url)
page_source = r.text
index_image = page_source.find('GraphImage')
index1 = (page_source.find('"shortcode":"', index_image) + 13)
index2 = page_source.find('"', index1)
id = page_source[index1:index2]

if os.path.isfile(id + '.jpg'):
    print ("This image has already been downloaded.")
else:
    url_image = 'https://www.instagram.com/p/' + id
    r2 = requests.get(url_image)
    page_source2 = r2.text
    index3 = page_source2.find('og:image')
    index4 = page_source2.find('https', index3)
    index5 = page_source2.find('" />', index4)
    image_link = page_source2[index4:index5]
    print(image_link)

    page = requests.get(image_link)
    f_name = id + '.jpg'

    with open(f_name, 'wb') as f:
        f.write(page.content)
        f.close()
    print(' A new image has been downloaded.')
    #   Set up Mastodon
    mastodon = Mastodon(
        access_token = 'XXXXXXXXXXXXXXXXXXXX',
        api_base_url = 'https://mstdn.jp/'
    )
    media = mastodon.media_post(f_name)
    mastodon.status_post("test", media_ids=media)

    print(' Image posted to the fediverse.')