from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import time

class Person:
	def __init__(self):
		name = ""
		party = ""
		voted = ""

filename = "votings.csv"
f = open(filename, "a", encoding="utf-8")
# file to write int
politicians = ['Ivan Adamec', 'Věra Adámková', 'Hana Aulická Jírovcová', 'Andrej Babiš', 'Andrea Babišová',
'Ondřej Babka', 'Margita Balaštíková', 'Dana Balcarová', 'Lukáš Bartoň', 'Ivan Bartoš', 'Jan Bartošek',
'Jan Bauer', 'Martin Baxa', 'Jiří Běhounek', 'Petr Beitl', 'Josef Bělica', 'Pavel Bělobrádek',
'Marek Benda', 'Petr Bendl', 'Ondřej Benešík', 'Stanislav Berkovec', 'Jan Birke', 'Stanislav Blaha',
'Jiří Bláha', 'Pavel Blažek', 'Irena Blažková', 'Marian Bojko', 'Richard Brabec', 'Milan Brázdil',
'Andrea Brzobohatá', 'Jaroslav Bžoch', 'Lukáš Černohorský', 'Jana Černochová', 'Alexander Černý',
'Monika Červíčková', 'Jan Čižinský', 'Jiří Dolejš', 'Petr Dolínek', 'Klára Dostálová', 'Lenka Dražilová',
'Jaroslav Dvořák', 'František Elfmark', 'Jaroslav Faltýnek', 'Kamal Farhan', 'Jan Farský', 'Milan Feranec',
'Dominik Feri', 'Mikuláš Ferjenčík', 'Petr Fiala', 'Radim Fiala', 'Eva Fialová', 'Vojtěch Filip',
'Jaroslav Foldyna', 'Stanislav Fridrich', 'Alena Gajdůšková', 'Petr Gazdík', 'Pavla Golasowská',
'Miroslav Grebeníček', 'Stanislav Grospič', 'Josef Hájek', 'Jan Hamáček', 'Tomáš Hanzel', 'Jiří Hlavatý',
'Milan Hnilička', 'Jaroslav Holík', 'Radek Holomčík', 'Jan Hrnčíř', 'Tereza Hyťhová', 'Milan Chovanec',
'Jan Chvojka', 'Ivan Jáč', 'Jakub Janda', 'Miloslav Janulík', 'Monika Jarošová', 'Pavel Jelínek',
'Martin Jiránek', 'Aleš Juchelka', 'Stanislav Juránek', 'Marian Jurečka',
'Pavel Juříček', 'Iva Kalátová', 'Adam Kalous', 'Miroslav Kalousek', 'Vít Kaňkovský', 'David Kasal',
'Václav Klaus', 'Jiří Kobza', 'Jiří Kohoutek', 'Tomáš Kohoutek', 'Lukáš Kolářík', 'Martin Kolovratník',
'Květa Matušovská', 'Vladimír Koníček', 'František Kopřiva', 'Barbora Kořanová', 'Radek Koten',
'Josef Kott', 'Pavel Kováčik', 'Věra Kovářová', 'Lenka Kozlová', 'Robert Králíček', 'Karel Krejza',
'Jana Krutáková', 'Roman Kubíček', 'Jan Kubík', 'Martin Kupka', 'Jaroslav Kytýr', 'Helena Langšádlová',
'Jana Levová', 'Jan Lipavský', 'Leo Luzar', 'Zuzana Majerová Zahradníková', 'Taťána Malá', 'Přemysl Mališ',
'Tomáš Martínek', 'Jaroslav Martinů', 'Karla Maříková', 'Jiří Mašek', 'Eva Matyášová',
'Ilona Mauritzová', 'Radka Maxová', 'Marcela Melková', 'Jiří Mihola', 'Jakub Michálek', 'Jana Mračková Vildumetzová',
'Vojtěch Munzar', 'Patrik Nacher', 'František Navrkal', 'Miroslava Němcová', 'Ivana Nevludová',
'Marek Novák', 'Monika Oborná', 'Tomio Okamura', 'Ladislav Okleštěk', 'Roman Onderka', 'Zdeněk Ondráček',
'Zuzana Ožanová', 'Jana Pastuchová', 'Petr Pávek', 'Daniel Pawlas', 'Markéta Pekarová Adamová',
'Mikuláš Peksa', 'Robert Pelikán', 'Marie Pěnčíková', 'František Petrtýl', 'Vojtěch Pikal', 'Pavel Plzák',
'Zdeněk Podal', 'Ivo Pojezný', 'Jaroslava Pokorná Jermanová', 'Ondřej Polanský', 'Jan Pošvář',
'Milan Pour', 'David Pražák', 'Ondřej Profant', 'Věra Procházková', 'Pavel Pustějovský', 'Martin Půta',
'Karel Rais', 'Vít Rakušan', 'Michal Ratiborský', 'Jan Richter', 'Olga Richterová', 'Miloslav Rozner',
'Radek Rozvoral', 'Miloslava Rutová', 'Pavel Růžička', 'Jan Řehounek', 'Petr Sadovský', 'Jan Schiller',
'Karel Schwarzenberg', 'Roman Sklenák', 'Jan Skopeček', 'Bohuslav Sobotka', 'Antonín Staněk', 'Pavel Staněk',
'Zbyněk Stanjura', 'Martin Stropnický', 'Jiří Strýček', 'Bohuslav Svoboda', 'Lucie Šafránková',
'Karla Šlechtová', 'Lubomír Španěl', 'Julius Špičák', 'David Štolpa', 'Dan Ťok', 'Petr Třešňák', 'Karel Tureček',
'František Vácha', 'Kateřina Valachová', 'Vlastimil Válek', 'Jiří Valenta', 'Helena Válková',
'Petr Venhoda', 'Jiří Ventruba', 'Ondřej Veselý', 'Radovan Vích',
'Adam Vojtěch', 'Jan Volný', 'Lubomír Volný', 'Radek Vondráček', 'Ivo Vondrák', 'Miloslava Vostrá',
'Václav Votava', 'Petr Vrána', 'Veronika Vrecionová', 'Marek Výborný', 'Tomáš Vymazal', 'Rostislav Vyzula',
'Jan Zahradník', 'Lubomír Zaorálek', 'Radek Zlesák', 'Pavel Žáček']

