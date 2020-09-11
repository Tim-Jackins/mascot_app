import csv
import json


def create_seeds(seeds):
  seed_data = []
  for model_seeds in seeds:
    model_name = model_seeds['model_name']
    path = model_seeds['path']
    print(f'-- Adding {model_name}')

    with open(path, 'r') as csv_file:
      reader = csv.reader(csv_file, delimiter=',')

      # Skip header of the file
      header = reader.__next__()

      for row in reader:
        fields = {}
        for model_key, model_value in zip(header[1:], row[1:]):
          fields[model_key] = model_value
        seed_data.append({'model': model_name, 'pk': row[0], 'fields': fields})
  return seed_data


# Dictionary with model name as the key and path to seed data as the value.
# Order does not matter
basic_seeds = [{
  'model_name': 'mascots.maker',
  'path': 'db_seed_data/basic_seeds/Mascot_Maker.csv',
}, {
  'model_name': 'mascots.variety',
  'path': 'db_seed_data/basic_seeds/Mascot_Variety.csv',
}, {
  'model_name': 'teams.collegedivision',
  'path': 'db_seed_data/basic_seeds/tbl_College_Divisions.csv',
}, {
  'model_name': 'teams.sport',
  'path': 'db_seed_data/basic_seeds/tbl_Sport.csv',
}]

# Dictionary with model name as the key and path to seed data as the value.
# Order matters!
relation_seeds = [
  {
    'model_name': 'teams.league',
    'path': 'db_seed_data/relational_seeds/Leagues.csv',
  },
  {
    'model_name': 'teams.team',
    'path': 'db_seed_data/relational_seeds/Teams.csv',
  },
  # {
  #   'model_name': 'mascots.mascot',
  #   'path': 'db_seed_data/relational_seeds/Mascots.csv',
  # }
]

print('Creating basic seeds')
basic_seed_data = create_seeds(basic_seeds)
basic_seeds_file = open('db_seed_data/basic_seeds.json', 'w')
json.dump(basic_seed_data, basic_seeds_file)

print('Creating relational seeds')
relational_seed_data = create_seeds(relation_seeds)
relational_seeds_file = open('db_seed_data/relational_seeds.json', 'w')
json.dump(relational_seed_data, relational_seeds_file)
