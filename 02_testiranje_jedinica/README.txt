Testiranje jedinice (Unit testovi)

* Testtiranje jedinice obuhvata proveru najmanjih celina koda koje se mogu testirati, nazvanih jedinica ili unita. Jednom napisan unit test koristimo d au fazmam daljeg razvoja mozemo prekontrolisati da li jedinica i dalje pravilno radi.

* Testiranje jedinice je white box oriented tehnika testiranja, gde imamo uvid u kod i pravimo direktne promene u samoj strukturi programa.

* Pod jedinicom mozemo posmatrati modul, klasu, metodu, objekat ili funkciju.


* Python je jedan od jezika koji imaju odlicnu podrsku za tesstiranje. Ovaj jezik u oviru svojih standardnih biblioteka sadrzi i pkaet za tesiranje jedinica(unit testing). Takodje, za Python postoji eksterna biblioteka/framework za razvoj testova pod nazivom pytest.

* biblioteka za testiranje jedinica integrisana u Python nosi naziv unittest i predstavlja okruzenje za razvoj testova.

* Test Fixture predstvalja pripremu testnog okruzenja tako da se test moze izvesti bez uticaja testa na ostatak koda ili suprotno, tako da neki drugi kod ne utice na rezultate testa. Dobro organizivan fixture testa omogucava lak prelaz sa testiranja koda na njegovu upotrebu.

* Test case je slucaj ili jedinica testiranja. Test slucaj unutar unit testa predstavljapazvljivo isplanirane pretpostavke o ishodu rada programa.

* Test suite predstavlja kolekciju test slucajeva. Sluzi nam da smestimo testove vezane za jednu jedinicu i omogucava da ih pokrenemo sve u isto vreme.

* Test runner predstavlja aplikaciju koja pokrece/startuje test. Runner aplikacija moze imati graficki korisnicki interfejs, ali i konzolni/termalni interfejs.