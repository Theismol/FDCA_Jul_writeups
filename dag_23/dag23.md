# Opgave

Thor har modtaget en besked fra jætterne, som hævder at have krypteret et vigtigt juleflag i en digital gave. Kun de, der kan afkode beskeden og bryde jætternes obfuskerede logik, kan hjælpe Asgård med at genoprette flaget. Kan du finde flaget og redde julen?

Vedhæftet fil: IndpakketGave.zip

---

# Løsning

strings på den ser .net
DotPeek på den
Klasse der hedder P
Dette kode er der 

```csharp
namespace IndpakketGave
{
  internal class P
  {
    private static void Main(string[] args)
    {
      string kG = Resources.kG;
      Console.WriteLine("Velkommen!");
      Console.WriteLine("Venligst indsat flaget:");
      string q = Console.ReadLine();
      byte[] bytes = Encoding.ASCII.GetBytes("valhallahpakkergodegaver");
      byte[] numArray = new byte[16];
      byte[] r = bytes;
      byte[] s = numArray;
      if (string.op_Equality(P.S(P.E(q, r, s)), kG))
        Console.WriteLine("Tillykke dit flag er korrekt!");
      else
        Console.WriteLine("Forkert.");
    }

    private static string E(string q, byte[] r, byte[] s)
    {
      using (AesManaged aesManaged = new AesManaged())
      {
        ((SymmetricAlgorithm) aesManaged).Key = r;
        ((SymmetricAlgorithm) aesManaged).IV = s;
        ((SymmetricAlgorithm) aesManaged).Mode = (CipherMode) 1;
        using (MemoryStream memoryStream = new MemoryStream())
        {
          using (CryptoStream cryptoStream = new CryptoStream((Stream) memoryStream, ((SymmetricAlgorithm) aesManaged).CreateEncryptor(), (CryptoStreamMode) 1))
          {
            using (StreamWriter streamWriter = new StreamWriter((Stream) cryptoStream))
              ((TextWriter) streamWriter).Write(q);
          }
          return Convert.ToBase64String(memoryStream.ToArray());
        }
      }
    }

    private static string S(string q)
    {
      char[] charArray = q.ToCharArray();
      for (int index = 0; index < charArray.Length - 1; index += 2)
      {
        char ch = charArray[index];
        charArray[index] = charArray[index + 1];
        charArray[index + 1] = ch;
      }
      return new string(charArray);
    }
  }
}
```
`S6BpWo8WyKFzwRzntKjW+nuD4+IeeZbMM2OmQcsTf2fgWoE81bOah1hmiPTLOzP`

---
