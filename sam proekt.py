from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

def po():
    sound1.play()



def df():
    sound16.stop()
    sound3.play()
    liftdveri1.animate_position((97.5, 7.6, 96), duration=3)
    liftdveri2.animate_position((97.5, 7.25, 104), duration=3)
    liftbutton.position = 1000000, 500, 100

def tp():
    sound1.play()
    dveriroom2.animate_position((68.5, 13, 115), duration=3)
    keytrue2room2.position = 1000000, 500, 100

def rotate():
    player.animate_rotation((0, 360 , 0), duration=1)


def pip():
    sound5.play()
    dveriroom3.animate_position((68.5, 13, 135), duration=1)
    player.animate_rotation((0, 180 , 0), duration=1)
    seek.position = 68.5, 8, 115
    seek.visible = True
    seek.animate_position((68.5, 8, 294), duration=20)
    sound7.play()
    dveriroom4.animate_position((68.5, 13, 235), duration=8)
    invoke(rotate, delay=2)

def lk7():
    dverifalse2room7.position = 93.5, 13, 300
    deah27room7.animate_position((68.5, 7.3, 300),duration=1.5)
    sound9.play()


def lk8():
    dveritrueroom7.animate_position((43.5, 13, 300), duration=3)
    sound1.play()

def lk9():
    dverifalse1room7.position = 68.5, 13, 325
    deah19room7.animate_position((68.5, 7.3, 300),duration=1.5)
    sound9.play()



def t():
    sound5.play()
    keytrue2room2.animate_position((71, 6, 103), duration=1)
    keytrue1room2.position = 1000000, 500, 100


    
def lkb():
    obmandveriroom4.animate_position((68.5, 7.3, 235), duration=1)


def pwp():
    sound7.stop()
    sound8.play()
    button.position = 1000000, 500, 100
    seek.animate_position((68.5, 6, 234), duration=1)
    obmandveriroom4.animate_position((68.5, 7.3, 235), duration=1)

def hide():
    deah.visible = False

def wtt():
    keytrueroom8.position = 1000000, 500, 100
    sound1.play()
    dvr8.animate_position((23.5,13, 300), duration=3)
    


def wrt():
    keyfalseroom8.position = 1000000, 500, 100
    keytrueroom8.position = 33.5, 7, 304.7
    sound5.play()


def jhu():
    deah.visible = True
    deah.animate_scale((1), duration=0.5)
    sound6.play()
    sound1.stop()
    sound16.stop()
    sound2.stop()
    sound3.stop()
    sound4.stop()
    sound5.stop()
    sound7.stop()
    sound8.stop()
    sound9.stop()
    sound10.stop()
    sound11.stop()
    sound12.stop()
    sound13.stop()
    sound14.stop()
    sound15.stop()
    player.position = 300, 299, 300
    hand.visible = False
    invoke(hide, delay=2)

def lkr():
    dveriroom5.animate_position((68.5, 13, 255), duration=3)
    sound1.play()
    
def lwr():
    dvr8.animate_position((23.5, 13, 300),duration=3)
    sound1.play()


def kh():
    sound5.play()
    dveriroom1.animate_position((78, 13, 100), duration=3)
    keytrueroom1.position = 1000000, 500, 100
    liftdveri1.animate_position((97.5, 7.6, 98.5), duration=3)
    liftdveri2.animate_position((97.5, 7.25, 101), duration=3)
    invoke(ky)

def ky():
    if hand.visible == True:
        invoke(kl)

def kl():
    if player.intersects(dveriroom1).hit:
        sound1.play()
        dveriroom1.animate_position((78, 13, 100), duration=3)


def llp():
    player.position = 53.5, 6, 297

def rushend():
    rush.scale = 1, 2, 10
    rush.animate_position((-205, 6, 300), duration=4)
    sound10.play()
    
def tenban():
    dvr9.animate_position((-26 ,30, 300), duration=3)
    sound1.play()

def llo():
    player.position = 1000, 1001, 1000
    
def oooo():
    yw.visible = True  
    sound15.play()  

def ooo():
    per14r10.animate_position((-66, 9.3, 320), duration=3)
    sound1.play()
    invoke(oooo, delay=3)

def lkp():
    sound1.play()
    dveriroom6.animate_position((68.5, 13, 275), duration=1)
    rush.position = 68.5, 6, 255
    rush.visible = True
    rush.animate_position((68.5, 6, 300),duration=9)
    sound11.play()
    invoke(rushend, delay=9)
    
