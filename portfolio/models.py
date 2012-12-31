from django.db import models

class About(models.Model):
	description = models.TextField()
	
	@classmethod
	def repopulate(About):
		for content in About.objects.all():
			content.delete()
		content = About(
			description = "<p>Hello! My name is Christina Guo and I'm a third year UC Berkeley student studying Electrical Engineering & Computer Science. My passion lies in web development and UI design, but I have also been rapidly developing an interest in artifical intelligence and machine learning. When I'm not coding, I enjoy dabbling in graphic design and photography, as well as drinking mochas in random coffee shops.</p><p>I love collaborating with toher people, and I'm always looking out for cool new projects to work on. Feel free to click the contact link above and get in touch!"
		)
		content.save()
			

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
			description = "For a software engineering course, I teamed up with four other students to build a show ticketing website for Theatre Bay Area, a non-profit theatre organization based in San Francisco. Site features include the ability to get theatre show recommendations based on category, keyword, location, and price. User accounts, as well as the ability to login through Facebook, were also implemented, so that favorited shows and past history of clicks could further personalize the user's recommendation listings. Besides the technical aspect of the project, I also gained experience with software engineering techniques such as Agile, Test-Driven Development, and consulting with a non-technical customer.",
			tools = "Ruby on Rails, PostgreSQL, JavaScript/JQuery, ERB, CSS, Cucumber, RSpec",
			photo_thumbnail_link = "/media/images/tix_thumbnail.png",
			photo_medium_link_1 = "/media/images/tix_med_1.png",
			photo_medium_link_2 = "/media/images/tix_med_2.png",
			client = "Theatre Bay Area",
			priority = 1
		)
		proj.save()

		proj = Project(
			title = "meta4explorer",
			description = "During my 2nd year of college, I worked with the Berkeley Institute of Design to research the ways in which computer technology could aid the product design process. Specifically, we studied the ways in which an web application could help designers come up with metaphors that they could apply to their own projects, by providing a new angle through which they could view the problems they were trying to solve. Through this project, I gained experience in web design, web development, and machine learning. Using matrix and graph algorithms, I created a metaphor recommendation engine. I also both designed, prototyped, and built a wrapper website for the recommendation engine GUI. It allowed users to create accounts, save their previous work, and share their work with other users.",
			tools = "Python, Django, SQLite, HTML, CSS, paper/pencil",
			photo_thumbnail_link = "/media/images/meta_thumbnail.png",
			photo_medium_link_1 = "/media/images/meta_med_1.png",
			photo_medium_link_2 = "/media/images/meta_med_2.png",
			priority = 2
		)
		proj.save()

		#proj = Project(
		#	title = "Code The Change",
		#	description = "",
		#)
		#proj.save()
	
		proj = Project(
			title = "Personal Portfolio",
			description = "I love learning random tricks with HTML and CSS, which means my personal website tends to get a redesign every time I'm on break. Check out some past iterations of this website here: <a href="">alpha</a>, <a href="">beta</a>, <a href="">gamma</a>",
			tools = "Python, Django, SQLite, HTML, CSS, Paper/Pencil",
			photo_thumbnail_link = "/media/images/personal_thumbnail.png",
			photo_medium_link_1 = "/media/images/personal_med_1.png",
			photo_medium_link_2 = "/media/images/personal_med_2.png",
			priority = 3
		)
		proj.save()
		
		proj = Project(
			title = "Graphic Design",
			description = "Although I've been playing around with Photoshop since the 7th grade, it wasn't until college that I got into graphic design. In the past few years, I've designed flyers for various events and student organizations, flyers for infosessions and company mixers, banquet programs, and logos.",
			tools = "Photoshop, Illustrator, pencil/paper",
			photo_thumbnail_link = "/media/images/graphic_thumbnail.png",
			photo_medium_link_1 = "/media/images/graphic_med_1.png",
			photo_medium_link_2 = "/media/images/graphic_med_2.png",
			priority = 4
		)
		proj.save()

	
	
