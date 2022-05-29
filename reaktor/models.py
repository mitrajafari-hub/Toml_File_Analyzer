from django.db import models

class List_package(models.Model):
    pname = models.CharField(max_length=100)
    pdesc = models.CharField(max_length=700)
    class Meta:
        db_table = "list_package"
        
        
class Pkg_Ind(models.Model):
    pack_id = models.IntegerField(primary_key=False)
    depend_name = models.CharField(max_length=500)
    depend_version = models.CharField(max_length=100)
    class Meta:
        db_table = "pkg_ind"
