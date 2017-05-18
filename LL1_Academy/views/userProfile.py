import operator

from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib import messages
from django.forms.models import model_to_dict

from LL1_Academy.models import *



def profile(request):
	current_user_id = request.user.id
	user_histories = UserHistory.objects.all().filter(user_id=current_user_id)
	context = {"skipped_grammars": [], 
		"completed_grammars": [], 
		"avg_score": 0, 
		"user_info": {}}
	total_score = 0
	# get data for each grammar that the user has completed
	for user_history in user_histories:
		grammar = Grammar.objects.get(pk=user_history.grammar_id)
		grammar_dict = model_to_dict(grammar, fields=["gid","prods"])
		stats_dict = model_to_dict(user_history, fields=["complete", "score", "updateTime"])
		combined_dicts = dict(list(grammar_dict.items()) + list(stats_dict.items()))
		if stats_dict["complete"]:
			context["completed_grammars"].append(combined_dicts)
			total_score += stats_dict["score"]
		else: 
			context["skipped_grammars"].append(combined_dicts)
	#sort grammarhistory based on time
	context["completed_grammars"] = sorted(context["completed_grammars"], key=lambda k: k['updateTime'])
	context["skipped_grammars"] = sorted(context["skipped_grammars"], key=lambda k: k['updateTime'])
	# get user information
	user_info = model_to_dict(User.objects.get(pk=current_user_id), ["first_name", "last_name", "data_joined", "email", "last_login"])
	context["user_info"] = user_info
	context["avg_score"] = total_score / len(context["completed_grammars"])
	return render(request, 'LL1_Academy/profile.html', context)

def disconnect_account(request):
    context = {}
    if not request.user.is_authenticated():
        messages.error(request, 'Please log in to access this feature.')
        return redirect('account_login')

    provider_name = request.POST.get('account', '')

    for acc in request.user.socialaccount_set.all().iterator():
        if acc.get_provider().id == provider_name:
            acc.delete()
            messages.info(request,
                          'Your account has been successfully disconnected.')

    return render(request, 'LL1_Academy/profile.html', context)