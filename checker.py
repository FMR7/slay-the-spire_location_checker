import json
        
col_size = 30

def checkCards():
  inconsistencies_counter = 0
  location_inconsistencies = []
  with open('cards.json', 'r') as f:
    cards = json.load(f)
    for card in cards:
        name = cards[card].get('NAME')
        powerName = getPowerName(card)
        if(name is not None and powerName is not None and name != powerName):
          inconsistencies_counter += 1
          data = (f"{card:<{col_size}} | {name:<{col_size}} | {powerName:<{col_size}}")
          location_inconsistencies.append(data)
    
    print(f'INCONSISTENCIES FOUND IN NAMING: {inconsistencies_counter}')
    print()
    if(inconsistencies_counter > 0):
        print(f"{'ID':<{col_size}}   {'Card Name':<{col_size}}   {'Power Name':<{col_size}}")
        for inconsistency in location_inconsistencies:
            print(inconsistency)
    
def getPowerName(powerId):
  with open('powers.json', 'r') as f:
    powers = json.load(f)
    for power in powers:
      if(power == powerId):
        return powers[power]['NAME']
    

print('CHECKING LOCATION CONSISTENCY...')
checkCards()    