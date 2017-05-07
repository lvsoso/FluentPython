# -*- coding: utf-8 -*-
"""
Created on Sun May 07 14:01:20 2017

"""

"""

from collections import namedtuple

ll = namedtuple('ll',['x', 'y'])

ll
Out[50]: __main__.ll

ll._fields
Out[51]: ('x', 'y')

City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

LatLong = namedtuple('LatLong', 'lat long')

delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

tokyo._asdict
Out[56]: <bound method City._asdict of City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))>

tokyo._asdict()
Out[57]: 
OrderedDict([('name', 'Tokyo'),
             ('country', 'JP'),
             ('population', 36.933),
             ('coordinates', (35.689722, 139.691667))])

delhi = City._make(delhi_data)

delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

delhi = City._make(delhi_data)

delhi._asdict()
Out[61]: 
OrderedDict([('name', 'Delhi NCR'),
             ('country', 'IN'),
             ('population', 21.935),
             ('coordinates', LatLong(lat=28.613889, long=77.208889))])

"""

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # <2>
    if longitude <= 0:  # <3>
        print(fmt.format(name, latitude, longitude))