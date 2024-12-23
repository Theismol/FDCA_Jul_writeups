# Opgave

I et dristigt hack-back forsøg efter Jætterne har krypteret Æsirne, er du blevet udvalgt til at afdække svagheder hos den frygtede ransomwaregruppe JætteBit 2.0. Gruppen skulle angiveligt have terroriseret organisationer verden over, og nu er det tid til at gøre en ende på dem en gang for alle.

Din mission er simpel:
Søg med lys og lygte efter cleartext credentials som kan bidrage til hack-back missionen. Måske har de været så ivrige efter at offentliggøre deres ofre, at de har glemt deres egen sikkerhed som kunne afsløre brugernavne, adgangskoder eller andre følsomme data, gemt i hemmelige filer.

Navigér forsigtigt på deres hjemmeside hvor de lækker data. Men vær varsom – jætterne er eksperter i at opsætte fælder for dem, der kommer for tæt på.

Held og lykke, og må du være den, der bringer Ragnarok til JætteBit 2.0!

Sitet kan findes på http://p9x6m4b2vqz7htfj.onion.jættenettet.dk

Flag er i formatet FDCA{username:password}


---

# Løsning

Hjemmesiden er en kopi af LockBits hjemmeside, hvor man kan betale løsesummen. Trykker man for at betale kommer man ind på siden: `http://jættenettet.dk/betal.php?file=betal.html`, hvor man i Inspector kan se at der er en kommentar i koden: `<!-- ja vi bruger admin:admin -->`. Jeg forsøger med dette som flaget, men det er ikke korrekt.

Jeg kigger derefter på robots.txt og finder hvor der står Disallow: /backend/.

Jeg går til dette link og her er der en masse forskellige træls ting der kører på siden. Den downloader en masse billeder, åbner en masse nye vinduer, som er svære og lukke og så videre. Dette må betyde vi er på den rette vej.

I Debugger er der en fil der hedder index.js med dette stykke kode: `const hemmelige_filer = [
  'intern/hashrevision/jaette_ntds_hashes.txt'
]`

Går man til denne sti får man 403 Forbidden.

Jeg lagde dog mærke til at siden hvor man kan betale er filen specificeret i URL og jeg prøver derfor at ændrer URL til `http://jættenettet.dk/betal.php?file=intern/hashrevision/jaette_ntds_hashes.txt` og her får jeg en masse brugernavne og hashes:

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:6c569aabbf7775ef8fc570e228c16b98:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
jotunheimr:1001:aad3b435b51404eeaad3b435b51404ee:8d777f385d3dfec881f3f8e2d7b2b93b:::
surt:1002:aad3b435b51404eeaad3b435b51404ee:c4ca4238a0b923820dcc509a6f75849b:::
ymer:1003:aad3b435b51404eeaad3b435b51404ee:2c6ee24b09816a6f14f95d1698b24ead:::
skadi:1004:aad3b435b51404eeaad3b435b51404ee:9c56f361f0b66d4b2f4db0b74a5b5c2f:::
loki:1005:aad3b435b51404eeaad3b435b51404ee:9e107d9d372bb6826bd81d3542a419d6:::
angrboða:1006:aad3b435b51404eeaad3b435b51404ee:bad0c6db35173c1b63459db6a1a2a22e:::
fafnir:1007:aad3b435b51404eeaad3b435b51404ee:1f54deae0f9a2ba375c724235ffaaefd:::
hel:1008:aad3b435b51404eeaad3b435b51404ee:9d5ed678fe57bcca4ec8b7b6d4b1e3b7:::
krbtgt:65534:aad3b435b51404eeaad3b435b51404ee:bfb8d96e5176b084ee453de1e6d5a1d0::: 
```
Jeg smider alle hashes ind i crackstation og hashes.com og får følgende passwords:
```
2c6ee24b09816a6f14f95d1698b24ead:openai
31d6cfe0d16ae931b73c59d7e0c089c0:
6c569aabbf7775ef8fc570e228c16b98:password!
9e107d9d372bb6826bd81d3542a419d6:The quick brown fox jumps over the lazy dog
c4ca4238a0b923820dcc509a6f75849b:1
1f54deae0f9a2ba375c724235ffaaefd:netcompany123
```
Jeg prøver alle kombinationer af brugernavne og passwords og får et hit med **fafnir:netcompany123**

Flaget er dermed FDCA{fafnir:netcompany123}


---