politicians_parties = ['Ivan Adamec party', 'Věra Adámková party', 'Hana Aulická Jírovcová party', 'Andrej Babiš party', 'Andrea Babišová party',
'Ondřej Babka party', 'Margita Balaštíková party', 'Dana Balcarová party', 'Lukáš Bartoň party', 'Ivan Bartoš party', 'Jan Bartošek party',
'Jan Bauer party', 'Martin Baxa party', 'Jiří Běhounek party', 'Petr Beitl party', 'Josef Bělica party', 'Pavel Bělobrádek party',
'Marek Benda party', 'Petr Bendl party', 'Ondřej Benešík party', 'Stanislav Berkovec party', 'Jan Birke party', 'Stanislav Blaha party',
'Jiří Bláha party', 'Pavel Blažek party', 'Irena Blažková party', 'Marian Bojko party', 'Richard Brabec party', 'Milan Brázdil party',
'Andrea Brzobohatá party', 'Jaroslav Bžoch party', 'Lukáš Černohorský party', 'Jana Černochová party', 'Alexander Černý party',
'Monika Červíčková party', 'Jan Čižinský party', 'Jiří Dolejš party', 'Petr Dolínek party', 'Klára Dostálová party', 'Lenka Dražilová party',
'Jaroslav Dvořák party', 'František Elfmark party', 'Jaroslav Faltýnek party', 'Kamal Farhan party', 'Jan Farský party', 'Milan Feranec party',
'Dominik Feri party', 'Mikuláš Ferjenčík party', 'Petr Fiala party', 'Radim Fiala party', 'Eva Fialová party', 'Vojtěch Filip party',
'Jaroslav Foldyna party', 'Stanislav Fridrich party', 'Alena Gajdůšková party', 'Petr Gazdík party', 'Pavla Golasowská party',
'Miroslav Grebeníček party', 'Stanislav Grospič party', 'Josef Hájek party', 'Jan Hamáček party', 'Tomáš Hanzel party', 'Jiří Hlavatý party',
'Milan Hnilička party', 'Jaroslav Holík party', 'Radek Holomčík party', 'Jan Hrnčíř party', 'Tereza Hyťhová party', 'Milan Chovanec party',
'Jan Chvojka party', 'Ivan Jáč party', 'Jakub Janda party', 'Miloslav Janulík party', 'Monika Jarošová party', 'Pavel Jelínek party',
'Martin Jiránek party', 'Aleš Juchelka party', 'Stanislav Juránek party', 'Marian Jurečka party',
'Pavel Juříček party', 'Iva Kalátová party', 'Adam Kalous party', 'Miroslav Kalousek party', 'Vít Kaňkovský party', 'David Kasal party',
'Václav Klaus party', 'Jiří Kobza party', 'Jiří Kohoutek party', 'Tomáš Kohoutek party', 'Lukáš Kolářík party', 'Martin Kolovratník party',
'Květa Matušovská party', 'Vladimír Koníček party', 'František Kopřiva party', 'Barbora Kořanová party', 'Radek Koten party',
'Josef Kott party', 'Pavel Kováčik party', 'Věra Kovářová party', 'Lenka Kozlová party', 'Robert Králíček party', 'Karel Krejza party',
'Jana Krutáková party', 'Roman Kubíček party', 'Jan Kubík party', 'Martin Kupka party', 'Jaroslav Kytýr party', 'Helena Langšádlová party',
'Jana Levová party', 'Jan Lipavský party', 'Leo Luzar party', 'Zuzana Majerová Zahradníková party', 'Taťána Malá party', 'Přemysl Mališ party',
'Tomáš Martínek party', 'Jaroslav Martinů party', 'Karla Maříková party', 'Jiří Mašek party', 'Eva Matyášová party',
'Ilona Mauritzová party', 'Radka Maxová party', 'Marcela Melková party', 'Jiří Mihola party', 'Jakub Michálek party', 'Jana Mračková Vildumetzová party',
'Vojtěch Munzar party', 'Patrik Nacher party', 'František Navrkal party', 'Miroslava Němcová party', 'Ivana Nevludová party',
'Marek Novák party', 'Monika Oborná party', 'Tomio Okamura party', 'Ladislav Okleštěk party', 'Roman Onderka party', 'Zdeněk Ondráček party',
'Zuzana Ožanová party', 'Jana Pastuchová party', 'Petr Pávek party', 'Daniel Pawlas party', 'Markéta Pekarová Adamová party',
'Mikuláš Peksa party', 'Robert Pelikán party', 'Marie Pěnčíková party', 'František Petrtýl party', 'Vojtěch Pikal party', 'Pavel Plzák party',
'Zdeněk Podal party', 'Ivo Pojezný party', 'Jaroslava Pokorná Jermanová party', 'Ondřej Polanský party', 'Jan Pošvář party',
'Milan Pour party', 'David Pražák party', 'Ondřej Profant party', 'Věra Procházková party', 'Pavel Pustějovský party', 'Martin Půta party',
'Karel Rais party', 'Vít Rakušan party', 'Michal Ratiborský party', 'Jan Richter party', 'Olga Richterová party', 'Miloslav Rozner party',
'Radek Rozvoral party', 'Miloslava Rutová party', 'Pavel Růžička party', 'Jan Řehounek party', 'Petr Sadovský party', 'Jan Schiller party',
'Karel Schwarzenberg party', 'Roman Sklenák party', 'Jan Skopeček party', 'Bohuslav Sobotka party', 'Antonín Staněk party', 'Pavel Staněk party',
'Zbyněk Stanjura party', 'Martin Stropnický party', 'Jiří Strýček party', 'Bohuslav Svoboda party', 'Lucie Šafránková party',
'Karla Šlechtová party', 'Lubomír Španěl party', 'Julius Špičák party', 'David Štolpa party', 'Dan Ťok party', 'Petr Třešňák party', 'Karel Tureček party',
'František Vácha party', 'Kateřina Valachová party', 'Vlastimil Válek party', 'Jiří Valenta party', 'Helena Válková party',
'Petr Venhoda party', 'Jiří Ventruba party', 'Ondřej Veselý party', 'Radovan Vích party',
'Adam Vojtěch party', 'Jan Volný party', 'Lubomír Volný party', 'Radek Vondráček party', 'Ivo Vondrák party', 'Miloslava Vostrá party',
'Václav Votava party', 'Petr Vrána party', 'Veronika Vrecionová party', 'Marek Výborný party', 'Tomáš Vymazal party', 'Rostislav Vyzula party',
'Jan Zahradník party', 'Lubomír Zaorálek party', 'Radek Zlesák party', 'Pavel Žáček party']