def wefend():
    hand.animate_rotation((10, 5, 5), duration=1)    

def figst():
    figyra.animate_position((-50, 9.3, 300), duration=3)
    invoke(fg1, delay=4)

def fg1():
    figyra.animate_position((-50, 9.3, 280), duration=5)
    invoke(fg2, delay=6)

def fg2():
    figyra.animate_position((-30, 9.3, 280), duration=3)
    invoke(fg3, delay=4)

def fg3():
    figyra.animate_position((-30, 9.3, 320), duration=6)
    invoke(fg4, delay=6)

def wqp():
    pred2.position = 1000000, 500, 100
    sound5.play()
    butoonlift2.position = -66, 5.5, 322

def fg4():
    figyra.animate_position((-50, 9.3, 320), duration=3)
    invoke(fg1, delay=4)



def wqr():
    sound5.play()
    pred.position = 1000000, 500, 100
    per13r10.position = -71, 18, 290

#def zvyk():
    #sound12.play()
    #invoke(zvyk, delay=8)
    

def wef():
    richag.animate_rotation((0, 0, 120),duration=2) 
    hand.animate_rotation((-60, 30, 5), duration=1) 
    per11r10.animate_position((-56, 17.3, 300), duration=3) 
    per8r10.animate_position((-46, 17.3, 300), duration=7)
    per7r10.animate_position((-36, 17.3, 300), duration=7)
    dvr99.animate_position((-26 ,7.3, 300), duration=1)
    figyra.animate_position((-59.5, 9.3, 300), duration=5)
    player.animate_position((-50.5, 6.3, 300),duration=2)
    sound13.play()
    #invoke(zvyk)
    sound12.play()
    invoke(wefend, delay=1) 
    invoke(figst, delay=6)


def kw():
    sound2.stop()
    sound16.play()
    player.position = liftpol.position
"""lobby"""

sound16 = Audio('Elevator.mp3', autoplay=False)
sound1 = Audio('dooropen.mp3', autoplay=False)
sound2 = Audio('loby.mp3', autoplay=True)
sound3 = Audio("liftend.mp3", autoplay=False)
sound4 = Audio("redkey.mp3", autoplay=False)
sound5 = Audio("pip.mp3", autoplay=False)
sound6 = Audio("bm.mp3", autoplay=False)
sound7 = Audio("seek.mp3", autoplay=False)
sound8 = Audio("seekend.mp3", autoplay=False)
sound9 = Audio("sc.mp3", autoplay=False)
sound10 = Audio("rush.mp3", autoplay=False)
sound11 = Audio("rushstart.mp3", autoplay=False)
sound12 = Audio("figv.mp3", autoplay=False)
sound13 = Audio("fgdr.mp3", autoplay=False)
sound14 = Audio("fgd.mp3", autoplay=False)
sound15 = Audio("YOU WIN.mp3", autoplay=False)



cube = Entity(model='cube', color=color.white, scale=(17, 1, 9), collider='box', texture = "ort.jpg")
cube1 = Entity(model='cube', color=color.white, position=(-1.25, 2, 2), scale=(12, 3, 1), collider='box',texture = "ort.jpg")
lift = Entity(model='cube', color=color.white, position=(6.25, 2, 2), scale=(3, 3, 1), collider='box', texture = "lift.jpg", on_click=kw)
cube2 = Entity(model='cube', color=color.white,position=(-7.5, 2, -2.5), scale=(1, 3, 10), collider='box', texture = "ort.jpg")
cube3 = Entity(model='cube', color=color.white,position=(0, 2, -5), scale=(16, 3, 1), collider='box', texture = "ort.jpg")
cube4 = Entity(model='cube', color=color.white,position=(8.3, 2, -2.5), scale=(1, 3, 9), collider='box', texture = "ort.jpg")
cube5 = Entity(model='cube', color=color.white,position=(0, 4, 0), scale=(17, 1, 9), collider='box', texture = "ort.jpg")
"""loby end"""
"""lift"""
liftpol = Entity(model='cube', color=color.white, position=(100, 5, 100), scale=(5, 1, 5),collider='box', texture = "ort.jpg")
liftbutton = Entity(model='cube', color=color.white, position=(98.5, 6, 102), scale=(1),collider='box', on_click=df, texture = "liftstop.jpg")
liftstina = Entity(model='cube', color=color.black, position=(103, 6, 100), scale=(1, 10, 5),collider='box', texture = "images.jpg")
liftstina1 = Entity(model='cube', color=color.black, position=(100, 6, 97), scale=(5, 10, 1),collider='box', texture = "images.jpg")
liftstina2 = Entity(model='cube', color=color.black, position=(100, 6, 103), scale=(5, 10, 1),collider='box', texture = "images.jpg")
liftpotolok = Entity(model='cube', color=color.black, position=(100, 10.5, 100), scale=(5, 1, 5),collider='box')
liftdveri1 = Entity(model='cube', color=color.white, position=(97.5, 7.6, 98.5), scale=(0.5, 8, 2.5),collider='box', texture = "0.jpg")
liftdveri2 = Entity(model='cube', color=color.white, position=(97.5, 7.25, 101), scale=(0.5, 8, 3),collider='box', texture = "01.jpg")

