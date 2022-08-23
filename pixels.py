mask_len = 104

'''
01 - ojo derecho - 0-12
02 - ojo izquierdo 13-31
03 - bigote sup iz 
04 - bigote inf iz
05 - lagrima
06 - nariz
07 - bigote sup der
08 - bigote inf der
09 - boca der
10 - boca iz
11 - oreja iz
12 - oreja der
'''

# bigotes
#pixels[33] = (1, 25, 15)
#pixels[34] = (1, 25, 15)
#pixels[35] = (1, 25, 15)

#pixels[44] = (1, 25, 15)
#pixels[45] = (1, 25, 15)
#pixels[46] = (1, 25, 15)

colors = { 'reaver': (10, 255, 150),
                 'angry': (255, 0, 0) 
               }

ojo = [ 1, 1, 0, 0,
           0, 1, 1, 0,
           0, 1, 1, 0,
           0, 0, 0, 1 ]


# lagrima
#while True:
#    time.sleep(1)
#    pixels[48] = (1, 25, 15)
#    time.sleep(1)
#    pixels[48] = (0, 0, 0)
