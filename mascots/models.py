from django.db import models
from teams.models import Team


class Maker(models.Model):
  name = models.CharField(max_length=31)
  website = models.URLField()


class Variety(models.Model):
  name = models.CharField(max_length=31)


class Mascot(models.Model):
  MASCOT_CHARACTER_TYPE_CHOICES = (
      ('AC', 'Animal Character'),
      ('LA', 'Live Animal'),
      ('HC', 'Human Character'),
      ('LH', 'Live Human'),
      # ('NM', 'No Mascot'),
      ('MC', 'Multiple Characters'))

  # Maybe implement this?
  # PERFORMER_TYPE_CHOICES

  name = models.CharField(max_length=31)
  team = models.ForeignKey(Team, on_delete=models.PROTECT)
  date_unveiled = models.DateField()
  year_retired = models.DateField()
  mhof_nominated_year = models.DateField()
  mhof_inducted_date = models.DateField()
  history = models.CharField(max_length=255)
  student_pro = models.BooleanField()
  image_file = models.ImageField(upload_to='mascots_portraits')
  image_url = models.URLField()
  character_type = models.CharField(max_length=2, choices=MASCOT_CHARACTER_TYPE_CHOICES)
  maker = models.ForeignKey(Maker, on_delete=models.PROTECT)
  variety = models.ForeignKey(Variety, related_name='variety', on_delete=models.PROTECT)
  sub_veriety = models.ForeignKey(Variety, related_name='sub_variety', on_delete=models.PROTECT)
  selection_process = models.CharField(max_length=255)
  performer_type = models.CharField(max_length=255)
  website = models.URLField()

  def is_current_character():
    pass
