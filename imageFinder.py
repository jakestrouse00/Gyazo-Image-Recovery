import requests
import os
import urllib.request
import random


def getImages(session):
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'cookie': session
    }
    r = requests.get(f'https://gyazo.com/api/internal/images?page=1&per={Recovery_Amount}&timestamp=1567117867.5293128',
                     headers=head)
    if r.reason == 'Forbidden':
        print("Session is invalid!")
        return None
    else:
        images = []
        for element in r.json():
            imageURL = str(element['thumb_url']).split('116')
            imageURL.insert(1, '190')
            imageURL = "".join(imageURL)
            imageTitle = element['metadata']['title']
            imageApp = element['metadata']['app']
            s = [imageApp, imageTitle, imageURL]
            images.append(s)
        return images


def sortImages(imageList):
    imageApp = imageList[0]
    imageTitle = imageList[1]
    imageURL = imageList[2]
    if len(imageTitle) > 20:
        imageTitle = "Long-file-name"
    for char in imageTitle:
        m = '\\'
        if char == m:
            imageTitle[char] = ":"
    if not os.path.exists("Recovered_Images"):
        os.makedirs("Recovered_Images")
    if not os.path.exists("Recovered_Images/"+imageApp):
        os.makedirs("Recovered_Images/"+imageApp)

    if not os.path.exists(f'Recovered_Images/{imageApp}/{imageTitle}'):
        os.makedirs(f'Recovered_Images/{imageApp}/{imageTitle}')
    while True:
        m = f"Recovered_Images/{imageApp}/{imageTitle}/{imageApp}-{imageTitle}-{random.randint(0,10000)}.jpg"
        if not os.path.exists(m):
            urllib.request.urlretrieve(imageURL, m)
            break
    print(f"Created file for {imageApp}")


# File Settings
Gyazo_Session = ''
Recovery_Amount = '5'
# Don't change anything below this comment or in the above functions
session = f"Gyazo_session={Gyazo_Session}"
images = getImages(session)
if images != None:
    for image in images:
        sortImages(image)

print("\nImage recovery complete!")
print("Press ENTER to close this window")
input()
