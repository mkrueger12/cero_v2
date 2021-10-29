from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import pandas as pd

# read in areas data

areas = pd.read_csv(r'/Users/maxwellkrueger/Documents/Ceros/cero_v2/cero_v2/locale/areas.csv')

all_areas = []

for i in areas:

    data = (i, i)
    all_areas.append(data)


class User(AbstractUser):
    """Default user for Cero v2."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class UrbanArea(models.Model):

    uac = models.CharField(choices=all_areas, max_length=40)

    def __str__(self):
        return self.name
