# ASCII Art

This is a simple tool to convert mp4 files or even live feed from your webcam to ascii art using libraries such as PIL and opencv.

Now each and every pixel's average value is calculated using a predetermined formulae. Then it is mapped to an ASCII character set and printed to the terminal after resizing the image.

## Demo


## Issues
* If the entire terminal is used to print the ascii art, then a lot of processing power is needed and also the character need to be printed faster than a new frame can be captured.

* There can be lot of flickering if the `cls` or `clear` command is used, thus to reduce it. We use ANSI escape sequence to clear the output buffer using `sys.stdout.write("\033[H")`.
<br>There is also a sleep of 4ms to make the animation smoother.