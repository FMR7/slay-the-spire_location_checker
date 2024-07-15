import json
        
def checkCards():
  with open('cards.json', 'r') as f:
    cards = json.load(f)
    for card in cards:
        name = cards[card].get('NAME')
        powerName = getPowerName(card)
        if(name is not None and powerName is not None and name != powerName):
          print(card + ' ' + str(name) + ' ' + str(powerName))
    
def getPowerName(powerId):
  with open('powers.json', 'r') as f:
    powers = json.load(f)
    for power in powers:
      if(power == powerId):
        return powers[power]['NAME']
    

print('CHECKING LOCATION CONISTENCY')
checkCards()    