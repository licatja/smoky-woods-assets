# Builds swag/american-track/index.html (web) and a preview with inlined images.
import base64,os,sys
B=os.path.dirname(os.path.abspath(__file__))
D='/home/user/smoky-woods-assets/swag/american-track/'
t=open(os.path.join(B,'template.html')).read()
form=sys.argv[1] if len(sys.argv)>1 else ''
open(D+'index.html','w').write(t.replace('__IMG__','img/').replace('__FORM_LINK__',form))
def inl(f):
    ext='png' if f.endswith('.png') else 'jpeg'
    return 'data:image/%s;base64,'%ext+base64.b64encode(open(D+'img/'+f,'rb').read()).decode()
p=t.replace('__FORM_LINK__','')
names=[f[:-4] for f in os.listdir(D+'img') if f.endswith('.jpg')]
m='{'+','.join('"%s":"%s"'%(n,inl(n+'.jpg')) for n in names)+'}'
p=p.replace('var IMG = "__IMG__";','var IMG = "";var __M='+m+';')
p=p.replace('return IMG+c[2]+".jpg"','return __M[c[2]]').replace('return IMG+it.img+".jpg"','return __M[it.img]').replace('return IMG+it.colors[0][2]+".jpg"','return __M[it.colors[0][2]]').replace('IMG+it.more[1]+".jpg"','__M[it.more[1]]')
assert '__IMG__' not in p
open(os.path.join(B,'preview.html'),'w').write(p)
