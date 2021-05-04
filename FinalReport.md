# Loppuraportti

## Sprinttien aikaiset ongelmat
**Ensimmäisen sprintin** aikana vastuunjako taskien suhteen oli epäselvää, ja taskeja tehtiin jonkin verran muille ilmoittamatta yksilötyönä. 
Lisäksi taskeihin liittyvä ajankäytön estimointi oli karkealla tasolla.

**Toisen sprintin** aikana erääksi ongelmaksi muodostui user storyjen väliset riippuvuudet: eräiden taskien tekemisien kanssa ei voinut edetä ennen kuin toinen 
saatiin valmiiksi. Tästä johtuen osa taskeista valmistui viime tingassa juuri ennen palautusajankohtaa. Lisäksi toisen sprintin aikana havaittiin, että sprintiin 
liittyvä työkuorma ei välttämättä jakaudu täysin tasaisesti eri jäsenten kesken. Myös kokouksien pitkä kesto tunnistettiin ongelmaksi.

## Hyvin sujuneet asiat
Pull requestit ja feature-haarat todettiin hyväksi käytännöksi, ja näiden käyttämistä jatkettiin laajemmin kolmannessa sprintissä.

Sovituista tapaamisista pidettiin kiinni ja niissä saatiin käytyä tarvittava määrä asioita läpi. Lisäksi ne alkoivat parin ensimmäisen viikon jälkeen edetä hieman 
sujuvammin.

Yleisesti ottaen ryhmätyöskentely ja -ohjelmointi sujui hyvin ja suurilta ja työskentelyn pysäyttäviltä ongelmilta vältyttiin. 

## Parantamiskohteet
Toisen sprintin retrospektiivissä kehittämiskohteeksi määriteltiin user storyihin tai taskeihin liittyvien pullonkaulojen tunnistaminen ja niiden priorisointi
toteutusjärjestyksessä, jotta ne eivät haittaa muiden taskien etenemistä. Kolmannessa sprintissä ongelma ei enää esiintynyt, mikä toisaalta johtui siitä, ettei 
sellaista teknisesti olisi voinutkaan syntyä.

Kokoukset etenivät toisen spritin jälkeen hieman sujuvammin ja nopeammin, mutta etenemisessä olisi voinut olla vielä hieman parantamisen varaa. Tähän olisi voinut 
auttaa se, että joku ryhmän jäsenistä olisi ottanut vetovastuun ja ohjannut kokousta.

Ohjemointiin liittyvä työkuorma ei välttämättä aina jakaantunut tasaisesti projektin eri jäsenten kesken. Tähän olisi voinut auttaa tarkempi taskeihin liittyvä ajan 
käytön estimointi ja toisaalta mahdollinen taskien uudelleendelegointi sen jälkeen kun tekijä on käyttänyt viikkottaisen tuntityömäärän.

## Mitä asioita opimme, halusimme oppia ja mikä tuntui turhalta
**Sakari**: Opin eniten gitin käytöstä, kuten mergeistä, feature-haaroista ja pull requesteista. Toiseksi eniten opin ohjelmistotuotantoon liittyvästä 
ryhmätyöskentelystä ja siihen liittyvistä haasteista. Kurssin kontekstissa nämä asiat tuntuivat riittäviltä oppimiseen nähden, joten toiveita opittavista asioista 
ei tullut. Turhilta tuntuvia asioita ei juurikaan ollut, vaikka jotkin sovellukseen toteutetut tai ehdotetut yksityiskohdat olivat ehkä liian hienoksi hiottuja ottaen 
työn tarkoitus ja laajuus huomioon.

**Meri**: Opin product backlogin tekemisestä, retrospektiiveistä ja muista Scrumin käytänteistä, jotka eivät olleet entuudestaan tuttuja. Eniten halusin oppia dokumentaatiosta ja tiimityöskentelystä lisää, ja opinkin jonkin verran, mutta näin lyhyessä projektissa pääpaino ei ollut siinä, kun kuitenkin teknistä toteutettavaa oli paljon. Siihen liittyen luin paljon ORMia käyttävistä tietokannoista, koska vain suorat SQL-kyselyt olivat ennestään tuttuja. Windowsin aiheuttamat tekniset haasteet taas opettivat jälleen lisää ongelmanratkaisua. Turhalta tuntui ehkä käyttää palavereihin niin paljon aikaa, mutta tämä ongelma korjattiin.

**Roope**: Scrumiin ja prosessiin muutenkin liittyen oli paljon opittavaa. "Extremly difficult to master" -lausahduksen merkitys tuli konkreettisesti selväksi.
Teknisellä tasolla oli mielenkiintoista yhdistellä aiemmin opittua, esimerkiksi testausta, ORMia ja kerrosarkkitehtuuria. Näiden yhdistelmä osoittautui hankalaksi, koska ORM käytännössä vaatii tietokantayhteyden toimiakseen ja toistaalta stubien kirjoittaminen modeleille olisi hankalaa. Huomasin, että ORM sotii melko paljon kerrosarkkitehtuurin periaatteita vastaan, kun olioille määritellään tietokantakerroksen toiminnallisuuksia - tämähän on melko yleinen kritiikki ORMia kohtaan.
Sanoisin samaa siitä, että palaverit venyivät turhan pitkiksi, johtuen esim. taskien jaon epävarmuudesta.

**Touko**: Eniten opin ohjelmoimisesta ryhmän kanssa sekä Scrumista. Tehtävien/Taskien jako, koodin katselmointi,feature branchit, Scrumin omat käytänteet yms. olivat kaikki uutta minulle. Jonkin verran opin myös teknisen tason asioista kuten Flask-kirjastosta ja ORMin käyttämisestä. Eniten halusinkin oppia minkälaista ohjelmoiminen ryhmässä Scrumia noudattaen on ja tämä projekti antoi hyvän pienoiskuvan siitä. En nyt oikein keksi hirveästi turhilta tuntuvia asioita, mutta komppaan tässä nyt muita että palaverit olivat turhin pitkiä, joita onneksi saitiin lyhennettyä projektin aikana.

