from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from meetings.models import Meeting, Room

# Create your views here.

@login_required
def detail(request, id):
    # Meeting.objects.get(pk=id)
    # handles automactly in case of not found
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, template_name="meetings/detail.html", context={"meeting": meeting})

@login_required
def rooms_list(request):
    return render(request, template_name="meetings/rooms.html", context={"rooms": Room.objects.all()})


MeetingForm = modelform_factory(Meeting, exclude=[])

@login_required
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, template_name="meetings/new.html", context={"form": form})

@login_required
def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect("details", id)
    else:
        form = MeetingForm(instance=meeting)
    return render(request, template_name="meetings/edit.html", context={"form": form})

@login_required
def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect("welcome")
    else:
        return render(request, template_name="meetings/confirm_delete.html", context={"meeting": meeting})
