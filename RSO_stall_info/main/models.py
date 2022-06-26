# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


class TypeDocs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'type_docs'
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Тип документов'
