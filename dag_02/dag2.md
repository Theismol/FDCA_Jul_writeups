# Opgave


Midt under juleforberedelserne i Valhalla er en vigtig gave til guderne forsvundet fra en af de fælles computere, der blev brugt i gave hallen!

Gaven, tiltænkt Thor, var omhyggeligt gemt i de digitale haller, men nu er den væk fra computeren. Odin er rasende og mistænker, at Loke står bag endnu et snedigt trick for at skabe kaos i julefreden.
Freja mener at have set Loke gå rundt med et USB-stick.

Vi har fået noget data fra maskinen, måske du kan finde noget?

Vedhæftet fil: 2024-11-23t14.55.47_investigationpackage.zip

---

# Løsning

Jeg har ikke arbejdet med Registry Hives før, men tænker da der står i opgaven at Loke har et USB-Stick at vi skal finde ud af hvad dette USB-stick er.
USB-Stick har ofte bogstaverne D: E: eller F: og jeg kører derfor nedenstående kommando i root af directory:

`grep -r '\\E:' *`

Denne kommando bruger grep med flaget -r som gør at den kigger recursively gennem alle subdirectories og * for at den gør det i alle filer. Jeg får her outputtet:
`grep: Windows/System32/config/SYSTEM: binary file matches
grep: Windows/System32/config/SYSTEM.LOG2: binary file matches
grep: Windows/System32/config/SYSTEM.LOG1: binary file matches
`

Jeg kigger derfor i SYSTEM filen, men da det er en binary som jeg ikke bare kan åbne skal jeg først bruge RegRipper til at trække det nødvendige data ud af filen.

Jeg kører nedenstående kommando:

`regripper -r ./SYSTEM -f system > system.txt`

Nu kan jeg åbne system.txt og lede efter E drevet og her kan jeg under MountedDevices se dette:

`Device: RkRDQXtVU0JfRjBSM041MUM1X1JfTjFDM30=
  \DoSDevices\F:

Device: _??_USBSTOR#Disk&Ven_Kingston&Prod_DataTraveler_80&Rev_PMAP#646E6999356EE7C1B1371C1D&0#{53f56307-b6bf-11d0-94f2-00a0c91efb8b}
  \??\Volume{212d52d8-a3e9-11ef-901e-047bcbc9edf1}
  \DosDevices\E:

Device: DMIO:ID: 34 57 cb 40 c8 0c 16 b2 47 a5 49 bc e0 b9 9c ac
  \DosDevices\C:

Device: \??\SCSI#CdRom&Ven_NECVMWar&Prod_VMware_SATA_CD01#5&260e6d66&0&010000#{53f5630d-b6bf-11d0-94f2-00a0c91efb8b}
  \??\Volume{9fc10d4f-a3ed-11ef-9019-806e6f6e6963}
  \DosDevices\D:`

Her ser device med navnet **RkRDQXtVU0JfRjBSM041MUM1X1JfTjFDM30=** en smule mistænkeligt ud og det ligner det er base64 encoded.

Jeg smider derfor strengen ind i CyberChef og decoder med base64 og får outputtet:

`FDCA{USB_F0R3N51C5_R_N1C3}`

Og dermed har vi flaget.
---

