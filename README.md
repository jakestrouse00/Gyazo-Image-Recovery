# Gyazo-Image-Recovery
Recovers images on your Gyazo account if you haven't upgraded your account to premium.
## Prerequisites
```pip install requests```, 
```pip install urllib```
## Notices

This tool is not perfect. The images it gets are compressed, so the quality is not outstanding. Depending on the recovered image's size, text and numbers may be visible and readable.


### How to use

1. Download all files
2. Open *getSession.py* in a text editor of your choice
3. Enter your email, password, and country in the required fields
4. Save and close *getSession.py*
5. Run *getSession.py*
6. Copy your session
7. Open *imageFinder.py*
8. Paste your session in the session field on line 57 between the *' '*
9. In number form (ex, 5 or 10), enter the *Recovery_Amount* on line 58 between the *' '*. This is the number of images to be recovered from Gyazo
10. Save and close *imageFinder.py*
11. Run *imageFinder.py*


### Inteprditing the results

After running *imageFinder.py* you will see a new folder named *Recovered_Images*. Inside of this folder are more folders. Each of these folders is the catagory of the images recovered. When opening any of the catagory folders there will be more folders inside. These folders are named the after the image descriptions. On occasion, you may see a folder named *Long-file-name*. These folders are no diffrent from the other folders, other than the description of the image was a directory. To avoid future errors, I set any descriptions that were longer than 20 charecters to *Long-file-name*.

### Future updates and ideas

- [X] Add GIF compatability
- [ ] Implement *getSession.py* to make the program just one file
- [ ] Add version that stores images and gifs continuously 

#### Contact Information
- Discord: Influxes#0603
- Discord Server: [SERVER](https://discord.gg/J5aBerV "MY DISCORD SERVER")
- Telegram: @Influxes
