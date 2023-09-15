from django.db import models

# Create your models here.

gender_choices = (
    ('male','MALE'),
    ('female','FEMALE'),
)

married_choices = (
    ('yes','YES'),
    ('no','NO'),
)

education_choices = (
    ('graduate','GRADUATE'),
    ('not graduate','NOT GRADUATE'),
)

selfemployed_choices = (
    ('yes','YES'),
    ('no','NO'),
)

propertyarea_choices = (
    ('rural','RURAL'),
    ('semiurban','SEMIURBAN'),
    ('urban','URBAN'),
)

class approvals(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    dependents = models.IntegerField(default=0)
    applicantincome = models.IntegerField(default=0)
    coapplicantincome = models.IntegerField(default=0)
    loanamount = models.IntegerField(default=0)
    loanterm = models.IntegerField(default=0)
    credithistory = models.IntegerField(default=0)
    gender = models.CharField(choices=gender_choices, max_length=15)
    married = models.CharField(choices=married_choices, max_length=5)
    education = models.CharField(choices=education_choices,max_length=15)
    selfemployed = models.CharField(choices=selfemployed_choices,max_length=5)
    propertyarea = models.CharField(choices=propertyarea_choices,max_length=15)

    def __str__(self):
        return self.id, self.firstname