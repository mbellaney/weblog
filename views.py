from django.shortcuts import get_object_or_404, render_to_response
from weblog.models import Entry

def entries_index(request):
    return render_to_response('weblog/entry_index.html',
                              { 'entry_list': Entry.objects.all() })



