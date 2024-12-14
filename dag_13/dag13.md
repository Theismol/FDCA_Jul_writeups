# Opgave

Vi har opsnappet et meget kryptisk signal mellem Hel og Loke. Det har dog vist sig besværligt at bryde deres Ase Existens Skjuler kryptering, selvom nøglen allerede stod deri, og ECB burde være easy at knække. Det er som om vi bare bliver ved med at få samme resultat, når vi prøver at dekryptere den.

Måske du har bedre held med at knække signalet?

Vedhæftet fil: signal.7z

---

# Løsning

Zip filen indeholder filen **suspicious_signal.bin**

Denne fil indeholder denne streng i toppen af filen og ellers bare en masse binary: **key=E30A381668FFD6F1CE634C7B58D164328990267A1F124A3838F9A7EA8AD0E464**

Denne key skal vi nok bruge til at decrypte resten af filen.

Jeg smider filen ind i CyberChef og decrypter med keyen og får som resultat en ny key efterfulgt af en masse binary.

Jeg laver denne procedure et par gange, men finder hurtigt ud af at det vil tage for lang tid at gøre manuelt.

Jeg laver derfor et script hvor jeg trækker de første 69 karakterer ud af filen, som svarer til keyen + et linjeskift, decrypter resten af filen og fjerner padding so data i filen har en størrelse som er en multiple af 16. Dette gøres indtil flaget er dekrypteret: **FDCA{B3tter_don3_tha7_aut0matic4lly}**

---
