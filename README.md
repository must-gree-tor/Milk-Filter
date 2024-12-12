# Milk-Filter
Choose any image you like and convert it to something you would find in the series Milk inside/outside a bag of milk! There is also another effect which you can try for different results.

![Milk Filter Logo.](https://github.com/LucaSinUnaS/Milk-Filter/blob/main/icon.ico)

## Showcase

![Milk Filter Showcase.](https://github.com/LucaSinUnaS/Milk-Filter/blob/main/Showcase.gif)

## How to open the program?
### On PC
There is an EXE file attached which should work perfectly fine on Windows. To download it, head to the releases section of this GitHub page (should be to the right of the website on PC).

If you are on an OS that doesn't support EXE files, you can download the source code (the file called filter.py), then install Python if you haven't already, and finally on the command line, insert:
```
python filter.py
```
### On Android
Keep in mind this program was not made for Android, and these steps are just to be baaaarely usable in it, and should be used this way only if you have no other choice. Expect it to be messy and overall bad. Nonetheless, it should still get the job done, I got it to work at least. So here are the steps:

1. Download Pydroid3 on Play Store
2. Download the file android.py from this repository
3. Open the file on Pydroid3
   ![Step 3](https://i.imgur.com/p9DqXof.jpeg)
4. Click the top left hamburguer and click on terminal
5. There, write:
   ```
   pip install pillow
   ```
6. Go back, and click on the play button in the bottom right corner
7. It should "work" now. You can open the image, apply the effect, and save the image.

Important note: 
- It WILL take quite some time (up to a minute or even more) for the filter to be applied, and the "app" will freeze when loading so don't worry if that happens. Just remember this was made for PC and not for mobile.
- The "app" is best viewed in portrait mode.
- Use this slider to move horizontally when opening an image:
  ![slider](https://i.imgur.com/V9JhjjV.jpeg)

## How do I use it?

1. Click on "Open a File"
2. Choose the image you want to convert. It supports png, jpg and jpeg files.
3. Choose if you want to compress the image or not. Compression gives a more pixelated look that can sometimes imitate the look of the games. Nonetheless, I recommend against using it in most cases.
4. Choose if you want to give the "pointillism" effect. Don't know how will it look? Give it a try!
5. Choose between applying the effect from the first or the second game.
7. Click on "Apply filter". Don't worry if the program freezes for a moment, it's normal since it is converting the image, just wait a few seconds.
8. A new window will open showcasing the new image, and a button that will open the new image in your default image viewer. Don't worry if after closing the image viewer the program freezes for a bit, it's normal, just wait.
9. In the main window, you can choose to save the image by clicking on the "Save image" button.
10. You can repeat this process until you are satisfied.

## Notes

- Don't worry if the program freezes during the conversion, after it finishes it will come back to normal.
- Don't worry if the image looks stretched in the program, when saved it will look normal (you can check viewing it in your default image viewer). It is a current problem where it doesn't take into account the dimension when inserting it into the program, but that problem doesn't happen when saving it.
- The program will take longer as the image size is bigger.
- When choosing to compress the image, a temp file will be created right where the program is located. If you want you can delete it after the conversion has finished, but don't worry about its size, it will be very small.
- Please contact me in lucamuino@gmail.com if you find any bugs, issues, or you want a new feature!
- Expect the program to be kind of simple. I put up a GUI quickly to remove the need to do it in console.
- You are free to do whatever you want with this code. If you want to help adding features, making it prettier, or just refactoring the code, I'll be happy to review them.

## Final comments

I hope you enjoy this simple program! I would be very happy to see what things you'll make with this :). 

If you want to support me for some reason, you can donate through here: https://ko-fi.com/lucasins
