from portfolio.models import About, Project
from django.http import HttpResponse
from django.template import Context, loader

def about(request):
	return gamma_about(request)

def projects(request):
	return gamma_projects(request)

def contact(request):
	return gamma_contact(request)
	
def tixbayarea(request):
	return gamma_projects_tixbayarea(request)
	
def meta4explorer(request):
	return gamma_projects_meta4explorer(request)
	
def personalportfolio(request):
	return gamma_projects_personalportfolio(request)
	
def graphicdesign(request):
	return gamma_projects_graphicdesign(request)
	
def beta_about(request):
	content = About.objects.first()
	template = loader.get_template('beta/about.html')
	context = Context({
		'content': content,
	})
	return HttpResponse(template.render(context))

def beta_projects(request):
	project_list = Project.objects.all().order_by('priority')
	template = loader.get_template('beta/projects.html')
	context = Context({
		'project_list': project_list,
	})
	return HttpResponse(template.render(context))

def beta_contact(request):
	template = loader.get_template('beta/contact.html')
	context = Context({
		'project_list': project_list,
	})
	return HttpResponse(template.render(context))
	
def gamma_about(request):
	content = About.objects.all()[0]
	template = loader.get_template('gamma/about.html')
	context = Context({
		'content': content,
	})
	return HttpResponse(template.render(context))

def gamma_projects(request):
	project_list = Project.objects.all().order_by('priority')
	template = loader.get_template('gamma/projects.html')
	context = Context({
		'project_list': project_list,
	})
	return HttpResponse(template.render(context))
	
def gamma_projects_tixbayarea(request):
	project = Project.objects.get(title="Tix Bay Area")
	template = loader.get_template('gamma/project.html')
	context = Context({
		'project': project,
		'tools': project.tools.split(', '),
	})
	return HttpResponse(template.render(context))
	
def gamma_projects_meta4explorer(request):
	project = Project.objects.get(title="meta4explorer")
	template = loader.get_template('gamma/project.html')
	context = Context({
		'project': project,
		'tools': project.tools.split(', '),
	})
	return HttpResponse(template.render(context))
	
def gamma_projects_codethechange(request):
	project = Project.objects.get(title="Code The Change")
	template = loader.get_template('gamma/project.html')
	context = Context({
		'project': project,
		'tools': project.tools.split(', '),
	})
	return HttpResponse(template.render(context))
	
def gamma_projects_personalportfolio(request):
	project = Project.objects.get(title="Personal Portfolio")
	template = loader.get_template('gamma/project.html')
	context = Context({
		'project': project,
		'tools': project.tools.split(', '),
	})
	return HttpResponse(template.render(context))
	
def gamma_projects_graphicdesign(request):
	project = Project.objects.get(title="Graphic Design")
	template = loader.get_template('gamma/project.html')
	context = Context({
		'project': project,
		'tools': project.tools.split(', '),
	})
	return HttpResponse(template.render(context))

def gamma_contact(request):
	template = loader.get_template('gamma/contact.html')
	context = Context({
	})
	return HttpResponse(template.render(context))
