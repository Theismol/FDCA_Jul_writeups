# Opgave
Cyber-Operations Command Centeret er efter flere dages hårdt arbejde gået fuldstændig sukkerkold, så kokken Andrimner finder dokumentet med æbleskivernes lokation frem fra skuffen - men hov! Jætterne har tilsyneladende krypteret teksten!? Heldigvis finder Andrimner krypteringsrunerne, som skurkene i deres hast ud af køkkenets server har tabt i filsystemet.


Kan du dekryptere æbleskiver.runes?

Vedhæftet fil:  JettEncrypt.dll_aebleskiver.runes.zip

---

# Løsning

Jeg unzipper filen, hvor der indeni ligger **æbleskiver.runes** og **JettEncrypt.dll**.

i **æbleskiver.runes** ligger denne string: **uru8voW7zNK0zpi4zY3SltOSqsqQzLOXzc6yggAAAAA=**

base64 decoder man den får man ikke noget der giver mening.

Jeg antager at **JettEncrypt.dll** er en .Net dll og åbner den i DotPeek, som er en .Net decompiler.

Her finder jeg hurtigt classen Encrypter med dette kode:

```csharp
using System;
using System.Text;

#nullable disable
namespace JettEncrypt
{
  public class Encryptor
  {
    public static string encrypt(string ymir)
    {
      byte[] numArray1 = new byte[32];
      Array.Copy((Array) Encoding.UTF8.GetBytes(ymir), (Array) numArray1, ymir.Length);
      byte[] numArray2 = new byte[32];
      for (int index = 0; index < 8; ++index)
      {
        byte[] destinationArray = new byte[4];
        Array.Copy((Array) numArray1, index * 4, (Array) destinationArray, 0, 4);
        Array.Copy((Array) BitConverter.GetBytes(-BitConverter.ToInt32(destinationArray, 0)), 0, (Array) numArray2, index * 4, 4);
      }
      return Convert.ToBase64String(numArray2);
    }
  }
}
```
Denne koder tager en string, konverterer den til et array af 32 bytes og tager 4 bytes af gangen konverterer det til en integer og ændrer fortegnet og ændrer det tilbage til 4 bytes. Til sidst bliver det hele lavet om til en base64 string.

Jeg har lavet et python script som reverser ovenstående encryption **decrypt.py**

Output fra dette python script er: **FDCA{D3-L1gG3r-i-mU5p3Lh31M}**, som er flaget for i dag

---
