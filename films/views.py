from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required  
from .models import Film_list

# Create your views here.
@login_required
def films(request):
    films = Film_list.objects.all()
    return render(request, 'films/films.html', {'films': films})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Film_list, Parties
from .forms import TicketBookingForm


# def film_detail(request, film_name):
#     film = get_object_or_404(Film_list, name=film_name)
    
#     # التأكد من أن الحفلات المرتبطة بالفيلم يتم استرجاعها
#     parties = Parties.objects.filter(film=film)  # الحصول على جميع الحفلات المرتبطة بالفيلم
    
#     # إذا كانت الحفلات غير موجودة أو فارغة، نعرض رسالة مناسبة
#     if not parties:
#         return render(request, 'films/film.html', {'film': film, 'error': 'لا توجد حفلات لهذا الفيلم حاليًا.'})
    
#     # إذا كان هناك أكثر من حفلة، نعرض للمستخدم قائمة لاختيار الحفلة
#     if len(parties) == 1:
#         party = parties.first()
#         form = TicketBookingForm(request.POST or None, party=party)
#     else:
#         if request.method == 'POST':
#             selected_party_id = request.POST.get('party')
#             if selected_party_id:
#                 party = get_object_or_404(Parties, id=selected_party_id)
#                 form = TicketBookingForm(request.POST, party=party)
#             else:
#                 form = TicketBookingForm(request.POST)  # إذا لم يتم اختيار حفلة، نعرض الخطأ
#         else:
#             form = None
#             party = None

#     if form and form.is_valid():
#         number_of_tickets = form.cleaned_data['number_of_tickets']
#         party.seats -= number_of_tickets  # تقليل عدد المقاعد المتاحة
#         party.save()  # حفظ التحديثات في قاعدة البيانات
#         return redirect('confirmation')  # قم بتوجيه المستخدم إلى صفحة تأكيد الحجز

#     return render(request, 'films/film.html', {
#         'film': film,
#         'parties': parties,  # تمرير جميع الحفلات المتاحة للفيلم
#         'form': form,
#         'party': party,
#     })
@login_required
def film_detail(request, film_name):
    film = get_object_or_404(Film_list, name=film_name)
    parties = Parties.objects.filter(film=film)
    
    if not parties:
        return render(request, 'films/film.html', {'film': film, 'error': 'لا توجد حفلات لهذا الفيلم حاليًا.'})
    
    # نعرف الـ party و form من البداية
    party = None
    form = None
    
    if len(parties) == 1:
        party = parties.first()
        form = TicketBookingForm(request.POST or None, party=party)
    else:
        if request.method == 'POST':
            selected_party_id = request.POST.get('party')
            if selected_party_id:
                party = get_object_or_404(Parties, id=selected_party_id)
                form = TicketBookingForm(request.POST, party=party)
            else:
                # لو مفيش حفلة مختارة، نرجع خطأ للمستخدم
                return render(request, 'films/film.html', {
                    'film': film,
                    'parties': parties,
                    'form': TicketBookingForm(request.POST),
                    'error': 'يرجى اختيار حفلة قبل الحجز.'
                })
        # لو GET، نعرض القايمة بدون form أو party

    if form and form.is_valid():
        number_of_tickets = form.cleaned_data['number_of_tickets']
        party.seats -= number_of_tickets
        party.save()
        return redirect('confirmation')

    return render(request, 'films/film.html', {
        'film': film,
        'parties': parties,
        'form': form,
        'party': party,
    })

def confirmation(request):
    return render(request, 'films/confirmation.html')
