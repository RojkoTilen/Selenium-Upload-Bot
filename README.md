# SELENIUM UPLOAD BOT
### Aplikacija, ki omogoča samodejno overjanje, ter urejenje in nalaganje datotek na spletno rešitev AudioJungle.

Iz poljubno določenega direktorija se dinamično preberejo vse mape, nato pa program datoteke posameznih map iterativno nalaga na portal AudioJungle. To poteka tako, da se ustvari imenik z vsemi pripadajočimi datotekami posamezne mape. Tekstovna datoteka predstavlja hitrost glasbe v udarcih na minuto, posamezne MP3 datoteke se dinamično preberejo, iz njih pa se ustvari imenik dolžin MP3 datotek, iz ZIP datoteke se prebere naslov skladbe, MP3 datoteka, zaščitena z vodnim žigom pa se razbere v kolikor je v imenu MP3 datoteke beseda ''Watermark''. Iz ustvarjenega imenika se na podlagi števila map v direktoriju, ki ga podamo, začne nalaganje na AudioJungle. Za nalaganje uporabljamo Selenium knjižnico. Na podlagi imena skladbe se pravilno izbere žanr ter pripadajoči opis.

![Selenium Bot Folder 1](https://user-images.githubusercontent.com/57943279/170692041-e4074de6-8d1d-40fc-849b-416f6a4df929.JPG)

![Selenium Bot Folder 2](https://user-images.githubusercontent.com/57943279/170692050-83ac5d80-7828-4f18-88df-38657c9110e8.JPG)


### Tehnološki sklad

* Python
* Selenium 
* Chromedriver

### Vpostavitev aplikacije:

* Prenos paketa.
* Prenos selenium knjižnice in vzpostavitev
* Zamenjava povezav ter uporabniškega imena in gesla za vpis
* Zagon

### Zaslonski posnetki

https://user-images.githubusercontent.com/57943279/170691810-eae5690b-0f59-42f1-9650-58250b3916bd.mp4

