# Composite-ForeignKey-in-Djnago
#Composite ForeignKey and composite PrimaryKey (unique_together) in Django 

Composite FK => Foreignkey(child) of more than one columns that refer primaryKey(Parent) of more than one columns.
1. Djnago does not support composite key(means more than one columns as PK in a table), But we can implement by using unique_together.
2. If we want more than one columns as ForeignKey then we use Composite FK module that will refer another table of primaryKey (unique_together columns).

1. Install using pip:
pip install django-composite-foreignkey

Parent table(Primary key table)->

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
      
Child table(Foreign key table) ->

    class Auth(models.Model):
    org_code = models.CharField(max_length=45)
    org_dom = models.CharField(max_length=45)
    org_subdom = models.CharField(max_length=45)
    org_seq = models.IntegerField()
    
    auth=CompositeForeignKey(to=OrgSubdom,db_column='org_seq',
                             related_name='auths', on_delete=models.CASCADE,
                          to_fields={'org_code':'org_code', 'org_dom':'org_dom', 'org_subdom':'org_subdom'}, )
    question = models.CharField(max_length=255, blank=True, null=True)
 
    class Meta:
        db_table = 'auth'
        unique_together = (('org_code', 'org_dom', 'org_subdom', 'org_seq'),)
    def __str__(self):
        return 'Auth '+ str(self.question)
      
--------------------------This is logic for composite key-------------------

    auth=CompositeForeignKey(to=OrgSubdom,db_column='org_seq',related_name='auths', on_delete=models.CASCADE,
                          to_fields={'org_code':'org_code', 'org_dom':'org_dom', 'org_subdom':'org_subdom'}, )
                          
                          #to_fields={pk_column_name : fK_column_name }
                          #we can map directly by set-> to_fields={"org_code", "org_dom", "org_subdom"}
                          
    -------------------------------------------------------------------------------
<b> I pointed issues-->/b> I able to enter data in ForignKey(child table) without mapping child columns to Parent table columns in django, technically this is wrong when I do same in MYSQL database then getting error  "Cannot add or update a child row: a foreign key constraint fails".
So, In Django we able to insert data without PK column data. 
    
   
