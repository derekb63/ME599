#!/usr/bin/env python


from urllib2 import urlopen


def update_currency_rates():
    url = urlopen('https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html')
    html = url.read()

    eur_rates = {}
    for i,line in enumerate(html.split('<td id="')[1:]):
        try:
            currency = line[:3]
            rate = float(line.split('class="rate">')[1].split('<')[0])
            eur_rates[currency] = rate
        except:
            pass
        
    # Translate to USD rates, and store in a global variable called
    # _rates
    global _rates
    _rates = {}
    for c,r in eur_rates.iteritems():
        _rates[c] = eur_rates[c] / eur_rates['USD']


class Cash:
    def __init__(self, dollars=0, cents=0):
        self.cents = int(round(dollars * 100 + cents))
        global _rates
        self.rates = _rates

    def __str__(self):
        if self.cents < 0:
            return '-${0:.2f}'.format(abs(self.cents / 100.0))
        else:
            return '${0:.2f}'.format(self.cents / 100.0)

    # Arithmetic operations    
    def __add__(self, other):
        try:
            return Cash(0, self.cents + other.cents)
        except:
            return self + Cash(other)

    def __radd__(self, other):
        return self + other
        
    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return Cash(0, -self.cents)

    def __mul__(self, other):
        return Cash(0, self.cents * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    # Divide by cash, return float.  Divde by a number, return Cash
    def __div__(self, other):
        try:
            return float(self.cents) / float(other.cents)
        except:
            return Cash(0, self.cents / other)

    # Comparison operators
    def __lt__(self, other):
        try:
            return self.cents < other.cents
        except:
            return self < Cash(other)

    def __gt__(self, other):
        try:
            return self.cents > other.cents
        except:
            return self > Cash(other)

    def __eq__(self, other):
        return not self < other and not self > other

    def __ne__(self, other):
        return self < other or self > other

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other

    def convert(self, currency):
        try:
            return self.rates[currency] * self.cents / 100.0
        except:
            return None
    

update_currency_rates()


if __name__ == '__main__':
    a = Cash(1.00)

    print a.convert('GBP')
    print a.rates
