from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Notice
import ctypes
from django.db.models import Q

# Create your views here.


def index(request):
    notice_list = Notice.objects.order_by('-create_date')[:5]
    context = {'notice_list': notice_list}
    return render(request, 'index.html', context)


def readNotice(request):
    notice_list = Notice.objects.order_by('-create_date')
    # keyword
    kw = request.GET.get('kw', '')
    if len(kw):
        notice_list = notice_list.filter(Q(subject__icontains=kw) |
                                         Q(content__icontains=kw) |
                                         Q(writer__icontains=kw))

    page = request.GET.get('page', '1')
    paginated_by = 10

    if len(notice_list) % paginated_by == 0:
        page_len = len(notice_list) // paginated_by
    else:
        page_len = (len(notice_list) // paginated_by) + 1

    # 페이징 처리
    total_page = list(range(1, page_len + 1))

    start_number = len(notice_list) - (paginated_by * (int(page) - 1))

    start_index = paginated_by * (int(page)-1)
    end_index = paginated_by * int(page)
    notice_list = notice_list[start_index:end_index]

    for notice in notice_list:
        notice.page_number = start_number
        start_number -= 1

    context = {'notice_list': notice_list, 'total_page': total_page, }
    if len(kw):
        context['kw'] = kw
    return render(request, 'readNotice.html', context)


def detail(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    context = {'notice': notice}
    return render(request, 'detail.html', context)


def create(request):
    return render(request, 'make_notice.html')


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
