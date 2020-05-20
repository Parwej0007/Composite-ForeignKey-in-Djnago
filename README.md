# Composite-ForeignKey-in-Djnago
#Composite ForeignKey and composite PrimaryKey (unique_together) in Django 

Composite FK => Foreignkey(child) of more than one columns that refer primaryKey(Parent) of more than one columns.
1. Djnago does not support composite key(means more than one columns as PK in a table), But we can implement by using unique_together.
2. If we want more than one columns as ForeignKey then we use Composite FK module that will refer another table of primaryKey (unique_together columns).

1. Install using pip:
pip install django-composite-foreignkey

Parent table ->

    class OrgSubdom(models.Model):
        org_code = models.ForeignKey(Org, on_delete=models.CASCADE, db_column='org_code', related_name='orgsubdoms')
        org_dom = models.CharField(max_length=45)
        org_subdom = models.CharField(max_length=45)
        created_by = models.CharField(max_length=45, blank=True, null=True)
        created_datetime = models.DateTimeField(blank=True, null=True)
        
        class Meta:
            db_table = 'org_subdom'
            unique_together = (('org_code', 'org_dom', 'org_subdom'),)
        def __str__(self):
            return 'Orgsubdom '+ str(self.org_subdom)
      
