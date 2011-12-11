from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CaptureTheFlag.views.home', name='home'),
    # url(r'^CaptureTheFlag/', include('CaptureTheFlag.foo.urls')),

    # players
    (r'^player/(?P<player_name>\w+)$', 'ctf.views.player'),
    # register
    (r'player/new$', 'ctf.views.new_player'),

    # new game
    (r'^game/new$', 'ctf.views.new_game'),
    # specific game
    (r'^game/(?P<game_id>\d+)$', 'ctf.views.game'),
    
    # flags
    (r'^game/(?P<game_id>\d+)/flag/(?P<flag_id>\d+)$', 'ctf.views.flag'),
    # next flag
    (r'^game/(?P<game_id>\d+)/flag/next$', 'ctf.views.next_flag'),
    # catch flag
    (r'^game/(?P<game_id>\d+)/flag/(?P<flag_id>\d+)/catch$', 'ctf.views.catch_flag'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
