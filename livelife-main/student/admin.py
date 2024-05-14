from django.contrib import admin
from .models import DonationCause, Donor, BlogPost, ContactForm, Sponsor,Service, RescueRequest


# Register your models here.
admin.site.register(Donor)
admin.site.register(DonationCause)
admin.site.register(BlogPost)
admin.site.register(ContactForm)
admin.site.register(Sponsor)
admin.site.register(Service)
admin.site.register(RescueRequest)
