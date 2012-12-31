function getBaseURL() {
	current_url = window.location.pathname
	if (current_url == '/') {
		return '/';
	} else if (current_url == '/about/' || current_url == '/projects/' || current_url == '/contact/') {
		return '../';
	} else {
		return '../../';
	}
}

function updateNav() {
	var hash = document.location.hash;
	if (hash == '#/about') {
		$("#nav-projects").removeClass('nav-current');
		$("#nav-contact").removeClass('nav-current');
		$("#nav-about").addClass('nav-current');
	} else if (hash == '#/projects') {
		$("#nav-about").removeClass('nav-current');
		$("#nav-contact").removeClass('nav-current');
		$("#nav-projects").addClass('nav-current');	
	} else if (hash == '#/contact') {
		$("#nav-projects").removeClass('nav-current');
		$("#nav-about").removeClass('nav-current');
		$("#nav-contact").addClass('nav-current');	
	} else if (hash != '') {
		$("#nav-projects").removeClass('nav-current');
		$("#nav-about").removeClass('nav-current');
		$("#nav-contact").removeClass('nav-current');	
	}
	return false;
}

function updateContent() {
	var hash = document.location.hash;
	var base = getBaseURL()
	var url = base.substring(0,base.length-1) + hash.substring(1,hash.length) + " #main";
	$("#main").load(url, function() {
		updateNav();
		initBindings();
	});
}

function initBindings() {

	$(".projects_overlay").hover(function() {
		$(this).css('opacity', '0.9');
	}, function() {
		$(this).css('opacity', '');
	});
	
	$("#nav-about").click(function() {
		document.location.hash = "/about";
		return false;
	});
	
	$("#nav-projects").click(function() {
		document.location.hash = "/projects";
		return false;
	});
	
	$("#nav-contact").click(function() {
		document.location.hash = "/contact";
		return false;
	});
	
	$(".project-link").click(function() {
		var url = $(this)[0].pathname;
		document.location.hash = url;
		return false;
	});
}

$(document).ready(function() {
	initBindings();
});


$(function(){
	$(window).hashchange( function(){
		updateContent();
	})
	
	$(window).hashchange();
	
});