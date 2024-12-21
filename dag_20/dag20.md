# Opgave


Vi har opsnappet noget netværkstrafik, der tyder på, at Jætterne har haft adgang til Asgårds filservere og har exfiltreret filer. Vi frygter, at nogle af disse filer indeholder følsomme oplysninger, som Jætterne vil bruge til at afpresse Thor.

Denne situation er kritisk, og vi har brug for din hjælp til at finde ud af, hvad der er blevet stjålet, før Jætterne kan gennemføre deres plan.

Vedhæftet fil: capture.7z

---

# Løsning

Jeg unzipper filen og i den ligger **capture.pcap**

Jeg kører kommandoen `strings capture.pcap | grep FDCA` for at se om flaget står i plaintext i filen og får outputtet: **FDCA{Th1s_1s_n0t_th3_fl4g}**

Det ligner et fake flag, men jeg prøver den alligevel og den virkede heller ikke.

Jeg åbner filen og kan se der er en masse ftp connections og der er blevet hentet nogle filer: **flag.txt**, **Very_Secret.docx**, **ThorTheKisser.jpeg***, **ThorMemes.zip**.

Jeg downloader alle filerne og kan se der på billedet i **ThorTheKisser.jpeg** står flaget **FDCA{FTP_15_N07_S3cur3}**

---