"""lift end"""

"""room 1"""
polroom1 = Entity(model='cube', color=color.white, position=(87.5, 5, 100), scale=(20, 1, 10),collider='box', texture = "pol.jpg")
stana1room1 = Entity(model='cube', color=color.white, position=(87.5, 7, 105), scale=(20, 5, 1),collider='box', texture = "stina.jpg")
stana2room1 = Entity(model='cube', color=color.white, position=(87.5, 7, 95), scale=(20, 5, 1),collider='box', texture = "stina.jpg")
stana3room1 = Entity(model='cube', color=color.white, position=(78, 7, 97), scale=(1, 5, 3),collider='box', texture = "stina.jpg")
stana4room1 = Entity(model='cube', color=color.white, position=(78, 7, 103), scale=(1, 5, 3),collider='box', texture = "stina.jpg")
potolokroom1 = Entity(model='cube', color=color.white, position=(87.5, 10, 100), scale=(20, 1, 10),collider='box', texture = "potolok.jpg")
dveriroom1 = Entity(model='cube', color=color.white, position=(78, 7.3, 100), scale=(1, 5, 3),collider='box', texture = "002.jpg")
pereshkodaroom1 = Entity(model='cube', color=color.brown, position=(90, 7, 97.5), scale=(2, 5, 5),collider='box')
keytrueroom1 = Entity(model='tinker.obj', color=color.blue, position=(88.5, 6, 96), scale=(0.01),rotation=(0, 30, 0),collider='box', on_click = kh)
keyfalseroom1 = Entity(model='tinker.obj', color=color.red, position=(92.5, 6, 96), scale=(0.01),rotation=(0, 30, 0),collider='box', on_click = jhu)

"""room2"""
pol1room2 = Entity(model='cube', color=color.white, position=(75, 5, 100), scale=(5, 1, 10),collider='box', texture = "pol.jpg")
pol2room2 = Entity(model='cube', color=color.white, position=(67.5, 5, 105), scale=(10, 1, 20),collider='box', texture = "pol.jpg")
stana1room2 = Entity(model='cube', color=color.white, position=(70.5, 7, 95), scale=(14, 5, 1),collider='box', texture = "stina.jpg")
stana2room2 = Entity(model='cube', color=color.white, position=(64, 7, 105), scale=(1, 5, 20),collider='box', texture = "stina.jpg")
stana3room2 = Entity(model='cube', color=color.white, position=(75, 7, 104.5), scale=(5, 5, 1),collider='box', texture = "stina.jpg")
stana4room2 = Entity(model='cube', color=color.white, position=(73, 7, 110), scale=(1, 5, 10),collider='box', texture = "stina.jpg")
stana5room2 = Entity(model='cube', color=color.white, position=(65, 7, 115), scale=(2, 5, 1),collider='box', texture = "stina.jpg")
stana6room2 = Entity(model='cube', color=color.white, position=(72, 7, 115), scale=(2, 5, 1),collider='box', texture = "stina.jpg")
dveriroom2 = Entity(model='cube', color=color.white, position=(68.5, 7.3, 115), scale=(5, 5, 1),collider='box', texture = "03.jpg")
keytrue1room2 = Entity(model='tinker.obj', color=color.blue, position=(71, 6, 107), scale=(0.01),collider='box', texture = "bluekey.jpg", on_click = t)
potolok1room2 = Entity(model='cube', color=color.white, position=(75, 10, 100), scale=(5, 1, 10),collider='box', texture = "potolok.jpg")
potolok2room2 = Entity(model='cube', color=color.white, position=(67.5, 10, 105), scale=(10, 1, 20),collider='box', texture = "potolok.jpg")
keytrue2room2 = Entity(model='tinker.obj', color=color.blue, position=(71, 6, 90), scale=(0.01),collider='box', texture = "bluekey.jpg", on_click = tp)
seek = Entity(model='Seek.obj', color=color.black, position=(1000000, 500, 100), scale=(0.2, 0.5, 0.2), collider='box', visible=False)

