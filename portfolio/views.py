from portfolio.models import About, Project
from django.http import HttpResponse

def about(request):
	content = About.objects.first()
	template = loader.get_template('portfolio/templates/about.html')
	context = Context({
		'content': content,
	})
	return HttpResponse(template.render(context))

def projects(request):
	project_list = Project.objects.all().order_by('priority')
	template = loader.get_template('portfolio/templates/projects.html')
	context = Context({
		'project_list': project_list,
	})
	return HttpResponse(template.render(context))

def contact(request):
	template = loader.get_template('portfolio/templates/contact.html')
	context = Context({
		'project_list': project_list,
	})
	return HttpResponse(template.render(context))