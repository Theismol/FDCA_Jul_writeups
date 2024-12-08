# Opgave

Vi har modtaget kritisk efterretning fra Asgård: Jætterne har stjålet hemmelige dokumenter fra gudernes arkiver, og de planlægger at bruge informationerne til at ødelægge Yggdrasil én gang for alle. Det eneste spor vi har, er et billede fundet efterladt i en af Jætternes skjulte lejr. Odin mener, at dette billede kan indeholde skjulte data, der kan føre os til de stjålne dokumenter.

Din opgave er at undersøge billedet for skjulte informationer. Kan du finde ud af, hvad Jætterne har gemt? Jætterne har været snedige og sat flere forhindringer på vejen. Held og lykke, for Asgårds skæbne afhænger af dig!

vedhæftet fil: Yggdrasil.zip

---

# Løsning

Jeg unzipper filen, hvor der indeni ligger Yggdrasil.jpeg.

Jeg forsøger med en del forskellige stegonography tools som exiftool, strings og binwalk, men finder ikke noget.

Til sidst kører jeg `steghide extract -sf Yggdrasil.jpeg` uden at bruge en passphrase og fra dette får jeg filen SuperHemmeligt.zip

Jeg prøver at unzippe den, men den er password protected.

Jeg bruger John The Ripper til at prøve at brute force passwordet

`john2zip SuperHemmeligt.zip > hash.txt`

`john hash.txt`

Her får jeg password **ragnarok**

Jeg unzipper .zip filen hvor der kommer tre folders **KageOpskrifter til jul**, **Papirkurven** og **ThorMemes**

Jeg starter med at kigge i **Papirkurven**, hvor folderen **HemmeligePlaner** ligger.

I denne folder ligger filen Hemmelig_Plan.docx, hvori der står En særlig opmærksomhed vil blive givet til brugen af **metadata** i digitale dokumenter og filer.

I folderen ligger der også tre jpeg **Dagger.jpeg**, **Key.jpeg** og **Mjolnir_jail.jpeg**

Jeg kører exiftool på alle tre, hvor der under author er en base64 encoded string. Decoder man stringen fra filen **Mjolnir_Jail.jpeg** får man FDCA{my_pr3c1ous_d4t4}, som er flaget for i dag



---
