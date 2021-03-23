"""
extemporaneous adventure ride sharing
eager allosaur romp session
eclectic ad-hoc rules for storytelling
easily amused ? ?
entropic adiabatic rocket surgery
enemy assault repulsion 
extraterrestrial atmospheric research starship
exogenic alternate reality shear
entertaining ad-free ? show
erect adders rampant sarcelly
? ? rusticating sojourn
edition amended, revised, streamlined
escalating anarchist rent strike
endearing adorable ray of sunshine
? ashy rummage shop
euclidean ? rectilinear space
"""

import random

with open("/usr/share/dict/words") as f:
    words = [line.strip() for line in f]

lists = [[w for w in words if w.startswith(c)] for c in 'ears']
for i in range(50):
    print(*map(random.choice, lists))
