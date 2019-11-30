# pisign
Raspberry Pi / WS2812B based Sign

Using [the 8x32 display available here](https://www.amazon.com/gp/product/B01DC0IPVU/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1), but any WS2812B set of LEDs would work..

## Getting Started

    sudo apt-get update && sudo apt-get -y upgrade
    sudo pip3 install -r requirements.txt
    
## Sample Code

### test_board.py

Displays a rainbow pattern. Auto_write is defaulted to true, so it will fill the pattern light by light. 

### rainbow.py

Rainbow pattern, animated.

### display_image.py

Using PIL, resize a given image to 8x32 and display.

### web.py

Using Flask, create a basic web page that will allow a user to change LEDs individually. 

### matrix.py

Required for the above; maps the linear LED IDs to an X/Y matrix. 


 
