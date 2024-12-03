# Opgave


Jætterne har igen skabt problemer! Thor har opdaget, at nogen har stjålet et vigtigt flag fra hans system. Sporene peger på, at det er sket lidt efter lidt. Thor har sendt os en logfil, men vi har brug for din hjælp til at finde ud af, hvad der er blevet stjålet.

Vedhæftet fil: handout.evtx

---

# Løsning

For at kunnne læse hvad der står i **handout.evtx** filen bruger jeg cli toolet **python-evtx** som laver evtx filen om til en human readable xml fil som jeg derefter kan åbne.
Jeg kigger lidt gennem filen og ser nogle interesanter linjer:

```xml
<Data Name="CommandLine">python  eksfiltration.py</Data>
<Data Name="CurrentDirectory">C:\Users\fdcactf\Desktop\hackernes hemmelige v&#230;rkt&#248;jer\</Data>

```


Her kan vi se at hackerne har kørt et python script for at eksfiltrere noget data (Nok Thors flag)

Scroller man længere ned ser man disse linjer som viser en DNS query lavet til et mistænkeligt domæne
```xml
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" />
    <EventID Qualifiers="">22</EventID>
    <Version>5</Version>
    <Level>4</Level>
    <Task>22</Task>
    <Opcode>0</Opcode>
    <Keywords>0x8000000000000000</Keywords>
    <TimeCreated SystemTime="2024-11-24 20:32:19.772343" />
    <EventRecordID>9066</EventRecordID>
    <Correlation ActivityID="" RelatedActivityID="" />
    <Execution ProcessID="3332" ThreadID="748" />
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel>
    <Computer>fdca-forensic</Computer>
    <Security UserID="S-1-5-18" />
  </System>
  <EventData>
    <Data Name="RuleName">-</Data>
    <Data Name="UtcTime">2024-11-24 20:32:18.714</Data>
    <Data Name="ProcessGuid">{e6661070-8d52-6743-8806-000000000600}</Data>
    <Data Name="ProcessId">8360</Data>
    <Data Name="QueryName">F.e3y8h.hackerneivalhalla.dk</Data>
    <Data Name="QueryStatus">9003</Data>
    <Data Name="QueryResults">-</Data>
    <Data Name="Image">C:\Users\fdcactf\AppData\Local\Programs\Python\Python313\python.exe</Data>
    <Data Name="User">fdca-forensic\fdcactf</Data>
  </EventData>
</Event>

```


Der er en del af disse og kigger man på første bogstav i hvert **QueryName** for DNS til dette domæne begynder et mønster at tegne sig.

Jeg har lavet et python script **flag_get.py** som finder alle DNS queries til hackerneivalhalla.dk og hiver det første bogstav ud og samler dem alle i en streng.

Output fra denne fil er **FDCA{Valhalla_Hackerne_Er_Snu}** som er flaget for i dag

---
