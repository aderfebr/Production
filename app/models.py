from django.db import models

# Create your models here.

class Edge(models.Model):
    id = models.IntegerField(primary_key=True)
    node1 = models.IntegerField(blank=True, null=True)
    node2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edge'


class Node(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node'