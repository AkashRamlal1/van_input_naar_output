AC = int(input('hoevel croisantjes wil je hebben?'))
#aantal croisantjes ^^
PC = 9
#prijs croisantjes ^^
print(f'je wilt {AC} croisantjes')
print(f'{AC} x {PC} = {AC * PC}')
ASB = int(input('hoevel stokbroden wil je hebben?'))
#aantal stokbrood
PSB = 9
#prijs stokbrood
AWSB = (ASB *  PSB)
print(f'je wilt {ASB} stokbroden')
print(f'{ASB} x {PSB} = {ASB * PSB} stokbroden')
totaal = ((ASB * PSB)+(AC *PC))
print(f'je totaal prijs voor de feest lunch is {str(totaal)} euro')