"""room 3"""
polroom3 = Entity(model='cube', color=color.white, position=(68.5, 5, 125), scale=(5, 1, 20),collider='box', texture = "pol.jpg")
dveriroom3 = Entity(model='cube', color=color.white, position=(68.5, 7.3, 135), scale=(5, 5, 1),collider='box', texture = "004.jpg", on_click = pip)
potolokroom3 = Entity(model='cube', color=color.white, position=(68.5, 10, 125), scale=(5, 1, 20),collider='box', texture = "potolok.jpg")
stana1room3 = Entity(model='cube', color=color.white, position=(66, 7.5, 125), scale=(1, 5, 20),collider='box', texture = "stina.jpg")
stana2room3 = Entity(model='cube', color=color.white, position=(71, 7.5, 125), scale=(1, 5, 20),collider='box', texture = "stina.jpg")

"""seek room4"""
polroom4 = Entity(model='cube', color=color.white, position=(68.5, 5, 185), scale=(5, 1, 100),collider='box', texture = "pol.jpg")
st1room4 = Entity(model='cube', color=color.white, position=(66, 7.5, 185), scale=(1, 5, 100),collider='box', texture = "stina.jpg")
st2room4 = Entity(model='cube', color=color.white, position=(71, 7.5, 185), scale=(1, 5, 100),collider='box', texture = "stina.jpg")
potroom4 = Entity(model='cube', color=color.white, position=(68.5, 10, 185), scale=(5, 1, 100),collider='box', texture = "potolok.jpg")
dveriroom4 = Entity(model='cube', color=color.white, position=(68.5, 7.3, 235), scale=(5, 5, 1),collider='box', texture = "005.jpg")
obmandveriroom4 = Entity(model='cube', color=color.gray, position=(68.5, 13, 235), scale=(5, 5, 1),collider='box')

"""room5"""
polroom5 = Entity(model='cube', color=color.white, position=(68.5, 5, 245), scale=(5, 1, 20),collider='box', texture = "pol.jpg")
st1room5 = Entity(model='cube', color=color.white, position=(66, 7, 245), scale=(1, 5, 20),collider='box', texture = "stina.jpg")
st2room5 = Entity(model='cube', color=color.white, position=(71, 7, 245), scale=(1, 5, 20),collider='box', texture = "stina.jpg")
button = Entity(model='cube', color=color.white, position=(68, 6, 238), scale=(1),collider='box', on_click = pwp, texture = "cldr.jpg")
potroom5 = Entity(model='cube', color=color.white, position=(68.5, 10, 245), scale=(5, 1, 20),collider='box', texture = "potolok.jpg")
dveriroom5 = Entity(model='cube', color=color.white, position=(68.5, 7.3, 255), scale=(5, 5, 1),collider='box', texture = "006.jpg" , on_click = lkr)

"""room 6"""
polroom6 = Entity(model='cube', color=color.white, position=(68.5, 5, 265), scale=(5, 1, 20),collider='box', texture = "ima.png")
st1room6 = Entity(model='cube', color=color.white, position=(64.75, 7, 265), scale=(2.5, 5, 20),collider='box', texture = "stina.jpg")
st2room6 = Entity(model='cube', color=color.white, position=(72.25, 7, 265), scale=(2.5, 5, 20),collider='box', texture = "stina.jpg")
potroom6 = Entity(model='cube', color=color.white, position=(68.5, 10, 265), scale=(5, 1, 20),collider='box', texture = "potolok.jpg")
dveriroom6 = Entity(model='cube', color=color.white, position=(68.5, 7.3, 275), scale=(5, 5, 1),collider='box', texture = "007.jpg" , on_click = lkp)


