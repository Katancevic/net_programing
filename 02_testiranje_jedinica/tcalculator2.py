# u posebnom folderu gde je projekat kreira se novi folder i unutar njega fajl u kome se pisu testovi
# importujem klasu calculator
from Calculator import Calculator
# pravim funkciju gde instanciram calsu calculator i sispisjem njen rezultat
def test_Calculator():
    calc = Calculator()
    print(calc.sum_from_number(7,3))

# Sledeci korak je da naposem proveru rezultata. Ynam da mi je rezultat 10 pa to i proveravam

def test_sum_from_numbers():
    calc = Calculator()
    result = calc.sum_form_number(7, 3)
    if result == 10:
        print("Test passed!")
    else:
        print("Test failed!")

test_sum_from_numbers()