words = """art
hue
ink
oil
pen
wax
clay
draw
film
form
kiln
line
tone
tube
wood
batik
brush
carve
chalk
color
craft
easel
erase
frame
gesso
glass
glaze
image
latex
liner
media
mixed
model
mural
paint
paper
photo
print
quill
quilt
ruler
scale
shade
stone
style
tools
video
wheel
artist
bridge
canvas
chisel
crayon
create
depict
design
enamel
eraser
fresco
hammer
marble
marker
medium
mobile
mosaic
museum
pastel
pencil
poster
pounce
roller
sculpt
sketch
vellum
visual
acrylic
artwork
cartoon
carving
casting
collage
compass
drawing
engrave
etching
exhibit
gallery
gilding
gouache
painter
palette
pigment
portray
pottery
primary
realism
solvent
stained
stencil
tempera
textile
tsquare
varnish
woodcut
abstract
airbrush
artistic
blending
ceramics
charcoal
contrast
critique
decorate
graffiti
graphite
hatching
maquette
marbling
painting
portrait
printing
quilting
sculptor
seascape
template
animation
cloisonne
decoupage
encaustic
engraving
landscape
porcelain
portfolio
sculpture
secondary
stippling
undertone
assemblage
brightness
creativity
decorative
exhibition
illustrate
lithograph
paintbrush
photograph
proportion
sketchbook
turpentine
watercolor
waterscape
calligraphy
composition
masterpiece
perspective
architecture
glassblowing
illustration
installation
stonecutting
crosshatching
"""

all_valid_words = ()
start = 0
end = 0

for char in words:
    # append substring to the end of the valid words tuple
    if char == '\n':
        all_valid_words = all_valid_words + (words[start:end], )
        start = end + 1
        end = end + 1
    # increment end pointer to keep looking for the end of the word
    else:
        end = end + 1

#print(all_valid_words)

tiles = "wodo"
found_words = ()

for word in all_valid_words:
    all_letters_in_word = True
    tiles_left = tiles
    #check every letter in an art word
    for letter in word:
        # letter not in leftover tiles, so stop looking at remaining letters in word
        if letter not in tiles_left:
            all_letters_in_word = False
            break
        # update leftover tiles 
        else:
            index = tiles_left.find(letter)
            tiles_left = tiles_left[0:index] + tiles_left[index+1:len(tiles_left)]

    # check why the inner for loop ended: break or found all letters?
    if all_letters_in_word:
        found_words = found_words + (word, )
        
for w in found_words:
    print(w)
