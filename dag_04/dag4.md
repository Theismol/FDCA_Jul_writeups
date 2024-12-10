# Opgave


Vi har modtaget efterretning om, at en spion i Asgard har været i kontakt med jætternes spion-hotline. Vi har opsnappet et telefonopkald, hvor spionen indtastede deres spionnummer.

Vi har brug for din hjælp til at identificere det indtastede spionnummer, så vi kan komme tættere på at afsløre deres identitet.

Lav flaget ud fra FDCA{spionnummer}

Flag eksempel:
FDCA{123456789}



Vedhæftet fil: OpsnappetOpkald.wav

---

# Løsning

Jeg åbner .wav filen i Audacity og afspiller den. I lydfilen hører man en robotstemme sige at hackeren skal indtaste sit spionnummer hvorefter man hører nogle høje lyde.

Lydene lyder meget som når man taster et telefonnummer ind på sin telefon. Dette hedder **Touch Tone** og gennem 2 unikke frekvenser kan man identificere tallene fra 0-9.

Her kan du blot tage din telefon frem og så prøve dig frem med tallene indtil du hører den samme tone i filen som på din telefon og finde frem til flaget.

En anden måde du kan løse den på er gennem **Fast Fourier Transform** som er en måde at trække de to kendetegnende frekvenser ud af lydfilen og dermed kunne identificere tallene.

Dette har jeg gjort gennem et python script **analyze_wav.py**, hvor jeg har fundet frem til spionnummeret **012500118**.

Flaget er dermed: **FDCA{012500118}**

---
