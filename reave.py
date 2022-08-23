import board
import neopixel
import time
import pixels


cara = neopixel.NeoPixel(board.A0, pixels.mask_len)

def strand_test():
    '''
    At startup, test the full strand
    '''
    for _ in range(pixels.mask_len):
        cara.fill(pixels.colors['reaver'])
        time.sleep(0.2)
        cara.fill((0, 0, 0))

def mirror(pattern):
    '''
    Mirrors a neopixel pattern for a cosplay mask
    '''
    pattern = [x for i in range(0,len(pattern),4) for x in reversed(pattern[i:i+4])]
    return pattern

def print4x4(pattern):
    '''
    Prints a 16 array in a 4x4 size.
    '''
    print(str(pattern[:4]) + '\n' + str(pattern[4:8]) + \
        '\n' + str(pattern[8:12]) + '\n' + str(pattern[12:]))

def animacion(nombre):
    '''
    Combines patterns into NeoPixel strip pattern
    '''
    print("anim")
