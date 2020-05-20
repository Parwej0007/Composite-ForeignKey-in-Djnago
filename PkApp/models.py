from compositefk.related_descriptors import CompositeForwardManyToOneDescriptor
from django.db import models
from compositefk.fields import CompositeForeignKey, LocalFieldValue, RawFieldValue
# Create your models here.
from django.db.models import ForeignObject
class Org(models.Model):
    org_code = models.CharField(primary_key=True, max_length=15)
    org_name = models.CharField(max_length=100)
    org_desc = models.CharField(max_length=255, blank=True, null=True)
    org_city = models.CharField(max_length=45, blank=True, null=True)
    org_state = models.CharField(max_length=45, blank=True, null=True)
    org_country = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'org'
    def __str__(self):
        return  'Org '+str(self.org_name)
class Seq(models.Model):
    org_code = models.ForeignKey(Org, on_delete=models.CASCADE, db_column='org_code',
                                    related_name='seqs')
    seq_num = models.IntegerField()
    seq_type = models.CharField(max_length=15)
    seq_desc = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'seq'
        unique_together = (('org_code', 'seq_num', 'seq_type'),)
    def __str__(self):
        return 'seq '+ str(self.seq_type)

class OrgSubdom(models.Model):
    org_code = models.ForeignKey(Org, on_delete=models.CASCADE, db_column='org_code',
                                    related_name='orgsubdoms')
    org_dom = models.CharField(max_length=45)
    org_subdom = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'org_subdom'
        unique_together = (('org_code', 'org_dom', 'org_subdom'),)
    def __str__(self):
        return 'Orgsubdom '+ str(self.org_subdom)

class Auth(models.Model):
    org_code = models.CharField(max_length=45)
    org_dom = models.CharField(max_length=45)
    org_subdom = models.CharField(max_length=45)
    org_seq = models.IntegerField()
    auth=CompositeForeignKey(to=OrgSubdom,db_column='org_seq',
                             related_name='auths', on_delete=models.CASCADE,
                          to_fields={'org_code':'org_code', 'org_dom':'org_dom', 'org_subdom':'org_subdom'}, )
    question = models.CharField(max_length=255, blank=True, null=True)
    answer_type = models.CharField(max_length=15, blank=True, null=True)
    answer = models.CharField(max_length=500, blank=True, null=True)
    answer_hel_field = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.CharField(max_length=45)
    created_datetime = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'auth'
        unique_together = (('org_code', 'org_dom', 'org_subdom', 'org_seq'),)
    def __str__(self):
        return 'Auth '+ str(self.question)
    #
    # def contribute_to_class(self, cls, name, **kwargs):
    #     kwargs['private_only'] = True
    #
    #     super(ForeignObject, self).contribute_to_class(cls, name, **kwargs)
    #     setattr(cls, self.name, CompositeForwardManyToOneDescriptor(self))
    #     CompositeForeignKey.contribute_to_class = self.contribute_to_class
