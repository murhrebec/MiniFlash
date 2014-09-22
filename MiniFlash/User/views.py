from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def user_settings(request):
	return render_to_response('authenticated/user/user_settings.html', locals(), context_instance=RequestContext(request))