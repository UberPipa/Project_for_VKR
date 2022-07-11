from django.db import models


class Docs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doc_type = models.ForeignKey('TypeDocs', models.DO_NOTHING, db_column='Doc_type')  # Field name made lowercase.

    class Meta:
        db_table = 'docs'
        unique_together = (('id', 'doc_type'),)
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.name

class TypeDocs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'type_docs'
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Тип документов'

    def __str__(self):
        return self.description
