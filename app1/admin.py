from django.contrib import admin
from .models import PartyDetails
from .models import Query
from .models import Feedback
from .models import Photo
from .models import Document

# from .models import Photo_venue
# from .models import Meta
# Register your models here.
admin.site.register(Photo)
admin.site.register(Document)
# admin.site.register(Meta)
admin.site.register(PartyDetails)
admin.site.register(Query)
admin.site.register(Feedback)
# admin.site.register(Photo_venue)