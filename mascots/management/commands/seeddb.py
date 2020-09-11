from django.core.management.base import BaseCommand, CommandError
import csv
import json
import os

from config.settings import BASE_DIR
from teams.models import Sport, CollegeDivision, League, Team
from mascots.models import Maker, Variety, Mascot


def create_seeds(seeds):
  seed_data = []
  for model_seeds in seeds:
    model_name = model_seeds['model_name']
    path = model_seeds['path']

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


# Unfinished method
def custom_create_mascots(model_name, path):
  seed_data = []
  with open(path, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    # Skip header of the file
    header = reader.__next__()
    for row in reader:
      fields = {}
      for model_key, model_value in zip(header[1:], row[1:]):
        fields[model_key] = model_value
      seed_data.append({'model': model_name, 'pk': row[0], 'fields': fields})


class Command(BaseCommand):
  help = 'Seeds the database with the mascot data.'

  def handle(self, *args, **options):
    tables_to_delete = [Mascot, Team, League, Sport, CollegeDivision, Variety, Maker]
    for table in tables_to_delete:
      table.objects.all().delete()

    self.stdout.write(self.style.SUCCESS('Successfully deleted mascot data'))

    # Dictionary with model name as the key and path to seed data as the value.
    # Order does not matter
    basic_seeds = [{
      'model_name': 'mascots.maker',
      'path': f'{BASE_DIR}/db_seed_data/basic_seeds/Mascot_Maker.csv',
    }, {
      'model_name': 'mascots.variety',
      'path': f'{BASE_DIR}/db_seed_data/basic_seeds/Mascot_Variety.csv',
    }, {
      'model_name': 'teams.collegedivision',
      'path': f'{BASE_DIR}/db_seed_data/basic_seeds/tbl_College_Divisions.csv',
    }, {
      'model_name': 'teams.sport',
      'path': f'{BASE_DIR}/db_seed_data/basic_seeds/tbl_Sport.csv',
    }]

    # Dictionary with model name as the key and path to seed data as the value.
    # Order matters!
    relation_seeds = [{
      'model_name': 'teams.league',
      'path': f'{BASE_DIR}/db_seed_data/relational_seeds/Leagues.csv',
    }, {
      'model_name': 'teams.team',
      'path': f'{BASE_DIR}/db_seed_data/relational_seeds/Teams.csv',
    }]

    basic_seeds_path = f'{BASE_DIR}/db_seed_data/basic_seeds.json'
    basic_seed_data = create_seeds(basic_seeds)
    basic_seeds_file = open(basic_seeds_path, 'w')
    json.dump(basic_seed_data, basic_seeds_file)
    basic_seeds_file.close()

    relation_seeds_path = f'{BASE_DIR}/db_seed_data/relational_seeds.json'
    relational_seed_data = create_seeds(relation_seeds)
    relational_seeds_file = open(relation_seeds_path, 'w')
    json.dump(relational_seed_data, relational_seeds_file)
    relational_seeds_file.close()

    # mascots_seeds_path = f'{BASE_DIR}/db_seed_data/mascots_seeds.json'
    # mascots_seed_data = custom_create_mascots(
    #   'mascots.mascot', f'{BASE_DIR}/db_seed_data/relational_seeds/Mascots.csv')

    self.stdout.write(self.style.SUCCESS('Successfully generated mascot data'))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
      from django.core.management import execute_from_command_line
    except ImportError as exc:
      raise ImportError("Couldn't import Django. Are you sure it's installed and "
                        "available on your PYTHONPATH environment variable? Did you "
                        "forget to activate a virtual environment?") from exc

    execute_from_command_line([f'{BASE_DIR}/manage.py', 'loaddata', basic_seeds_path])
    execute_from_command_line([f'{BASE_DIR}/manage.py', 'loaddata', relation_seeds_path])