politicians.sort()
politicians_parties.sort()
headers = ['Voting']
headers.append(politicians)
#f.write('Voting'+ ';' + ';'.join(politicians) + ';' + ';'.join(politicians_parties) + '\n')

# get html from url
for i in range(71294, 73901):
	time.sleep(1)
	my_url = "https://www.psp.cz/sqw/hlasy.sqw?g=" + str(i) + "&l=cz"
	client = urlopen(my_url)
	raw_html = client.read()
	client.close()

	# parse downloaded html
	page_soup = soup(raw_html.decode('windows-1250').encode('utf-8'), "html.parser")
	container = page_soup.findAll("ul", {"class":"results"})
	votings = page_soup.findAll("h1", {"class":"page-title-x"})
	if len(votings) != 0:
		voting_name = votings[0].text
		print(voting_name)
		parties = ['ANO', 'ODS', 'Piráti', 'SPD', 'ČSSD', 'KSČM', 'KDU-ČSL', 'TOP09', 'STAN', 'Nezařaz']
		people = []

		party_index = 0
		for one_list in container: # one list = one party, not name sorted yet
			list_items = one_list.findAll('li')
			for item in list_items:
				current_politician = Person()
				name = item.a
				name_text = name.text
				current_politician.name = name.text
				result = item.span
				result_text = result.text
				current_politician.voted = result.text
				current_politician.party = parties[party_index]
				people.append(current_politician)
			party_index += 1

		sorted_people = sorted(people, key=lambda Person: Person.name)
		result_list = []

		for politician in politicians: # 1. pro hlasy, potom loop pro prislusnosti
			if any(x.name == politician for x in sorted_people):
				i = 0
				while i < len(sorted_people):
					if politician == sorted_people[i].name:
						result_list.append(sorted_people[i].voted)
						break
					else:
						i+= 1
			else:
				result_list.append("-")

		for politician in politicians: # 2. loop pro politicke strany
			if any(x.name == politician for x in sorted_people):
				i = 0
				while i < len(sorted_people):
					if politician == sorted_people[i].name:
						result_list.append(sorted_people[i].party)
						break
					else:
						i+= 1
			else:
				result_list.append("-")

		f.write(voting_name + ';' + ';'.join(result_list) + '\n') # vsechny vysledky do jednoho string listu a pak jako u headers, ale append

f.close()
