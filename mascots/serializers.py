from rest_framework import serializers
from .models import Mascot


class MascotSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mascot
    fields = ('id', 'name', 'team', 'date_unveiled', 'year_retired', 'mhof_nominated_year',
              'mhof_inducted_date', 'history', 'student_pro', 'image_file', 'image_url',
              'character_type', 'maker', 'variety', 'sub_veriety', 'selection_process',
              'performer_type', 'website')
