from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Notice
import ctypes

# Create your views here.


def index(request):
    notice_list = Notice.objects.order_by('-create_date')[:5]
    context = {'notice_list': notice_list}
    return render(request, 'index.html', context)


def readNotice(request):
    notice_list = Notice.objects.order_by('-create_date')
    context = {'notice_list': notice_list}
    return render(request, 'readNotice.html', context)


def detail(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    context = {'notice': notice}
    return render(request, 'detail.html', context)


def createNotice(request):
    if request.method == 'POST':
        newNotice = Notice(
            subject=request.POST['subject'],
            content=request.POST['content'],
            writer=request.POST['writer'],
            create_date=timezone.now(),
            password=request.POST['password'])
        newNotice.save()
    return redirect('/mysite/readNotice/')


def delete(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    notice.delete()
    return redirect('/mysite/readNotice/')


def update(request, notice_id):
    if request.method == 'POST':
        notice = Notice.objects.get(id=notice_id)
        context = {'notice': notice}
        if notice.password == request.POST['password']:
            return render(request, 'update.html', context)
        else:
            msg = ctypes.windll.user32.MessageBoxW(None, "비밀번호가 틀립니다", "오류", 0)
            return redirect(f'/mysite/readNotice/{notice_id}/')


def update_notice(request, notice_id):
    if request.method == 'POST':
        notice = Notice.objects.get(id=notice_id)
        notice.subject = request.POST['subject']
        notice.content = request.POST['content']
        notice.writer = request.POST['writer']
        notice.create_date = timezone.now()
        notice.password = request.POST['password']
        notice.save()
    return redirect(f'/mysite/readNotice/{notice_id}/')
