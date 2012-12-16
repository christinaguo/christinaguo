from django.db import models

class About(models.Model):
	description = models.TextField()
	
	@classmethod
	def repopoulate():
		for content in About.objects.all():
			content.delete()
		content = About(
			description = ""
		)
			

class Project(models.Model):

	title = models.TextField()
	description = models.TextField()
	tools = models.TextField()
	github_link = models.URLField(null=True)
	photo_thumbnail_link = models.FilePathField(path="/media/images/", null=True)
	photo_small_link = models.FilePathField(path="/media/images/", null=True)
	photo_medium_link_1 = models.FilePathField(path="/media/images/", null=True)
	photo_medium_link_2 = models.FilePathField(path="/media/images/", null=True)
	collaborators = models.TextField(null=True)
	client = models.TextField(null=True)
	priority = models.IntegerField(null=True)
	
	@classmethod
	def repopulate():
	
		for proj in Project.objects.all():
			proj.delete()

		proj = Project(
			title = "Tix Bay Area",
			description = "",
		)
		proj.save()

		proj = Project(
			title = "Tix Bay Area",
			description = "",
		)
		proj.save()

		proj = Project(
			title = "meta4explorer",
			description = "",
		)
		proj.save()

		proj = Project(
			title = "Code The Change",
			description = "",
		)
		proj.save()
	
		proj = Project(
			title = "Personal Portfolio",
			description = "",
		)
		proj.save()

	
	