"""room 7"""
pol1room7 = Entity(model='cube', color=color.white, position=(68.5, 5, 300), scale=(10, 1, 50),collider='box', texture = "ima.png")
pol2room7 = Entity(model='cube', color=color.white, position=(68.5, 5, 300), scale=(50, 1, 10),collider='box', texture = "ima.png")
pot1room7 = Entity(model='cube', color=color.white, position=(68.5, 10, 300), scale=(10, 1, 50),collider='box', texture = "potolok.jpg")
pot2room7 = Entity(model='cube', color=color.white, position=(68.5, 10, 300), scale=(50, 1, 10),collider='box', texture = "potolok.jpg")
st1room7 = Entity(model='cube', color=color.white, position=(73.5, 7, 285), scale=(1, 5, 20),collider='box', texture = "stina.jpg")
st2room7 = Entity(model='cube', color=color.white, position=(63.5, 7, 285), scale=(1, 5, 20),collider='box', texture = "stina.jpg")
st3room7 = Entity(model='cube', color=color.white, position=(63.5, 7, 315), scale=(1, 5, 20),collider='box', texture = "stina.jpg")
st4room7 = Entity(model='cube', color=color.white, position=(73.5, 7, 315), scale=(1, 5, 20),collider='box', texture = "stina.jpg")
st5room7 = Entity(model='cube', color=color.white, position=(53.5, 7, 305), scale=(20, 5, 1),collider='box', texture = "stina.jpg")
st6room7 = Entity(model='cube', color=color.white, position=(53.5, 7, 295), scale=(20, 5, 1),collider='box', texture = "stina.jpg")
st7room7 = Entity(model='cube', color=color.white, position=(83.5, 7, 295), scale=(20, 5, 1),collider='box', texture = "stina.jpg")
st8room7 = Entity(model='cube', color=color.white, position=(83.5, 7, 305), scale=(20, 5, 1),collider='box', texture = "stina.jpg")
dverifalse1room7 = Entity(model='cube', color=color.white, position=(68.5, 7.3, 325), scale=(10, 5, 1),collider='box', texture = "00922.jpg" , on_click = lk9)
dverifalse2room7 = Entity(model='cube', color=color.white, position=(93.5, 7.3, 300), scale=(1, 5, 10),collider='box', texture = "00722.jpg" , on_click = lk7)
dveritrueroom7 = Entity(model='cube', color=color.white, position=(43.5, 7.3, 300), scale=(1, 5, 10),collider='box', texture = "008.jpg" , on_click = lk8)
deah19room7 = Entity(model='cube', color=color.pink, position=(68.5, 7.3, 326), scale=(10, 5, 1),collider='box')
deah27room7 = Entity(model='cube', color=color.pink, position=(94.5, 7.3, 300), scale=(1, 5, 10),collider='box')
rush = Entity(model='cube', color=color.black, position=(1000000, 500, 100), scale=(10, 2, 5), collider='box', visible=False, texture = "кгір.jpg",)
skaf = Entity(model='cube', color=color.white, position=(53.5, 6, 296), scale=(1), collider='box', texture = "sfrm.png", on_click = llo)
"""room 8"""
polr8 = Entity(model='cube', color=color.white, position=(33.5, 5, 300), scale=(20, 1, 10),collider='box', texture = "pol.jpg")
st1r8 = Entity(model='cube', color=color.white, position=(33.5, 7, 305), scale=(20, 5, 1),collider='box', texture = "stina.jpg")
st2r8 = Entity(model='cube', color=color.white, position=(33.5, 7, 295), scale=(20, 5, 1),collider='box', texture = "stina.jpg")
potr8 = Entity(model='cube', color=color.white, position=(33.5, 10, 300), scale=(20, 1, 10),collider='box', texture = "potolok.jpg")
dvr8 = Entity(model='cube', color=color.white, position=(23.5,7.3, 300), scale=(1, 5, 10),collider='box', texture = "00922.jpg")
keyfalseroom8 = Entity(model='tinker.obj', color=color.red, position=(33.5, 7, 304.7), rotation=(90, 0, 0), scale=(0.01),collider='box', on_click = wrt)
keytrueroom8 = Entity(model='tinker.obj', color=color.blue, position=(1000000, 500, 100), rotation=(90, 0, 0), scale=(0.01),collider='box', on_click = wtt)

