from events.models import EnvironmentEvent

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=EnvironmentEvent)
def sender(sender, instance, **kwargs):
    # if the bathroom is now available
    if instance.device.bathroom_set.get().available:
        alerts = instance.device.bathroom_set.get().bathroomalert_set.all()

        for alert in alerts:
            alert.send_sms_alert()
            alert.delete()
