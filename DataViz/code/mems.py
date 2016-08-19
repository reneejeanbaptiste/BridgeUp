import pycountry


input_countries = [
'Afghanistan',
'Albania',
'Algeria',
'Angola',
'Antigua and Barbuda',
'Argentina',
'Armenia',
'Australia',
'Austria',
'Azerbaijan',
'Bahamas',
'Bahrain',
'Bangladesh',
'Barbados',
'Belarus',
'Belgium'
'Belize',
'Benin',
'Bhutan',
'Bolivia (Plurinational State of)',
'Bosnia and Herzegovina',
'Botswana',
'Brazil',
'Brunei Darussalam',
'Bulgaria',
'Burkina Faso',
'Burundi',
'Cote d Ivoire',
'Cabo Verde',
'Cambodia',
'Cameroon',
'Canada',
'Central African Republic',
'Chad',
'Chile',
'China',
'Colombia',
'Comoros',
'Congo',
'Costa Rica',
'Croatia',
'Cuba',
'Cyprus',
'Czech Republic',
'Democratic Peoples Republic of Korea',
'Democratic Republic of the Congo',
'Denmark',
'Djibouti',
'Dominican Republic',
'Ecuador',
'Egypt',
'El Salvador',
'Equatorial Guinea',
'Eritrea',
'Estonia',
'Ethiopia',
'Fiji',
'Finland',
'France',
'Gabon',
'Gambia',
'Georgia',
'Germany',
'Ghana',
'Greece',
'Grenada',
'Guatemala',
'Guinea',
'Guinea-Bissau',
'Guyana',
'Haiti',
'Honduras',
'Hungary',
'Iceland',
'India',
'Indonesia',
'Iran (Islamic Republic of)',
'Iraq',
'Ireland',
'Israel',
'Italy',
'Jamaica',
'Japan',
'Jordan',
'Kazakhstan',
'Kenya',
'Kiribati',
'Kuwait',
'Kyrgyzstan',
'Lao Peoples Democratic Republic',
'Latvia',
'Lebanon',
'Lesotho',
'Liberia',
'Libya',
'Lithuania',
'Luxembourg',
'Madagascar',
'Malawi',
'Malaysia',
'Maldives',
'Mali',
'Malta',
'Mauritania',
'Mauritius',
'Mexico',
'Micronesia (Federated States of)',
'Mongolia',
'Montenegro',
'Morocco',
'Mozambique',
'Myanmar',
'Namibia',
'Nepal',
'Netherlands',
'New Zealand',
'Nicaragua',
'Niger',
'Nigeria',
'Norway',
'Oman',
'Pakistan',
'Panama',
'Papua New Guinea',
'Paraguay',
'Peru',
'Philippines',
'Poland',
'Portugal',
'Qatar',
'Republic of Korea',
'Republic of Moldova',
'Romania',
'Russian Federation',
'Rwanda',
'Saint Lucia',
'Saint Vincent and the Grenadines',
'Samoa',
'Sao Tome and Principe',
'Saudi Arabia',
'Senegal',
'Serbia',
'Seychelles',
'Sierra Leone',
'Singapore',
'Slovakia',
'Slovenia',
'Solomon Islands',
'Somalia',
'South Africa',
'South Sudan',
'Spain',
'Sri Lanka',
'Sudan',
'Suriname',
'Swaziland',
'Sweden',
'Switzerland',
'Syrian Arab Republic',
'Tajikistan',
'Thailand',
'The former Yugoslav republic of Macedonia',
'Timor-Leste',
'Togo',
'Tonga',
'Trinidad and Tobago',
'Tunisia',
'Turkey',
'Turkmenistan',
'Uganda',
'Ukraine',
'United Arab Emirates',
'United Kingdom of Great Britain and Northern Ireland',
'United Republic of Tanzania',
'United States of America',
'Uruguay',
'Uzbekistan',
'Venezuela',
'Viet Nam',
'Yemen',
'Zambia',
'Zimbabwe']

countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha3

codes = [countries.get(country, 'Unknown code') for country in input_countries]

print codes