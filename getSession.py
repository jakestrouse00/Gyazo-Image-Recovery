import requests

# login settings
email = ''
password = ''
country = ''
# headers for post request
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'cookie': '__cfduid=de0379a6302e055c35500bc59cc1053681551119262; Gyazo_session=TDR5dkhPQjdsL0hyZ2wwdUtEblNUdlp1aEJ3TGZ0d2FTTTY1bEtFSWVwN2hMTm52ZTZFM3ZxaEFieEdtVEF0T2ZwdURJdnZ6Y3FwSHFtOXY4c3lzN2FxbUdJYzh0QUtGVXprVE1sbUNtY0lYN2F2TkdYQVc5ZCtmcEdMMEJTTGJ4cTRVeUVEYkVldE9UOWJacE5ud1N3MkFKdDhrYlhnRzNMdng3Ty9kaytaR0RVSXVrSDNDQ2ZpbURZcm5neW9tcU1hMFp4TkFtUHFTY1JwQ1BST0JObGwrdExFYlA1RFhwbGdpRW5qbHdOdkQzZ25lVWdQUnpUVVFHaUswcy9wblArTGRoa3loVGVnT0hVS2JmQ0VLUEpyMk14dERVWHZRT0xhNnhaNDNIWWh6SEhhS2dzb2Z3U2NRaldYODNVTnd4b1dxd1ZLd1cwT2xYUm1TSUtSWEJDR1RTVElQRnhhL21lL0RUeGtYNDcwPS0tQ1E3bDgzTWptc0c4ZTF0YktGTVpxdz09--22a81caa60a7db6c6aef771d2cc9d5a098f46d91',
    'x-csrf-token': 'ibzu7splMNOUj/loImIa2fOuN9/KiYxSyHDyZqTVdUKsC7k0IVkLeYVma98efURrSkuA+ZQBe2DM4CwThs6m4A=='
}
# json for post request
payload = {"email": email, "origin": 'null', "password": password, "country": country}
# the post request
r = requests.post('https://gyazo.com/api/internal/sessions', headers=head, json=payload)
# looking through the response cookies
for cookie in r.cookies:
    try:
        # spiting the cookie to get the session
        session = str(cookie).split("<Cookie Gyazo_session=")[1].split(" for .gyazo.com")[0]
    except:
        pass
print(f"Your Session Is: {session}")
input()
