import pycountry


input_countries = ['American Samoa', 'Canada', 'France']

countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha3

codes = [countries.get(country, 'Unknown code') for country in input_countries]

print codes  # prints [u'AS', u'CA', u'FR']