# Opgave:
Thor har fået sin første smartphone – og det går ikke helt som planlagt. I sin begejstring har han delt mere, end hvad godt er, og nu står Asgård over for en potentiel katastrofe. Loke har opsnappet hemmelig information, og jætterne planlægger et angreb på Bifrost-porten.
Din opgave er at undersøge Thors online-profil og finde frem til:
Vagtskifte Tidspunkt ved Bifrost.
Kodeordet til våbenkammeret.
Hvornår Heimdal holder pause.
Dato for Lokes planlagte angreb.

Pas på – Loke er snu, og han gemmer sine spor godt.

Hint: Thor elsker BlueSky og går under navnet @thorthundergod90.bsky.social
Lav flaget i formatet: FDCA{vagtskiftetidspunkt_kodeord_HeimdalsPause_angrebsdato}

Flag Eksempel:
FDCA{15:00_GodKode123_19:00_23/11/2024}

# Løsning
Jeg startede med at gå ind på Thor's bluesky og se på alle hans opslag.
Her er der specielt 4 der er interessante: <br>
I et opslag skriver han: Så skal jeg på vagt igen i dag! #ReadyAt1200, hvilket kunne indikere at vagtskiftet sker klokken 12 <br>
I et andet opslag skriver han: Hver dag kl. 14:30 sker der noget magisk i Asgård – jeg fanger Heimdal i pauserummet, hvor han sidder og leger med ponyer!  Selv den mægtige vogter af Bifrost har brug for lidt hygge. Skal jeg begynde at tage billeder? Dette kunne betyde at Heimdal holder pause klokken 14:30 <br>
Thor har også lavet et par opslag som omhandler koden til våbenrummet. I et opslag skriver han dette: Hør lige her!!! Hvis I også har problemer med at huske jeres koder, ligesom jeg altid har, så har jeg fundet den perfekte løsning! Tatover koden – så glemmer du den aldrig igen! Genialt, ikke? På hans profil kan man også se et billede af en arm med en tatovering hvor der står THUNDER9000. Dette må være koden til våbenrummet. <br>
Til sidst skal vi finde datoen hvor Loke har tænkt sig at angribe Asgård. Loke har kommenteret på en del af Thor's opslag og på hans profil havde han et opslag hvor han snakkede omkring at der kunne ske noget den 13. december i Asgård. <br>
Jeg prøvede derfor flaget: FDCA{12:00_THUNDER9000_14:30_13/12/2024} <br> 
Dette var forkert og på nuværende tidspunkt er opslaget fra Loke omkring den 13. december blevet slettet. <br>
Efter pinligt lang tids undring og de to hints, som ikke hjalp på datoen lagde jeg mærke til at der stod at Thor skulle arbejde 24 timer hos bifrost igen den 24. og den 25. dermed ville være oplagt for Loke at angribe så jeg prøvede som sidste håb dette flag: <br>
FDCA{12:00_THUNDER9000_14:30_25/12/2024} <br>
Og BUM det var korrekt.
