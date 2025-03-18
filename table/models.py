from django.db import models

class MyTable(models.Model):
    primary_gene_symbol = models.CharField(max_length=100, primary_key=True)
    symbol = models.CharField(max_length=100, null=True, blank=True)
    concept_id = models.CharField(max_length=100, null=True, blank=True)
    relationship = models.CharField(max_length=100, null=True, blank=True, default='Unknown')
    source = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'disease_capture_ncbi_df'

    def __str__(self):
        return self.primary_gene_symbol