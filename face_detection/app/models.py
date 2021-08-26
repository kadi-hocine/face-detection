from django.db import models
#from django.utils import timezone


# Customer table
class Customer(models.Model):
    boolChoice = (("Male","Male"),("Female","Female"))
    balcklistChoice = (("Yes", "Yes"), ("No", 'No'))

    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(blank=True, null=True)
    isBlackList = models.CharField(max_length = 3,choices=balcklistChoice)
    gender = models.CharField(max_length = 6,choices=boolChoice)
    image = models.ImageField(upload_to='images')

    def str(self):
        return '%s %s' % (self.first_name, self.last_name)

    def unicode(self):
        return '%s %s' % (self.first_name, self.last_name)

# # Model Accident
# class Incident(models.Model):
#     # accident_id = models.AutoField(primary_key=True)
#     label = models.CharField(max_length=120)

#     def str(self):
#         return self.label

# Each image is converted on embedding vector and stored in BDD as vector 
# class EmbeddingVectors(models.Model):
#     ev_id = models.AutoField(primary_key=True)
#     link_file = models.CharField(max_length=10000)
#     person_ev = models.ForeignKey(Customer, related_name="person_ev", on_delete=models.CASCADE, db_column='customer_id')


# class VisitsHistory(models.Model):
#     # visit_id = models.AutoField(primary_key=True)
#     entry_date = models.DateTimeField(editable=False)
#     exit_date = models.DateTimeField()
#     total_spent = models.FloatField()
#     person_vh = models.ForeignKey(Customer, related_name="person_vh", on_delete=models.CASCADE, db_column='person_id')

#     def init(self, *args, kwargs):
#         # super().init(args, kwargs)
#         self.id = None

#     def save(self, *args, kwargs):
#         """ On save, update timestamps """
#         if not self.id:
#             self.entry_date = timezone.now()
#         # self.entry_date_modified = timezone.now()
#         return super(VisitsHistory, self).save(*args, kwargs)

#     def save_exit(self, *args, kwargs):
#         """ On save, update timestamps """
#         if self.id:
#             self.exit_date = timezone.now()
#         # self.exit_date_modified = timezone.now()
#         return super(VisitsHistory, self).save(*args, **kwargs)


# class Association(models.Model):
#     association_id = models.AutoField(primary_key=True)
#     accident_id = models.ForeignKey(Incident, related_name="accident_id", on_delete=models.CASCADE,
#                                     db_column='accident_id')
#     visit_id = models.ForeignKey(VisitsHistory, related_name="visit_id", on_delete=models.CASCADE,
#                                  db_column='visit_id')
#     description = models.TextField(blank=True, null=True)
#     damages_estimation = models.FloatField()

#     class Meta:
#         managed = True
#         db_table = 'association'
#         unique_together = (('accident_id',
#                             'visit_id'),)

#     def str(self):
#         return self.description

