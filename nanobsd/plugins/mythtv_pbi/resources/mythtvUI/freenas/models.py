from django.db import models


class MythTV(models.Model):
    """
    Django model describing every tunable setting for mythtv
    """

    MYTH_SERVICES = ( ('1','MythSetup'), ('2','MythBackend'), ('3', 'MythFrontend'))

    enable = models.BooleanField(default=False)
    x11_DISPLAY = models.CharField(max_length=500, default=':1', blank=True)
    xvfb_enable = models.BooleanField(default=True)
    """
    mythsetup_enable = models.BooleanField(
	default=True,
        help_text=("Run MythTV-Setup")
	)
    mythbackend_enable = models.BooleanField(
	default=False,
        help_text=("Run MythBackend (Only Check ONE!)")
	)
    """
    mythservices_list = models.CharField(max_length=12,
	choices=MYTH_SERVICES,
	help_text=("Must select MythSetup the first time!")
	)
