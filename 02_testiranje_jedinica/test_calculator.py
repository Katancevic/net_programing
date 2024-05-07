from Calculator import Calculator

class Testcalculator:

    def test_is_corect(self):
        calc = Calculator()
        result = calc.sum_form_number(7, 3)
        expected = 10
        assert result == expected

    def test_is_negative(self):
        calc = Calculator()
        result = calc.sum_form_number(-5, 2)
        expected = 0
        assert result < expected

    def test_is_greater(self):
        calc = Calculator()
        result = calc.sum_form_number(7, 3)
        expeced = 10
        assert result >= expeced