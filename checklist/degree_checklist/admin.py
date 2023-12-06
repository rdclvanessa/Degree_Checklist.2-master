from django.contrib import admin
from degree_checklist.models import (DegreeType, Course, Core, Program, ProCourse, DegreeRequirements, Curriculum)

admin.site.register(DegreeType)
admin.site.register(Course)
admin.site.register(Core)
admin.site.register(Program)
admin.site.register(ProCourse)
admin.site.register(DegreeRequirements)
admin.site.register(Curriculum)
