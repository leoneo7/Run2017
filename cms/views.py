from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from django.contrib.auth.models import User
from cms.models import Track
from cms.forms import TrackForm


def track_list(request):
    tracks = Track.objects.all().order_by('id')
    sum_distance = 0
    for track in tracks:
        sum_distance += track.distance
    left = 2017 - sum_distance
    return render(request,
                  'cms/track_list.html',
                  {'tracks': tracks, 'sum_distance': sum_distance, 'left': left})


@login_required
def track_list_user(request):
    tracks = Track.objects.filter(user=request.user)
    sum_distance = 0
    for track in tracks:
        sum_distance += track.distance
    return render(request,
                  'cms/track_list_user.html',
                  {'tracks': tracks, 'sum_distance': sum_distance})


@login_required
def track_edit(request, track_id=None):
    if track_id:
        track = get_object_or_404(Track, pk=track_id)
    else:
        track = Track()

    if request.method == 'POST':
        form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            track = form.save(commit=False)
            track.user = request.user
            track.save()
            return redirect('cms:track_list_user')
    else:
        form = TrackForm(instance=track)

    return render(request, 'cms/track_edit.html', dict(form=form, track_id=track_id))


@login_required
def track_del(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    track.delete()
    return redirect('cms:track_list_user')


def track_ranking(request):
    user = User.objects.raw('select auth_user.id, username, SUM(distance) as distance from auth_user, cms_track '
                            'where auth_user.id = cms_track.user_id '
                            'group by auth_user.id '
                            'order by SUM(distance) desc')[:5]
    # user = User.objects.raw('select * from auth_user')
    # track = Track.objects.all().values('user_id').annotate( sum_distance = Sum('distance'))
    return render(request, 'cms/track_ranking.html', dict(users=user)   )