"""room9"""
polr9 = Entity(model='cube', color=color.white, position=(-1.5, 5, 300), scale=(50, 1, 10),collider='box', texture = "ort.jpg")
st1r9 = Entity(model='cube', color=color.white, position=(-1.5, 5, 305), scale=(49, 5, 1),collider='box', texture = "ort.jpg")
st2r9 = Entity(model='cube', color=color.white, position=(-1.5, 5, 295), scale=(49, 5, 1),collider='box', texture = "ort.jpg")
dvr9 = Entity(model='cube', color=color.white, position=(-26 ,7.3, 300), scale=(1, 5, 10),collider='box', texture = "010.jpg" , on_click = tenban)
potr9 = Entity(model='cube', color=color.white, position=(-1.5, 10, 300), scale=(49, 1, 10),collider='box', texture = "ort.jpg")
dvr99 = Entity(model='cube', color=color.white, position=(-26 ,12, 300), scale=(1, 5, 10),collider='box', texture = "tem.jpg" )
dvr999 = Entity(model='cube', color=color.white, position=(-26 ,12, 300), scale=(1, 5, 10),collider='box', texture = "tem.jpg" )


"""final room 10"""
polr10 = Entity(model='cube', color=color.white, position=(-51.5, 5, 300), scale=(50, 1, 50),collider='box', texture = "temp.jpg")
st2r10 = Entity(model='cube', color=color.white, position=(-26, 9.3, 285), scale=(1, 9, 20),collider='box', texture = "tem.jpg")
str110 = Entity(model='cube', color=color.white, position=(-26, 9.3, 315), scale=(1, 9, 20),collider='box', texture = "tem.jpg")
st3r10 = Entity(model='cube', color=color.white, position=(-51.5, 9.3, 275), scale=(50, 9, 1),collider='box', texture = "tem.jpg")
st4r10 = Entity(model='cube', color=color.white, position=(-51.5, 9.3, 325), scale=(50, 9, 1),collider='box', texture = "tem.jpg")
st5r10 = Entity(model='cube', color=color.white, position=(-76.5, 9.3, 300), scale=(1, 9, 50),collider='box', texture = "tem.jpg")
potr10 = Entity(model='cube', color=color.white, position=(-51.5, 14, 300), scale=(50, 1, 50),collider='box', texture = "temp.jpg")
per2r10 = Entity(model='cube', color=color.white, position=(-36, 9.3, 290), scale=(1, 9, 10),collider='box', texture = "tem.jpg")
per1r10 = Entity(model='cube', color=color.white, position=(-41, 9.3, 285), scale=(10, 9, 1),collider='box', texture = "tem.jpg")
per3r10 = Entity(model='cube', color=color.white, position=(-46, 9.3, 290), scale=(1, 9, 10),collider='box', texture = "tem.jpg")
per5r10 = Entity(model='cube', color=color.white, position=(-36, 9.3, 310), scale=(1, 9, 10),collider='box', texture = "tem.jpg")
per4r10 = Entity(model='cube', color=color.white, position=(-41, 9.3, 315), scale=(10, 9, 1),collider='box', texture = "tem.jpg")
per6r10 = Entity(model='cube', color=color.white, position=(-46, 9.3, 310), scale=(1, 9, 10),collider='box', texture = "tem.jpg")
per7r10 = Entity(model='cube', color=color.white, position=(-36, 9.3, 300), scale=(1, 9, 10),collider='box', texture = "tem.jpg")
per8r10 = Entity(model='cube', color=color.white, position=(-46, 9.3, 300), scale=(1, 9, 10),collider='box', texture = "tem.jpg")
per9r10 = Entity(model='cube', color=color.white, position=(-56, 9.3, 286), scale=(1, 9, 22),collider='box', texture = "tem.jpg")
per10r10 = Entity(model='cube', color=color.white, position=(-56, 9.3, 314), scale=(1, 9, 22),collider='box', texture = "tem.jpg")
per11r10 = Entity(model='cube', color=color.white, position=(-56, 9.3, 300), scale=(1, 9, 6),collider='box', texture = "tem.jpg")
richag = Entity(model='cube', color=color.gray, position=(-55.5, 7.3, 304), scale=(0.3, 0.9, 0.3),rotation=(0, 0, 60),collider='box', on_click = wef)
figyra = Entity(model='cube', color=color.white, position=(-59.5, 9.3, 306), scale=(3, 9, 3),collider='box', texture='fig.jpg')
pred = Entity(model='cube', color=color.blue, position=(-43.5, 6, 303), scale=(0.3, 0.3, 0.5),collider='box', texture='fig.jpg', on_click = wqr)
per12r10 = Entity(model='cube', color=color.white, position=(-61, 9.3, 290), scale=(10, 9, 1),collider='box', texture = "tem.jpg")
per13r10 = Entity(model='cube', color=color.white, position=(-71, 9.3, 290), scale=(10, 9, 1),collider='box', texture = "tem.jpg")
per14r10 = Entity(model='cube', color=color.gray, position=(-66, 18, 320), scale=(20, 9, 1),collider='box', texture = "tem.jpg")
pred2 = Entity(model='cube', color=color.blue, position=(-66, 5.8, 285), scale=(0.3, 0.3, 0.5),collider='box', texture = "fig.jpg", on_click = wqp)
butoonlift2 = Entity(model='cube', color=color.red, position=(-66, 4, 322), scale=(0.3, 1, 0.5),collider='box', on_click = ooo)







