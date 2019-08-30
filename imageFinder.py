import requests
import os
import urllib.request
import random
import time
from datetime import datetime


def getImages(session):
    # getting the current date and time and converting it to epoch
    date_time = str(datetime.now()).split(".")[0]
    pattern = '%Y-%m-%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(str(date_time), pattern)))
    # setting up the headers
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'cookie': session
    }
    # sending the post
    r = requests.get(f'https://gyazo.com/api/internal/images?page=1&per={Recovery_Amount}&timestamp={epoch}',
                     headers=head)
    # testing to see if the session is valid
    if r.reason == 'Forbidden':
        print("Session is invalid!")
        return None
    else:
        images = []
        for element in r.json():
            # going through the returned images and gifs and making a list to use in the future
            imageURL = str(element['thumb_url']).split('116')
            imageURL.insert(1, '190')
            imageURL = "".join(imageURL)
            # checking if the image is a gif
            if ".gif" in imageURL:
                imageType = 'gif'
            else:
                imageType = 'jpg'
            imageTitle = element['metadata']['title']
            imageApp = element['metadata']['app']
            s = [imageApp, imageTitle, imageURL, imageType]
            images.append(s)
        return images


def sortImages(imageList):
    # extracting all the need variables from the list
    imageApp = imageList[0]
    imageTitle = imageList[1]
    imageURL = imageList[2]
    imageType = imageList[3]
    # making sure the image description isn't too long
    if len(imageTitle) > 20:
        imageTitle = "Long-file-name"
    # in case there is a file as a description under 20 characters, replace backslashes with colons 
    for char in imageTitle:
        m = '\\'
        if char == m:
            imageTitle[char] = ":"
    # checking if paths exist for the files being created. If not, create them
    if not os.path.exists("Recovered_Images"):
        os.makedirs("Recovered_Images")
    if not os.path.exists("Recovered_Images/" + imageApp):
        os.makedirs("Recovered_Images/" + imageApp)

    if not os.path.exists(f'Recovered_Images/{imageApp}/{imageTitle}'):
        os.makedirs(f'Recovered_Images/{imageApp}/{imageTitle}')
    while True:
        # if the image is a gif, setting the file to have the correct ending
        if imageType == 'gif':
            m = f"Recovered_Images/{imageApp}/{imageTitle}/{imageApp}-{imageTitle}-{random.randint(0,10000)}.gif"
        else:
            m = f"Recovered_Images/{imageApp}/{imageTitle}/{imageApp}-{imageTitle}-{random.randint(0,10000)}.jpg"
        # checking that the filename hasn't been used before
        if not os.path.exists(m):
            urllib.request.urlretrieve(imageURL, m)
            break
    print(f"Created file for {imageApp}")


# File Settings
Gyazo_Session = ''
Recovery_Amount = ''
# Don't change anything below this comment or in the above functions
session = f"Gyazo_session={Gyazo_Session}"
images = getImages(session)
if images is not None:
    for image in images:
        sortImages(image)

print("\nImage recovery complete!")
print("Press ENTER to close this window")
input()
