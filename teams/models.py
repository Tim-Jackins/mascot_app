from django.db import models
from phone_field import PhoneField


class Sport(models.Model):
  name = models.CharField(max_length=31)

  def __str__(self):
    return f'{self.name}'


class CollegeDivision(models.Model):
  name = models.CharField(max_length=31)

  def __str__(self):
    return f'{self.name}'


class League(models.Model):
  LEAGUE_TYPE_CHOICES = (('PRO', 'Professional'), ('COL', 'Collegiate'), ('AMA', 'Ameteur'),
                         ('OTR', 'Other'))

  name = models.CharField(max_length=63)
  sport = models.ForeignKey(Sport, models.PROTECT)
  league_type = models.CharField(max_length=3, choices=LEAGUE_TYPE_CHOICES)
  college_division = models.ForeignKey(CollegeDivision, models.PROTECT)


class Team(models.Model):
  STATE_CHOICES = (
    # American states
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),

    # American territories
    ('DC', 'Washington D.C.'),

    # Canadian provinces
    ('ON', 'Ontario'),
  )

  name = models.CharField(max_length=31)
  league = models.ForeignKey(League, models.PROTECT)
  nickname = models.CharField(max_length=31)
  address = models.CharField(max_length=31)
  city = models.CharField(max_length=31)
  state = models.CharField(max_length=2, choices=STATE_CHOICES)  # This also means province
  country = models.CharField(max_length=31)
  phone = PhoneField(blank=True)
  stadium = models.CharField(max_length=31)

  def location(self):
    # Print out City, State letters
    return f'{self.city}, {self.state}'

  def has_multiple_mascots(self):
    pass
