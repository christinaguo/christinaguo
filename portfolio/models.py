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
	def repopulate(Project):
	
		for proj in Project.objects.all():
			proj.delete()

		proj = Project(
			title = "Tix Bay Area",
			description = "For a software engineering course, I teamed up with four other students to build a show ticketing website for Theatre Bay Area, a non-profit theatre organization based in San Francisco. Features include the ability to get theatre show recommendations based on category, keyword, location, and price. User accounts, as well as the ability to login through Facebook, were also implemented, so that favorited shows and past history of clicks could further personalize the user's recommendation listings. Besides the technical aspect of the project, I also gained experience with software engineering techniques such as Agile, Test-Driven Development, and consulting with a non-technical customer.",
			tools = "Ruby on Rails, PostgreSQL, JavaScript/JQuery, HAML, ERB, Cucumber, RSpec",
			photo_thumbnail_link = "/media/images/tix_thumbnail.png",
			photo_medium_link_1 = "/media/images/tix_med_1.png",
			photo_medium_link_2 = "/media/images/tix_med_2.png",
			client = "Theatre Bay Area",
			priority = 1
		)
		proj.save()

		#proj = Project(
		#	title = "meta4explorer",
		#	description = "",
		#)
		#proj.save()

		#proj = Project(
		#	title = "Code The Change",
		#	description = "",
		#)
		#proj.save()
	
		#proj = Project(
		#	title = "Personal Portfolio",
		#	description = "",
		#)
		#proj.save()

	
	
