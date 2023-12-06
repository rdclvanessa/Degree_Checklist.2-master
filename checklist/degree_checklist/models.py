from django.db import models


class DegreeType(models.Model):
    dName = models.CharField(
        max_length=50)
    dType = models.CharField(
        max_length=50)

    def str(self):
        return self.dName


class Course (models.Model):
    cName = models.CharField(
        max_length=50)
    cDesc = models.TextField(
        help_text="Course Description.")
    cNum = models.IntegerField(
        help_text="Course Number.")
    cHours = models.IntegerField(
        help_text="Course Credit Hours.")
    cSubject = models.CharField(
        max_length=50)

    def str(self):
        return self.cName


class Core (models.Model):
    coreName = models.CharField(
        max_length=50)
    coreCode = models.IntegerField(
        null=True, help_text="Course Credit Hours.")
    degreeType_id = models.ForeignKey(
        DegreeType, on_delete=models.CASCADE)
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True)

    def str(self):
        return self.coreName


class Program (models.Model):
    pName = models.CharField(
        max_length=50)
    courses_id = models.ManyToManyField(
        'Course', through="ProCourse")
    core_id = models.ForeignKey(
        Core, on_delete=models.CASCADE)

    def str(self):
        return self.pName


class ProCourse (models.Model):
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE)
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE)
    isCore = models.BooleanField()
    isDegree = models.BooleanField()
    isProgram = models.BooleanField()


class DegreeRequirements (models.Model):
    program = models.ForeignKey(
        Program, on_delete=models.CASCADE)
    core = models.ForeignKey(
        Core, on_delete=models.CASCADE)
    isCore = models.BooleanField()
    isDegree = models.BooleanField()
    isProgram = models.BooleanField()

    def str(self):
        return self.program


class Curriculum (models.Model):
    curName = models.CharField(
        max_length=50)
    curHours = models.IntegerField(
        help_text="Curriculum total hours.")
    degreeType = models.ForeignKey(
        DegreeType, on_delete=models.CASCADE)
    degreeRequirements = models.ForeignKey(
        DegreeRequirements, on_delete=models.CASCADE)
