import uuid
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE, SOFT_DELETE


class Beach(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    beach_status = [
        ("cleaned", "Cleaned"),
        ("messy", "Messy"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID",
    )
    name = models.CharField(max_length=20, blank=True, null=True)

    location = models.TextField(blank=False)
    lat = models.FloatField()
    lng = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=7,
        choices=beach_status,
        blank=True,
        null=True,
    )

    def save(self):
        super(Beach, self).save()
