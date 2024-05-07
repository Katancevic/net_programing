# Testiranje jedinica(unit test) rucno

def sum_from_numbers(a,b):
    return a + b
# definisem promenljive i ocekivani rezultat
first_number = 7
second_number = 3
expected_result = 10

# pozivam funkciju i prosledjujem joj vrednosti promenljive

result = sum_from_numbers(first_number,second_number)

# pisem test jednostavnim if uslovom

if result == expected_result:
    print("Test passed!")
else:
    print("Test failed!")

""" Zadatak: Napraviti funkciju prvo_slovo koja kao argument prima string i vraca prvi karakter datog stringa. 
Proverite da li je povrtna vrednsot funkcije jednaka vrednosti promenljive expected_result koja se unosi preko input funkcije. 
Ako jeste ispisati "slova su ista!" ukoliko nije ispisati "Slova nisu ista!"
"""
def prvo_slovo(a):
    return a[0]

string = "Ivan"
expected_result2 = input("Unesi ocekivani razultat prvog karaktera: ").upper()

result2 = prvo_slovo(string)

if result2 == expected_result2:
    print("Slova su ista")
else:
    print("Slova nisu ista")

# Unit test 


