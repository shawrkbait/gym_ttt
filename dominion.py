import yaml

with open('dominion.yaml', 'r') as stream:
  try:
    data = yaml.load(stream)
  except yaml.YAMLError as exc:
    print(exc)


for card in data['cards']:
  print(card)
