#Opgave(IKKE LØST)

ÅH NEJ!! Jætterne har ændret Odins katte billeder, Odin er dybt bedrøvet over dette og forlanger at dette udbedres. Derfor har han bedt os undersøge, hvad jætterne har gjort ved hans katte.

Vedhæftet fil: cat.zip

#Løsning

zip filen er password protected. Jeg bruger kommando `zip2john cat.zip > hash.txt`som laver en fil som JohnTheRipper kan cracke.

Jeg kører så kommandoen `john hash.txt` og får password **thor123**.

Jeg unzipper filen med passwordet og får 5 filer **cat1.jpg, cat2.jpg, cat3.jpg, cat4.jpg, cat5.jpg**.

Jeg bruger `binwalk`og `exiftool` til at se om der er noget gemt i billederne. i cat5.jpg ligger der en zip fil **42C0F.zip**, men også denne er password protected.

Med exiftool finder jeg en comment i cat4.jpg som er base64 encoded: **IUhlbW1lbGlndF9Lb2Rlb3JkMTMyNA==**. Jeg decoder det og får passwordet **!Hemmeligt_Kodeord1324**. 

Jeg unzipper filen og får en ny fil, som hedder **cat6.jpg**

På denne fil prøvede binwalk, exiftool, steghide, strings, stegsolve, stegseek, men ingen af disse gav flaget.

Til sidst besluttede jeg mig for at brugte et hint som var:

```
The cats on picture 4 love strings, especially the colourful kind! The binary duo on picture 5 just love going on walks. The cat on picture 6 has something in his (steg)hide.
```

Dette hjælper mig så ikke vanvittigt meget når jeg allerde har prøvet med steghide, men nu ved jeg i det mindste at jeg nok skal finde en passphrase.

Jeg tænkte først at et passphrasen måske var **thor123** eller **!Hemmeligt_Kodeord1324** jeg allerde havde brugt kunne være svaret, men ingen af disse virkede. 



