import reave

reave.strand_test()

print(reave.pixels.colors['reaver'])

print("ojo iz")
reave.print4x4(reave.pixels.ojo)
print("ojo der")
reave.print4x4(reave.mirror(reave.pixels.ojo))
