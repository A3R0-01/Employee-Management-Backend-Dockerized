from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class AbstractManager(models.Manager):
    def get_by_id(self, public_id):
        try:
            obj = self.get(PublicId=public_id)
            return obj
        except (ObjectDoesNotExist, TypeError, ValueError):
            return Http404
        
class AbstractModel(models.Model):
    PublicId = models.UUIDField(db_index=True, unique=True, editable=False, default=uuid.uuid4)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    objects = AbstractManager()

    class Meta:
        abstract=True
class AbstractFileModel(models.Model):
    file = models.FileField()