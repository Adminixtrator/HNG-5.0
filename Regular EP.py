import re

genome = re.compile(r'\d\d\d-\d\d\d-\d\d\d-\d\d\d\d') 
june = re.compile(r'ADMINIXTRATOR')
gnome = ('''My name is ADMINIXTRATOR. Phone number is
 234-705-664-3929.
land line is 234-705-433.''')
print('\n')
for gool in gnome.split():
    if genome.match(gool) or june.match(gool):
        print('.'*70, "\n \t Match found :",repr(gool),"\n"+"."*70)
        print ("Index is",gnome.index(gool),'.'*70,"\n")         	
    else:
        print ("No match found :",repr(gool))