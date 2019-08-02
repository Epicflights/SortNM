from tkinter.filedialog import askopenfilename, askdirectory
import tkinter as tk
root = tk.Tk()
root.withdraw()
ntmfile = askopenfilename()

defdir = askdirectory()

def rechercheFree(filename,word):
    logs = 0
    with  open(filename) as f:
        for line in f:
            if word in line:
                print(line)
                charline = line
                logs += 1
    return logs

plmnFree = '4G;208;15';
plmnOR = '4G;208;1;';
plmnBT = '4G;208;20';
plmnSFR = '4G;208;10';

fr = rechercheFree(ntmfile,plmnFree)
OR = rechercheFree(ntmfile,plmnOR)
bt = rechercheFree(ntmfile,plmnBT)
sfr = rechercheFree(ntmfile,plmnSFR)

#summary
print('---------------------------------------------------------------------------------------------------------------')
print(str(fr)+" Instances de "+str(plmnFree)+" trouvées dans "+str(ntmfile))
print(str(OR)+" Instances de "+str(plmnOR)+" trouvées dans "+str(ntmfile))
print(str(bt)+" Instances de "+str(plmnBT)+" trouvées dans "+str(ntmfile))
print(str(sfr)+" Instances de "+str(plmnSFR)+" trouvées dans "+str(ntmfile))

file = open(ntmfile , 'r')
file2 = open(defdir+'/20801.ntm' , 'w')
file3 = open(defdir+'/20810.ntm' , 'w')
file4 = open(defdir+'/20815.ntm' , 'w')
file5 = open(defdir+'/20820.ntm' , 'w')
for line in file.readlines():
    if plmnOR in line:
     file2.write(line)
    elif plmnFree in line:
     file4.write(line)
    elif plmnBT in line:
     file5.write(line)
    elif plmnSFR in line:
     file3.write(line)

file.close()
file2.close()
file3.close()
file4.close()
file5.close()

