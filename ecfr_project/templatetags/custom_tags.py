from django import template

register = template.Library()
def replace_arg(value,arg):
	return value.replace(arg,"|")

register.filter('replace_arg',replace_arg)
