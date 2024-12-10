# Opgave
Efter Thors debut på sociale medier har han mistet interessen i at styre vejrforholdene i Midgård. Der er simpelthen alt for mange andre ting som han skal tage sig af. Han har derfor valgt at finde en digital løsning og har  downloadet et program, som kan hjælpe ham med at bestemme, hvordan vejret skal være på en given dag.

Odin er ikke tilfreds med situationen og har samtidig mistanke om, at jætterne kan være involveret. Derfor har Odin bedt dig undersøge programmet nærmere.

vedhæftet fil: WeatherMachine.7z 

---

# Løsning

Jeg unzipper filen hvori der ligger **WeatherMachine.exe**

Jeg kører strings på filen og finder disse interessante linjer:

`Running evil code
a = 2081, b = 25, m = 26
(a * x + b) % m
"If at first you don't succeed, try, try again."
SQPN{XINAGVGRG_E_XINYVGRG}`

**SQPN{XINAGVGRG_E_XINYVGRG}** ligner et krypteret flag, og linjen `(a * x + b) % m` kunne være måden den er krypteret på.

Da jeg ved at starten af flaget er FDCA prøver jeg at putte disse bogstaver ind som x, hvor A-Z er lig et tal fra 1-26.

F: (2081 * 6 + 25) % 26 = 5 = E. Dette tyder på at ligningen måske ikke er blevet brugt til at kryptere alligevel.

Det krypterede flag har mange af de samme bogstaver som går igen, hvilket godt kunne ligne sådan man kryptere med caeser cipher.

Caeser cipher er når man rykker alle bogstaver i en sætning X bogstaver til højre.

13 endte med at være det rigtige tal som giver flaget: **FDCA{KVANTITET_R_KVALITET}**


---
