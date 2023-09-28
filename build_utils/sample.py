test_md = """
<iframe src="./naslovna_stranica.html" style="width: 100%; height: 100%; border: none;"></iframe>
asdasdasd
<div></div>
# Sadržaj <!-- omit in toc -->
- [1. Uvod](#1-uvod)
- [2. Teorijski okvir](#2-teorijski-okvir)
  - [2.1. Osnovni termini i oblast u kojoj se praksa radi](#21-osnovni-termini-i-oblast-u-kojoj-se-praksa-radi)
    - [2.1.1. Embedded programiranje](#211-embedded-programiranje)
    - [2.1.2. Internet of Things](#212-internet-of-things)
    - [2.1.3. Cloud computing - računarstvo u oblaku](#213-cloud-computing---računarstvo-u-oblaku)
  - [2.2. Organizacija rada](#22-organizacija-rada)
    - [2.2.1. Sastanci - tehnički deo](#221-sastanci---tehnički-deo)
    - [2.2.2. Sastanci - netehnički deo](#222-sastanci---netehnički-deo)
    - [2.2.3. Struktura ljudi](#223-struktura-ljudi)
  - [2.3. Ključni korišćeni alati](#23-ključni-korišćeni-alati)
    - [2.3.1. Arduino ekosistem](#231-arduino-ekosistem)
    - [2.3.2. Qt Framework](#232-qt-framework)
- [3. Sadržaj projekta](#3-sadržaj-projekta)
  - [3.1. Šira slika projekta](#31-šira-slika-projekta)
    - [3.1.1. Primer primene, davanje konteksta](#311-primer-primene-davanje-konteksta)
    - [3.1.2. Korišćeni alati (upitno da li treba uz ključne)](#312-korišćeni-alati-upitno-da-li-treba-uz-ključne)
  - [3.2. Struktura projekta - hardware](#32-struktura-projekta---hardware)
    - [3.2.1. Arduino razvojna ploča i firmware](#321-arduino-razvojna-ploča-i-firmware)
      - [3.2.1.1. Arduino Uno](#3211-arduino-uno)
      - [3.2.1.2. Shields i clicks](#3212-shields-i-clicks)
    - [3.2.2. Raspberry Pi kao posrednik](#322-raspberry-pi-kao-posrednik)
    - [3.2.3. "Hardver" cloud platforme?](#323-hardver-cloud-platforme)
    - [3.2.4. Hardver krajnjeg korisnika](#324-hardver-krajnjeg-korisnika)
  - [3.3. Struktura projekta - sofware](#33-struktura-projekta---sofware)
    - [3.3.1. Arduino firmware](#331-arduino-firmware)
    - [3.3.2. Raspberry Pi Cloud Client](#332-raspberry-pi-cloud-client)
    - [3.3.3. WolkAbout Cloud platforma](#333-wolkabout-cloud-platforma)
    - [3.3.4. PC (ili Android) Data Visualizer](#334-pc-ili-android-data-visualizer)
- [4. Zaključak](#4-zaključak)
- [5. Literatura](#5-literatura)

---
<div style="page-break-before: always;"></div>
# I  Uvod
Praksu sam obavio u kompaniji [**Execom**](execom.eu), koju je u međuvremenu kupio [**HTEC**](). U pitanju je *outsourcing* kompanija koja ima niz timova, svaki od kojih radi na uglavnom jednom projektu za eksternog klijenta. Timovi se bave različitim tehnologijama, u zavisnosti od potreba klijenta.

Kao i svaka *outsourcing* kompanija, nema svoje interne projekte, već ih isključivo uslužno pravi za druge. Važno je napomenuti da je njihov nekadašnji interni projekat prerastao u tzv. *spin off* kompaniju [**WolkAbout**](), čije cloud tehnologije smo koristili na projektu koji sam izradio.

Tim u koji sam primljen bavi se sa **IoT** (*Internet of Things*) i **Embedded** tehnologijama i u tom momentu je radio sa dva različita klijenta na proizvodima koji su njima bili potrebni, o čijim detaljima ne mogu govoriti zbog NDA (Non-disclosure agreement) koji sam potpisao.

[...]


### 3.3.3. Software - Arduino firmware
Jednostavno povezivanje bilo kojeg eksternog uređaja, kao što su ovi klikovi, kako hardverski a tako i softverski je ključna odlika Arduino ekosistema. Da bismo iz firmwarea Arduino razvojne ploče slali komande u komponente, potrebno je jednostavno instalirati softverske pakete/ekstenzije namenjene za rad sa tim eksternim uređajem. Razlog zašto toliki dijapazon eksternih uređaja ima svoje paekte, leži u tome da je ceo ekosistem Open Source, te da mu bilo ko može doprinositi.

Za senzore vazduha koristio sam C biblioteke razvijene od kompanije Adafruit, koja je dosta zastupljena i prepoznata u ovoj branši, i to:  

1. **Adafruit_BME680.h** - specijalizovan za Bosch-ov detektor BME680 korišćen na ovom *environment click*-u.  
2. **Adafruit_Sensor.h** - osnovna biblioteka za sve vrste senzora, na koju se specijalizovane biblioteke oslanjaju.  

Pored toga korišćene su još dve biblioteke za ove senzore (bme680.h, bme680_defs.h) u razvojnom procesu, ali u krajnjoj verziji nisu imale značajan uticaj.

Za Bluetooth komunikaciju niske energije (BLE - Bluetooth Low Energy) korišćena je biblioteka **BLEPeripheral.h**

## 3.4. Raspberry Pi - posrednik
### 3.4.1. Hardware - Raspberry Pi
**Raspberry Pi** je serija malih računara na jednoj ploči (SBCs) razvijenih u Ujedinjenom Kraljevstvu od strane Fondacije Raspberry Pi u saradnji sa Broadcom-om. Originalni cilj Raspberry Pi projekta bio je promocija osnovnog računarskog obrazovanja u školama. Originalni model postao je popularniji nego što je bilo očekivano, prodavajući se izvan svoje ciljne tržišne niše za upotrebe kao što su robotika. Široko se koristi u mnogim oblastima, kao što su nadgledanje vremenskih uslova, zbog svoje niske cene, modularnosti i otvorenog dizajna. Obično ga koriste zaljubljenici u računare i elektroniku, zbog njegovog usvajanja HDMI i USB standarda.

![Fotografija Raspberry Pi 3 Model B, poput onog korišćenog na praksi](images/image-12.png)

Nakon izdavanja druge vrste ploče, Fondacija Raspberry Pi je osnovala novi entitet, nazvan Raspberry Pi Trading, i postavila Ebena Uptona za izvršnog direktora, sa odgovornošću za razvoj tehnologije. Fondacija je ponovo posvećena kao obrazovna dobrotvorna organizacija za promociju osnovnog računarskog obrazovanja u školama i  zemljama. Većina Pis-a se proizvodi u Sonijevoj fabrici u Pencoedu u Velsu, dok se drugi proizvode u Kini i Japanu.

2015, Raspberry Pi je postao najprodavaniji britanski računar.

Ono što je za njih zanimljivo jeste, pored neograničene primene u projektima entuzijasta i hobista, jeste da u potpunosti mogu poslužiti kao desktop računari, sa sve periferijama (tastatura, miš, monitor). Na njega smo zakačili BLE 4.0 prijemnik koji je primao poruke sa Arduina (očitane vrednosti sa senzora). Putem Ethernet (LAN) kabla se kačio na internet i komunicirao sa cloud platformom WolkAbout.

### 3.4.2. Software - Raspberry Pi Cloud Client
Softver za Raspberry Pi je razvijen u programskom jeziku C++. U početku smo za razvoj koristili SSH vezu, tako da je RPi bio u "headless" režimu. To znači da sam razvoj radio na svom stonom računaru, i onda slao code, slično radu sa Arduinom. Usled mnogobrojnih problema u komunikaciji mog Windows računara i Linux-a na RPi (Raspberry Pi OS) prešli smo na upotrebu RPi kao samostalnog računara, povezanog na TV sa svojim periferijama (miš, tastatura).

Program se bavi prikupljanjem podataka sa BLE (Bluetooth Low Energy) konekcije sa Arduinom i njihovim slanjem na WolkAbout IoT platformu. Od biblioteka, korišćene su:
1. Gattlib++ za BLE komunikaciju
2. Wolk.h za komunikaciju sa WolkAbout platformom (bazirano na MQTT protokolu)

Početna Podešavanja
Definisan je enum `AirCharacteristic` sa vrednostima `TEMP`, `HUMI`, i `PRES`.
Napravljena je globalna instanca `wolk` klase `Wolk`.
Inicijalizovana je centralna jedinica za BLE sa imenom `arduino`.
Definovane su UUID-ove (Unique Universal Identifiers) za BLE uređaj, servise i karakteristike.

Funkcije za Obaveštenja
`notificationCallback`: Ova funkcija se poziva svaki put kada stigne obaveštenje sa BLE uređaja. U zavisnosti od vrste karakteristike (TEMP, PRES, ili HUMI), podaci se dodaju u `wolk` instancu i ispisuju se na standardni izlaz.
`tempCallback`, `presCallback`, `humiCallback`: Ovi pozivi su specijalizovani slučajevi notificationCallback-a za određene tipove podataka (temperatura, pritisak, vlažnost).

`main()` funkcija
1. Wolk Setup: Kreira se Wolk uređaj sa određenim kredencijalima i uspostavlja se veza sa WolkAbout platformom.
2. BLE Setup: Inicijalizuje se BLE i povezuje se na BLE uređaj.
   - Ako je uspešno omogućena BLE veza, postavljaju se parametri veze i povezuje se sa BLE uređajem. Nakon toga,započinju se obaveštenja za odabrane servise i karakteristike.
   - Ako povezivanje ne uspe, veza sa WolkAbout platformom se prekida i program se završava.
3. Glavna Petlja: Kontinuirano se obrađuju asinhroni događaji sa BLE uređaja i program spava na kratko između iteracija.

## 3.5. WolkAbout Cloud Platforma - centrala informacija
### 3.5.1. "Hardware" Cloud platforme?
Kao što je pomenuto u [1.3. Cloud computing - računarstvo u oblaku](#213-cloud-computing---računarstvo-u-oblaku) glavna vrednost je upravo u tome da se developer ne mora baviti hardverskim pojedinostima, već isključivo apstrakcijom i softverom.

### 3.5.2. Software - konfigurisanje, povezivanje, monitoring
**WolkAbout Cloud** platforma je gotov proizvod koji se minimalno programira, već jednostavno koristi putem GUI-ja. Potrebno je ulogovati se sa svojim kredencijalima (koji se dobijaju onda kada se korišćenje njihovih usluga plati, i svako korišćenje se prebrojava i sabira).



U njoj je bilo potrebno da okvirno opišem kakve uređaje imam, kakvim podacima barataju. Bilo je moguće dizajnirati tzv *dashboard* putem kojeg se može vizualno pratiti promet podataka (i tako proveriti da li isprogramirane komponente ispravno rade svoj posao).

## 3.6. Krajnji korisnik
### 3.6.1. Hardware - Windows, Linux, ...
Kao što je pomenuto u odeljku [3.2. Qt Framework](#232-qt-framework), glavna prednost je u tome da jedan razvojni proces može da se jednostavno prebaci u paket za bilo koju platformu. Budući da sam softver za krajnjeg korisnika razvijao na Windows desktopu (u drugom mesecu), najjednostavnije mi je bilo da ga za tu platformu i razvijem. Veoma prosto bi se prebacio i na Linux (na kojem sam razvijao u prvom mesecu), macOS, Android i iOS. Jedino je za mobilne platforme potrebno malo pažnje za dizajn, povodom ograničenijeg prostora na ekranu.


### 3.6.2. Software - Cross-platform GUI Data Visualizer
#### 3.6.2.1. MainWindow klasa

Glavna klasa u kojoj je smeštena većina logike je `MainWindow`. Ova klasa upravlja svim elementima korisničkog interfejsa 
i komunikacijom sa IoT platformom.

```cpp
class MainWindow : public QMainWindow {
    Q_OBJECT
public:
    explicit MainWindow(QWidget *parent = nullptr);
    ...
private slots:
    void on_pushButton_clicked();
    ...
};
```
"""

