# Opgave
Jætterne har forvoldt kaos i Asgaard ved at hacke en vigtig server og krypteret essentielle filer med deres ransomware. De kræver løsepenge for at frigive dem, men heldigvis har de lavet fejl i deres kode, som gør den langt fra uigennemtrængelig.

Under undersøgelsen blev både ransomware-programmet og en krypteret fil fundet.

**Advarsel:** Ransomware-programmet er live-malware og kan udføre skadelige handlinger. Undersøg det kun i et sikkert og isoleret miljø, eksempelvis en virtuel maskine uden netværksforbindelse.

Vedhæftet fil: Ragnarok.zip

---

# Løsning

Jeg unzipper filen hvori der ligger **Raganarok.exe** og **flag.txt.ragnarok**

Opgaven går ud på at finde ud af hvordan **flag.txt.raganrok** er blevet krypteret og så dekryptere den.

Jeg åbner filen i Ghidra og klikker på **.text** øverst til venstre i programmet.

.text er der hvor selve koden begynder at køre. Jeg scroller ned igennem koden for at finde der hvor filen bliver krypteret.

Efter lidt scrollen finder jeg nedenstående funktion:

```c
void __cdecl FUN_00401160(LPCSTR param_1)
{
  BOOL BVar1;
  DWORD local_24;
  uint local_20;
  uint local_1c;
  LPVOID local_18;
  DWORD local_14;
  HANDLE local_10;

  local_10 = CreateFileA(param_1, 0xc0000000, 0, (LPSECURITY_ATTRIBUTES)0x0, 3, 0x80, (HANDLE)0x0);
  if (local_10 != (HANDLE)0xffffffff) {
    local_14 = GetFileSize(local_10, (LPDWORD)0x0);
    if (local_14 == 0xffffffff) {
      CloseHandle(local_10);
    } else {
      local_18 = (LPVOID)FUN_004048bf(local_14);
      if (local_18 == (LPVOID)0x0) {
        CloseHandle(local_10);
      } else {
        BVar1 = ReadFile(local_10, local_18, local_14, &local_1c, (LPOVERLAPPED)0x0);
        if ((BVar1 == 0) || (local_1c != local_14)) {
          FUN_004048ca(local_18);
          CloseHandle(local_10);
        } else {
          for (local_20 = 0; local_20 < local_14; local_20 = local_20 + 1) {
            *(char *)((int)local_18 + local_20) =
                 (char)(((int)*(char *)((int)local_18 + local_20) +
                        (int)s_Jotunheim_0041b000[local_20 % 9]) % 0x100);
          }
          SetFilePointer(local_10, 0, (PLONG)0x0, 0);
          WriteFile(local_10, local_18, local_14, &local_24, (LPOVERLAPPED)0x0);
          FUN_004048ca(local_18);
          CloseHandle(local_10);
        }
      }
    }
  }
  return;
}
```

Denne kode krypterer filen en byte af gangen og bruger hvert bogstav i stringen **Jotunheim**. stringen bliver gået igennem cyklisk så første byte bliver krypteret med J go det samme gør tiende byte.

Bytesne i filen bliver lagt sammen med det bogstav i **Jotunheim** man er nået til med modulus 256 så det stadig kun fylder 1 byte. Denne nye byte erstatter så den gamle i filen.

Det kan beskrives som denne formel:

`krypterede_byte = (originale_byte + Jotunheim_byte) mod 256`

Fordi krypteringen blot er addition og modulus og at alle bytes ikke kan tage en værdi større end 256 kan vi dekryptere hver byte ved denne formel:

`orginale_byte = (krypterede_byte - Jotunheim_byte + 256) mod 256`

Dette har jeg lavet et python script, **decrypt.py**, til som tager filen **flag.txt.ragnarok** og dekrypterer.

Outputtet fra dette script er: **FDCA{n0_r4ns0m_4_j07un}**, som er flaget for i dag

---
