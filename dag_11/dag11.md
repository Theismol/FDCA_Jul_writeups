# Opgave
Vi har modtaget efterretninger om, at dele af vores hemmelige kildekode samt adgangskoder er blevet sat til salg på darkweb. Som led i efterforskningen har vi afhørt vores udvikler “Loke” og beslaglagt hans workstation til nærmere undersøgelse.


Under afhøringen var Loke ikke til stor hjælp; han snakkede konstant om Django, og til sidst var det kun et spørgsmål om sekunder, før IR-holdet, der udførte afhøringen, ville ty til andre metoder for at få ham til at tale. Heldigvis nævnte han dog en detalje, som de formoder er et vigtigt led i efterforskningen. Han nævnte at han engang havde hentet en Python-dependency fra en uofficiel kilde.


Selvom han syntes, det var mistænkeligt, at filerne var pakket i en zip-fil med en adgangskode, blev han beroliget, da kilden allerede havde givet ham koden: “123”.


Loke’s workstation er et digitalt kaos af kode, filer og rod, hvilket har resulteret i at IR holdet nægtede at undersøge den. Kan du hjælpe os med at gennemgå den og finde ud af, hvad der er sket? Vi advarer dog – det er ikke en opgave for de svagelige...


Vedhæftet fil: **developer_image.E01**

---

# Løsning

Jeg åbner filen i Autopsy, som er et program man kan bruge til at analysere disk images i en GUI.

Med det samme ser jeg at der blevet downloaded en del filer fra internettet og især disse to filer er interessante:

**django-main.zip** og **PythonExtendedLibrary_v4.3.1.zip**

Jeg extracter begge filer fra Autopsy, men kun **PythonExtendedLibary_v4.3.1.zip** skulle bruge passworded 123 fra opgaveteksten så det er kunne denne jeg fokuserer på.

Jeg kigger igennem filerne, men der er så mange det er lidt uoverskueligt.

Jeg bruger normalt NeoVim som min IDE og der har jeg et plugin som hedder Telescope, som gør man kan søge efter tekst gennem alle filer i et directory. Jeg bruger dette i root af directory og søger på FDCA, da jeg ved flaget altid starter med dette. Her kom der dog ikke noget frem, men i tidligere opgaver har flaget været base64 encoded så jeg prøver i stedet at søge på **RkRDQ**, som er FDCA i base 64.

Her finder jeg nedenstående linje i filen **ISO/userprofiles/storage/python_runtime.pyw**

**WEBHOOK='aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTMwMjcwNDU1MTAyMzc2MjgyMy93M0hqWURfRkRDQXtweTdoMG5fazN5MTA5OTMyX2QxNWMwMmRfM3hmMTF9'**

Jeg prøver at decode linjen og får:

**https://discord.com/api/webhooks/1302704551023762823/w3HjYD_FDCA{py7h0n_k3y109932_d15c02d_3xf11}**

Her ser vi flaget **FDCA{py7h0n_k3y109932_d15c02d_3xf11}**

---
