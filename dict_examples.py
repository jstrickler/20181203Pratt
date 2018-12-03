#!/usr/bin/env python

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

print(airports['OAK'])
print(airports.get('BDL')) # default NONE
print(airports.get('BDL', 'NOT FOUND'))
print(airports, '\n')
print(airports.setdefault('BDL', 'Hartford'))

print(airports, '\n')

more_airports = {'JFK': 'NY-Kennedy', 'ELM': 'Elmyra',
    'IND': 'Indianapolis', 'IAD': 'Washington-Dulles'}

airports.update(more_airports)

print(airports, '\n')

for abbr, airport in sorted(airports.items()):
    print(abbr, airport)
print()
