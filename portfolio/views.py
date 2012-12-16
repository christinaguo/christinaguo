from portfolio.models import About, Project
from django.http import HttpResponse

def about(request):
	return gamma_about()

def projects(request):
	return gamma_projects()

def contact(request):
	return gamma_contact()
	
def beta_about(request):
	content = About.objects.first()
	template = loader.get_template('portfolio/templates/beta/about.html')
	context = Context({
		'content': content,
	})
	return HttpResponse(template.render(context))

def beta_projects(request):
	project_list = Project.objects.all().order_by('priority')
	template = loader.get_template('portfolio/templates/beta/projects.html')
	context = Context({
		'project_list': project_list,
	})
	return HttpResponse(template.render(context))

def beta_contact(request):
	template = loader.get_template('portfolio/templates/beta/contact.html')
	context = Context({
		'project_list': project_list,
	})
	return HttpResponse(template.render(context))
	
def gamma_about(request):
	content = About.objects.first()
	template = loader.get_template('portfolio/templates/gamma/about.html')
	context = Context({
		'content': content,
	})
	return HttpResponse(template.render(context))

def gamma_projects(request):
	project_list = Project.objects.all().order_by('priority')
	template = loader.get_template('portfolio/templates/gamma/projects.html')
	context = Context({
		'project_list': project_list,
	})
	return HttpResponse(template.render(context))

def gamma_contact(request):
	template = loader.get_template('portfolio/templates/gamma/contact.html')
	context = Context({
		'project_list': project_list,
	})
	return HttpResponse(template.render(context))
	
def navigation():