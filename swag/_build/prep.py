from PIL import Image
import json,os
S='/mnt/project-files/'; O='/home/user/smoky-woods-assets/swag/american-track/img/'
def save(src,name,crop=None,size=640):
    im=Image.open(S+src).convert('RGB')
    if crop: im=im.crop(crop)
    im.thumbnail((size,size),Image.LANCZOS)
    # pad to square white
    c=Image.new('RGB',(max(im.size),)*2,'white');c.paste(im,((c.width-im.width)//2,(c.height-im.height)//2))
    c.save(O+name,quality=80,optimize=True,progressive=True)
tum=['Beach','BerryJam','Black','ChocolateBrown','ChocolateFlagRed','ChocolateLavenderGlitter','Cobalt','CoolGrey','CoolPeriwinkle','CoolPineTree','Denim','Graphite','Navy','Olive','PalePink','Persimmon','White']
sw={}
for t in tum:
    f=f'Rtic20ozTumbler{t}-AmericanTrack.png'
    save(f,f'rtic-{t.lower()}.jpg')
    im=Image.open(S+f).convert('RGB'); px=[im.getpixel((x,y)) for x in range(360,380) for y in range(820,840)]
    sw[t]='#%02x%02x%02x'%tuple(sum(p[i] for p in px)//len(px) for i in range(3))
save('BlackAmmoCan2-AmericanTrack.png','ammo-black.jpg')
save('GreenAmmoCan2-AmericanTrack.png','ammo-green.jpg')
save('Journal-Blue-AmericanTrack.png','journal.jpg',crop=(100,300,820,1330))
save('Journal-Blue-AmericanTrack-Numbered.png','journal-colors.jpg',crop=(0,1300,1728,2250),size=900)
save('MediumMemoryBox-DarkWalnut-AmericanTrack.png','memorybox.jpg',crop=(330,320,1400,1060))
save('MediumMemoryBox-DarkWalnut-AmericanTrack.png','memorybox-sheet.jpg',size=900)
print(json.dumps(sw))
