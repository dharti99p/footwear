from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import *
# Create your views here.


# about
def about(request):
    image = About.objects.last()
    return render(request, 'about.html', {'image': image})


# add_to_wishlist
def add_to_wishlist(request):
    shopmore = ShopMore.objects.all()
    pro_detail = ProDetail.objects.all()
    return render(request, 'add-to-wishlist.html', {'shopmore': shopmore, 'pro_detail': pro_detail})


def admin_dashboard(request):
    show_menu_table = False
    show_badge_table = False
    data = None
    if request.method == "POST" and request.POST.get('show_menu_table'):
        show_menu_table = True
        data = MenuForm.objects.all()   
    elif request.method == "POST" and request.POST.get('show_badge_table'):
        show_badge_table = True
        data = BadgeMenu.objects.all()
    return render(request, 'admin-dashboard.html', {'show_menu_table': show_menu_table, 'data': data, 'show_badge_table': show_badge_table})


def badge(request):
    if request.method == 'POST':
        badge = request.POST.get('badge')
        print(badge)

        if BadgeMenu.objects.filter(badge=badge).exists():
            return render(request, 'badge.html', {'error': 'Badge Name already exists.'})

        data = BadgeMenu(badge=badge)
        data.save()

        return redirect('badge-table')
    return render(request, 'badge.html')


def badge_table(request):
    data = BadgeMenu.objects.all()
    return render(request, 'badge_table.html', {'data': data})


def badge_edit(request, id):
    data = BadgeMenu.objects.get(id=id)
    if request.method == 'POST':
        data.badge = request.POST.get('badge')
        print(data.badge)

        data.save()
        data = BadgeMenu.objects.all()
        return render(request, 'badge_table.html', {'data': data})
    return render(request, 'badge_edit.html', {'data': data})


def badge_delete(request, id):
    BadgeMenu.objects.get(id=id).delete()
    data = BadgeMenu.objects.all()
    return render(request, 'badge_table.html', {'data': data})


def cart(request):
    pro_detail = ProDetail.objects.all()
    shopmore = ShopMore.objects.all()
    
    subtotal = sum(i.total for i in pro_detail)

    delivery = 0.00
    discount = 45.00

    total = subtotal + delivery - discount

    context = {
        'pro_detail': pro_detail,
        'shopmore' : shopmore,
        'subtotal' : subtotal,
        'delivery' : delivery,
        'discount' : discount,
        'total' : total
        }
    return render(request, 'cart.html', context)


def checkout(request):
    pro_detail = ProDetail.objects.all()
    
    subtotal = sum(i.total for i in pro_detail)

    delivery = 0.00
    discount = 45.00

    total = subtotal + delivery - discount

    context = {
        'pro_detail': pro_detail,
        'subtotal' : subtotal,
        'delivery' : delivery,
        'discount' : discount,
        'total' : total
        }
    return render(request, 'checkout.html', context)


def contact(request):
    contactus = ContactUs.objects.last()

    context = {
        'contactus' : contactus
    }
    return render(request, 'contact.html', context)


def forgot_password(request):
    return render(request, 'forgot-password.html')


def header(request):
    menu_items = MenuForm.objects.all()
    data = BadgeMenu.objects.all()

    context = {'menu_items': menu_items, 'data': data}

    return context


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # if not LogIn.objects.filter(username=username).exists() :
        #     return render(request,'login.html', context={'error': f"Invalid username !"})
        obj = authenticate(username=username, password=password)
        if obj:
            return render(request, 'admin-dashboard.html')
        else:
            return render(request, template_name='login.html', context={'error': f"Invalid username and password"})
    return render(request, 'login.html')


def men(request):
    return render(request, 'men.html')


def menu_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')

        print(title, url)
        if MenuForm.objects.filter(title=title).exists():
            return render(request, 'menu-form.html', {'error': 'Title already exists.'})

        if MenuForm.objects.filter(url=url).exists():
            return render(request, 'menu-form.html', {'error': 'URL already exists.'})

        data = MenuForm(title=title, url=url)
        data.save()
        
        return redirect('admin-dashboard')
    return render(request, 'menu-form.html')


def menu_table(request):
    data = MenuForm.objects.all()
    return render(request, 'menu-table.html', {'data': data})


def menu_edit(request, id):
    data = MenuForm.objects.get(id=id)
    if request.method == 'POST':
        data.title = request.POST.get('title')
        data.url = request.POST.get('url')
        data.save()
        data = MenuForm.objects.all()
        return render(request, 'admin-dashboard.html', {'data': data})
    return render(request, 'menu_edit.html', {'data': data})


def menu_delete(request, id):
    MenuForm.objects.get(id=id).delete()
    data = MenuForm.objects.all()
    return render(request, template_name='admin-dashboard.html', context={'data': data})


def order_complete(request):
    return render(request, 'order-complete.html')


def product_detail(request):
    return render(request, 'product-detail.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        print(username, phone_number, email, password, confirm_password)
        if Register.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists.'})

        if Register.objects.filter(phone_number=phone_number).exists():
            return render(request, 'register.html', {'error': 'Phone number already exists.'})

        if Register.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'email already exists.'})

        if password == confirm_password:
            data = Register(username=username, phone_number=phone_number, email=email, password=password, confirm_password=confirm_password)
            data.save()
            return redirect('user-dashboard')
        else:
            return render(request, template_name='register.html', context={'error': f"password not match"})
    return render(request, 'register.html')


def submenu(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        url = request.POST.get('url')
        menu_form_id = request.POST.get('menu_form')

        if not(name and url and menu_form_id):
            return render(request, 'subform.html')

        try:
            menu_form = MenuForm.objects.get(pk=menu_form_id)
        except MenuForm.DoesNotExist:
            return render(request, 'submenu.html')

        submenu = SubMenu(name=name, url=url, menu_form=menu_form)
        submenu.save()
        return redirect('admin-dashboard')

    else:
        menu_forms = MenuForm.objects.all()
        return render(request, 'submenu.html', {'menu_forms': menu_forms})


def user_dashboard(request):
    return render(request, 'user-dashboard.html')


def women(request):
    return render(request, 'women.html')