test_html = """
<ul style="font-size:10px">
<li style="font-size:14px">
<ul>
<li><a href="#1-uvod">1. Uvod</a></li>
</ul>
</li>
<li style="font-size:14px">
<ul>
<li><a href="#2-teorijski-okvir">2. Teorijski okvir</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#21-osnovni-termini-i-oblast-u-kojoj-se-praksa-radi">2.1.
Osnovni termini i oblast u kojoj se praksa radi</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#211-embedded-programiranje">2.1.1. Embedded
programiranje</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#212-internet-of-things">2.1.2. Internet of Things</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#213-cloud-computing---računarstvo-u-oblaku">2.1.3. Cloud
computing - računarstvo u oblaku</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#22-organizacija-rada-i-tok-prakse">2.2. Organizacija rada
i tok prakse</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#221-onboarding-">2.2.1. Onboarding //</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#222-struktura-ljudi">2.2.2. Struktura ljudi</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#223-sastanci---tehnički-deo">2.2.3. Sastanci - tehnički
deo</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#224-sastanci---netehnički-deo">2.2.4. Sastanci -
netehnički deo</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#225-finalna-prezentacija">2.2.5. Finalna
prezentacija</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#23-ključni-korišćeni-alati">2.3. Ključni korišćeni
alati</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#231-arduino-ekosistem">2.3.1. Arduino ekosistem</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#232-qt-framework">2.3.2. Qt Framework</a></li>
</ul>
</li>
<li style="font-size:14px">
<ul>
<li><a href="#3-sadržaj-projekta">3. Sadržaj projekta</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#31-šira-slika-projekta">3.1. Šira slika projekta</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#311-primer-primene-davanje-konteksta-use-case">3.1.1.
Primer primene, davanje konteksta (<em>use case</em>)</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a
href="#312-primena-1---spoljno-praćenje-vremenskih-prilika-prognoza">3.1.2.
Primena 1 - spoljno praćenje vremenskih prilika, prognoza</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a
href="#313-primena-2---unutrašnje-praćenje-i-regulacija-osetljivih-procesa">3.1.3.
Primena 2 - unutrašnje praćenje i regulacija osetljivih procesa</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#32-struktura-projekta">3.2. Struktura projekta</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#321-hardware">3.2.1. Hardware</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#322-sofware">3.2.2. Sofware</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#33-arduino---prvi-korak-detekcija">3.3. Arduino - prvi
korak, detekcija</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#331-hardware---arduino-uno">3.3.1. Hardware - Arduino
Uno</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#332-hardware---shields-i-clicks">3.3.2. Hardware - Shields
i clicks</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#333-software---arduino-firmware">3.3.3. Software - Arduino
firmware</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#34-raspberry-pi---posrednik">3.4. Raspberry Pi -
posrednik</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#341-hardware---raspberry-pi">3.4.1. Hardware - Raspberry
Pi</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#342-software---raspberry-pi-cloud-client">3.4.2. Software
- Raspberry Pi Cloud Client</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#35-wolkabout-cloud-platforma---centrala-informacija">3.5.
WolkAbout Cloud Platforma - centrala informacija</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#351-hardware-cloud-platforme">3.5.1. “Hardware” Cloud
platforme?</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a
href="#352-software---konfigurisanje-povezivanje-monitoring">3.5.2.
Software - konfigurisanje, povezivanje, monitoring</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#36-krajnji-korisnik">3.6. Krajnji korisnik</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a href="#361-hardware---windows-linux-">3.6.1. Hardware - Windows,
Linux, …</a></li>
</ul>
</li>
<li style="font-size:10px">
<ul>
<li><a
href="#362-software---cross-platform-gui-data-visualizer-todo">3.6.2.
Software - Cross-platform GUI Data Visualizer //TODO</a></li>
</ul>
</li>
<li style="font-size:14px">
<ul>
<li><a href="#4-zaključak">4. Zaključak</a></li>
</ul>
</li>
<li style="font-size:14px">
<ul>
<li><a href="#5-literatura">5. Literatura</a></li>
</ul>
</li>
</ul>
<hr />
<div style="page-break-before: always;">

</div>
<h1 id="i-uvod">I Uvod</h1>
<p>Praksu sam obavio u kompaniji <a
href="execom.eu"><strong>Execom</strong></a>, koju je u međuvremenu
kupio <a href=""><strong>HTEC</strong></a>. U pitanju je
<em>outsourcing</em> kompanija koja ima niz timova, svaki od kojih radi
na uglavnom jednom projektu za eksternog klijenta. Timovi se bave
različitim tehnologijama, u zavisnosti od potreba klijenta.</p>
<p>Kao i svaka <em>outsourcing</em> kompanija, nema svoje interne
projekte, već ih isključivo uslužno pravi za druge. Važno je napomenuti
da je njihov nekadašnji interni projekat prerastao u tzv. <em>spin
"""