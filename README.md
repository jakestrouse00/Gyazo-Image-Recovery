# Gyazo-Image-Recovery
Recovers images on your Gyazo account if you haven't upgraded your account to premium.
## Prerequisites
```pip install requests```, 
```pip install urllib```
## Notices

This tool is not perfect. The images it gets are compressed, so the quality is not outstanding. Depending on the recovered image's size, text and numbers may be visible and readable.


### How to use

1. Open *imageFinder.py* in a text editor of your choice
2. Fill in your account email, password, and country code in the required fields from lines 102 to 105
3. Save and close *imageFinder.py*
4. Run *imageFinder.py* with the command ```python imageFinder.py``` in cmd or terminal

Same steps apply for the [continuous version](Continuous-GIR)


### Inteprditing the results

After running *imageFinder.py* you will see a new folder named *Recovered_Images*. Inside of this folder are more folders. Each of these folders is the catagory of the images recovered. When opening any of the catagory folders there will be more folders inside. These folders are named the after the image descriptions. On occasion, you may see a folder named *Long-file-name*. These folders are no diffrent from the other folders, other than the description of the image was a directory. To avoid future errors, I set any descriptions that were longer than 20 charecters to *Long-file-name*.

### Future updates and ideas

- [X] Add GIF compatability
- [X] Implement *getSession.py* to make the program just one file
- [X] Add version that stores images and gifs continuously 

#### Contact Information
- Discord: Influxes#0603
- Discord Server: [SERVER](https://discord.gg/J5aBerV "MY DISCORD SERVER")
- Telegram: @Influxes
