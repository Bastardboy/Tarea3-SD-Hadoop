import wikipedia as wiki


p = ["Fútbol","Canino","Chile","Digimon","Wea","Tango","Node.js","Argentina", "Pokemon", "Turnip Boy Commits Tax Evasion"]

for i in p:
    a = wiki.page(i,auto_suggest=False)
    carpeta = "1" if p.index(i) < 5 else "2"
    with open("./"+carpeta+"/"+str(p.index(i))+"wiki"+str(i.replace(" ", "_"))+".txt", "w") as f:
        f.write(str(p.index(i))+"xdxdxd")
        f.write('\n')
        f.write(a.content)
        f.write('\n')
        f.close()
    print("Escribio el archivo: "+i)