"""sfrm"""
sfp = Entity(model='cube', color=color.black, position=(1000, 1000, 1000), scale=(5, 1, 5),collider='box')
sfs1 = Entity(model='cube', color=color.black, position=(1000, 1003, 1002.5), scale=(5, 5, 1),collider='box')
sfs2 = Entity(model='cube', color=color.black, position=(1002.5, 1003, 1000), scale=(1, 5, 5),collider='box')
sfs3 = Entity(model='cube', color=color.black, position=(997.5, 1003, 1000), scale=(1, 5, 5),collider='box')
sfs4 = Entity(model='cube', color=color.black, position=(1000, 1003, 997.5), scale=(5, 5, 1),collider='box')
sfpt = Entity(model='cube', color=color.black, position=(1000, 1004, 1000), scale=(5, 1, 5),collider='box')
skafn = Entity(model='cube', color=color.white, position=(1000, 1001, 1001.5), scale=(1), collider='box', texture = "tbk.png", on_click = llp)


"""diet room"""
dietpo = Entity(model='cube', color=color.white, position=(300, 298, 300), scale=(5, 1, 5),collider='box', texture = "ppooiiuuyytt.png")
dietst1 = Entity(model='cube', color=color.white, position=(300, 301, 302.5), scale=(5, 5, 1),collider='box', texture = "ppooiiuuyytt.png")
dietst2 = Entity(model='cube', color=color.white, position=(302.5, 301, 300), scale=(1, 5, 5),collider='box', texture = "ppooiiuuyytt.png")
dietst3 = Entity(model='cube', color=color.white, position=(297.5, 301, 300), scale=(1, 5, 5),collider='box', texture = "ppooiiuuyytt.png")
dietst4 = Entity(model='cube', color=color.white, position=(300, 301, 297.5), scale=(5, 5, 1),collider='box', texture = "ppooiiuuyytt.png")
dietstpoto = Entity(model='cube', color=color.white, position=(300, 304, 300), scale=(5, 1, 5),collider='box', texture = "ppooiiuuyytt.png")




hand = Entity(parent=camera.ui, model='cube', color=color.blue, scale=(0.1, 0.1, 0.7), position=(0.84,-0.45,0.3), rotation=(10, 5, 5), visible=False)
deah = Entity(parent=camera.ui, model='cube', color=color.white, scale=(0.1), position=(0, 0, 0), texture = "deah.jpg", visible = False)
yw = Entity(parent=camera.ui, model='cube', color=color.white, scale=(1), position=(0, 0, 0), texture = "yw.jpg", visible = False)



player = FirstPersonController(collider="box")







def input(key):
    if key == 'escape':
        exit()
    if key == 'f':
        sound16.stop()
    if key =='shift':
        player.speed = 15
    if key =='shift up':
        player.speed = 5

text_display = Text(text="Натисніть shift щоб бігти", color=color.white, position=(0,0.4), origin=(0,0), scale=2, visible=False)

player.speed = 5

# Функція для перевірки зіткнення
def update():
    if player.intersects(polroom3).hit:  # Якщо є зіткнення
        text_display.visible = True
    else:
        text_display.visible = False





    if deah19room7.intersects(player).hit:
        invoke(jhu, delay=0.1)

    if figyra.intersects(player).hit:
        invoke(jhu, delay=0.1)
    
    if deah27room7.intersects(player).hit:
        invoke(jhu)

    if rush.intersects(player).hit:
        rush.position = 1000000, 500, 100
        invoke(jhu)



    if seek.intersects(player).hit:
        invoke(jhu)

    if player.intersects(seek).hit:
        invoke(jhu)

    

    if player.y < -5:
        invoke(jhu, delay=0.1)

app.run()
