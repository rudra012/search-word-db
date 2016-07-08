from django.db.models import Q
from django.http import HttpResponse,HttpResponseBadRequest
from django.shortcuts import render
from demo import models
import json
# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)
    # now = get_current_datetime()
    # battle_master_obj = models.Deals.objects.filter(is_published__exact=True, start__lte=now, winner='0').order_by('-end')
    # context = dict(/
    #     title="Spotify Login Page",
    #     current_action=request.resolver_match.url_name
    # )
    # last_winner = Battle.objects.filter(~Q(winner='0')).filter(is_published__exact=True).order_by('-end')

    # if last_winner:
    #     print("Winner", last_winner[0].battle_name)
    #     context['last_winner'] = last_winner[0]
    #     last_winner_id = int(last_winner[0].winner)
    #     context['last_winner_track'] = last_winner[0].track_link_1.split('/')[-1] if last_winner_id == 1 else \
    #         last_winner[0].track_link_2.split('/')[-1]
    #     context['last_winner_count'] = last_winner[0].streams_count_1 if last_winner_id == 1 else \
    #         last_winner[0].streams_count_2
    #
    #
    #     context['battle'] = battle_master_obj[0]
    #     context['track1'] = battle_master_obj[0].track_link_1.split('/')[-1]
    #     context['track2'] = battle_master_obj[0].track_link_2.split('/')[-1]
    #     if (context['battle'].end - now).total_seconds() > 0:
    #         context['count_down_time'] = (context['battle'].end - now).total_seconds() + 5
    #     else:
    #         context['count_down_time'] = 0
    #         context['neg_counter'] = 1

def find_deal(request):
    text = request.GET.get('text')
    if text:
        print(text)
        result_list = []
        deal_obj = models.Deals.objects.filter(Q(title__icontains=text))
        print(deal_obj)
        for deal in deal_obj:
            deal_dict = {
                'title': deal.title,
                'link': deal.link,
                'location': deal.location,
            }
            result_list.append(deal_dict)
        return HttpResponse(json.dumps(result_list))
    else:
        return HttpResponseBadRequest()