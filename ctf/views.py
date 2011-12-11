from django.http import HttpResponse

def player(request, player_name):
    return HttpResponse('/player/%s' % player_name)

def new_player(request):
    return HttpResponse('/player/new')

def game(request, game_id):
    return HttpResponse("/game/%s" % game_id)

def flag(request, game_id, flag_id):
    return HttpResponse('/game/%s/flag/%s' % (game_id, flag_id))

def next_flag(request, game_id):
    return HttpResponse('/game/%s/flag/next' % game_id)

def catch_flag(request, game_id, flag_id):
    return HttpResponse('/game/%s/flag/%s/catch' % (game_id, flag_id))

