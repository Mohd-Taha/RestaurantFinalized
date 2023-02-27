from django.contrib import admin

# Register your models here.
from .models import Team
admin.site.register(Team)
from .models import order
admin.site.register(order)
from .models import testimonial
admin.site.register(testimonial)
from .models import featured
admin.site.register(featured)
from .models import products
admin.site.register(products)
from .models import starters
admin.site.register(starters)