# Opgave
Julen nærmer sig med stormskridt, og Thor har igen formået at skabe problemer. Denne gang har han mistet den hemmelige kode, der skulle aktiveres for at starte festen i Asgård! Odin var overbevist om, at en digital løsning var fremtiden og havde fået Loke til at udvikle et system, hvor kun den rette kode kunne låse op for Valhallas julefest.


Men selvfølgelig havde Loke en skjult dagsorden, og nu vil han ikke give koden tilbage og skrev bare, “Alt hvad der skal bruges, er i systemet. God jul… eller måske ikke…”

vedhæftet fil: jul.dll

---

# Løsning

Jeg kører strings på filen for at se om der gemmer sig et nemt flag. Det gør der ikke, men baseret på outputtet kan jeg se at filen er compiled .NET kode og at der er en class i filen der hedder FlagSpiseren.

jeg åbner filen i dotPeek, som er en .NET decompiler, hvor jeg kan åbne FlagSpiseren som ser således ud:

```csharp
public static class FlagSpiseren
{
  public static void Main()
  {
    Console.WriteLine("HA! Jeg har gemt flaget i min mave og du finder det ALDRIG!");
    byte[] numArray1 = new byte[22]
    {
      (byte) 12,
      (byte) 33,
      (byte) 36,
      (byte) 9,
      (byte) 26,
      (byte) 22,
      (byte) 41,
      (byte) 22,
      (byte) 29,
      (byte) 13,
      (byte) 107,
      (byte) 9,
      (byte) 19,
      (byte) 74,
      (byte) 8,
      (byte) 29,
      (byte) 44,
      (byte) 76,
      (byte) 17,
      (byte) 61,
      (byte) 1,
      (byte) 15
    };
    string str = "JegHarGemtFlagetBagXor";
    byte[] numArray2 = new byte[str.Length];
    for (int index = 0; index < str.Length; ++index)
      numArray2[index] = (byte) ((uint) str[index] ^ (uint) numArray1[index]);
  }
}
```
I denne kode skal vi XOR stringen "JegHarGemtFlagetBagXor" med tallene i arrayet.
Fordi jeg er elendig til at kode omskrev jeg koden ovenfor til Python for at finde flaget i filen **xor.py**

Outputtet fra dette er: **FDCA{dnspy-er-min-ven}**, som er flaget for i dag

---
