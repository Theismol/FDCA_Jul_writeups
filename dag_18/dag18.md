# Opgave

Thor, den mægtige tordengud, har udført en utrolig bedrift – han har kastet Mjølner, sin legendariske hammer, med så enorm kraft, at den nu kredser om Jorden i en uendelig himmelsk bane. Men Mjølner er jo ikke bare et almindeligt våben. Overladet med elektricitet sender den kraftige lynimpulser ned mod planeten. Disse impulser er ikke kun ødelæggende gnister; de bærer mystiske signaler på tværs af det elektromagnetiske spektrum, krypteret med Mjølners krav til Thor, for at vende tilbage til sin retmæssige herre.

Thor, fast besluttet på at genvinde sin elskede hammer, har tilkaldt FDCA for hjælp. Jeres mission: opfang signalet, afslør dets kryptiske besked, og dekrypter den guddommelige kryptering for at bringe Mjølner tilbage til Thor.

Jordstationen har en en hjemmeside der kan få dig igang her:
http://groundstation.jul.fdca.dk

Vedhæftet fil: thorbit-recv.grc

---

# Løsning

Jeg havde aldrig set en .grc fil før, men efter lidt googling fandt jeg ud af at det er en fil som kan åbnes med programmet GNU Radio Companion.

Jeg downloader derfor dette program og åbner filen. Jeg kan dog se her at vi mangler en ip og en port at kalde og at sym_rate er tom.

Jeg åbner hjemmesiden der er er linket til i opgaven åbner **Inspector**, hvor der står disse kommentarer:

```
<!-- Husk, vi skal bruge jordstationens domæne eller ip addresse, og port 1337 for at behandle signaler fra den. -->
<!-- sps == verdener i nordisk mytologi -->
```

IP og port ender derfor med at være `groundstation.jul.fdca.dk:1337`

Der er 9 verdener i nordisk mytologi og sps er udregnet ved SPS = (samp_rate/sym_rate).

Vi kan se i .grc filen at samp_rate er (4242*9) og hvis SPS er 9 må sym_rate være 4242.

Jeg sætter disser værdier ind i filen og klikker `generate the flow graph`

Dette skaber et python script `temp.py`, som når man kører får man dette output i terminalen (Jeg tror potentielt man skal vente op til 10 minutter for at få outputtet):

```
***** VERBOSE PDU DEBUG PRINT ******
()
pdu length = 18 bytes
pdu vector contents = 
0000: 5a 58 57 55 7b 6d 67 34 35 62 5f 61 31 34 68 6e
0010: 35 7d
************************************
```

Oversætter man disse hexadecimal værdier til ascii får man stringen: **zxwu{mg45b_a14hn5}**

Min første tanke er at dette er en caeser cipher af flaget, som er hvor man rykker alle bogstaver et bestemt antal til højre i alfabettet.

Vi ved at det flaget starter med FDCA, så krypteringen må være sket ved at rykke alle bogstaver 20 (længden fra F til Z).

Derfor kan vi dekrypterer ved at rykke alle bogstaverne 20 tilbage og dermed får vi: **FDCA{sm45h_g14nt5}**, som er flaget for i dag



---
