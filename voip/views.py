from django.db import transaction
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render
from django.http import HttpResponseRedirect

from voip.models import members, extensions, sip, astrt_sipusers
from voip.forms import ExtensionEditForm, SipuserEditForm

import logging
#logger = logging.getLogger(__name__)
logger = logging.getLogger('django.request')

import random
def pwgen(size=16):
    str = []
    chars = 'abcdefghkpqrstxyzACEFHJKLPRTXY3479'
    for k in range(1, size+1):
        str.append(random.choice(chars))
    str = "".join(str)
    return str

@login_required
def index(request):
    logger.debug('index accessed from %s by %s' % (request.META.get('REMOTE_ADDR'),request.user.username) )
    member = members.objects.get(nickname=request.user.username)
    context = {'request': request, 'member': member}
    return render(request, 'voip/index.html', context)

@login_required
def userinfo(request):
    logger.debug('userinfo accessed from %s by %s' % (request.META.get('REMOTE_ADDR'),request.user.username) )
    member = members.objects.get(nickname=request.user.username)
    context = {'request': request, 'member': member}
    return render(request, 'voip/userinfo.html', context)

@login_required
def phonebook(request):
    logger.debug('phonebook accessed from %s by %s' % (request.META.get('REMOTE_ADDR'),request.user.username) )
    member = members.objects.get(nickname=request.user.username)
    extension_list = extensions.objects.filter(phonebook=True).order_by('extension')
    context = {'request': request, 'member': member, 'extension_list': extension_list}
    return render(request, 'voip/phonebook.html', context)

@login_required
def extensions_show(request):
    logger.debug('extension_show accessed from %s by %s' % (request.META.get('REMOTE_ADDR'),request.user.username) )
    member = members.objects.get(nickname=request.user.username)
    extension_list = extensions.objects.filter(id_members=member.id).order_by('extension')
    context = {'request': request, 'member': member, 'extension_list': extension_list}
    return render(request, 'voip/extensions.html', context)

@login_required
def extension_add(request):
    logger.debug('extension_add accessed from %s by %s' % (request.META.get('REMOTE_ADDR'),request.user.username) )
    member = members.objects.get(nickname=request.user.username)
    if request.method == 'POST':
        form = ExtensionEditForm(request.POST)
        if form.is_valid():
            from datetime import datetime
            now = datetime.now()
            last_month = datetime(now.year, now.month-1, 1, 0, 0, 0)
            #extension1 = extensions.objects.filter(id_members=None).filter(changed__lt=last_month)[0]
            #extension = extensions.objects.filter(id_members=None).order_by('extension')[5]
            extension = extensions.objects.filter(id_members=None).order_by('extension')[5]
            extension.id_members = members.objects.get(nickname=request.user.username)
            extension.voicemail = form.cleaned_data['voicemail']
            extension.voicemail_pin = form.cleaned_data['voicemail_pin']
            extension.voicemail_delay = form.cleaned_data['voicemail_delay']
            extension.voicemail_emailnotify = form.cleaned_data['voicemail_emailnotify']
            extension.phonebook = form.cleaned_data['phonebook']
            extension.save()
            return HttpResponseRedirect('/extensions/')
    else:
        form = ExtensionEditForm()
    context = {'request': request, 'member': member, 'form': form}
    return render(request, 'voip/extension_edit.html', context)

@login_required
def extension_edit(request, extension_id):
    logger.debug('extension_edit accessed from %s by %s' % (request.META.get('REMOTE_ADDR'),request.user.username) )
    member = members.objects.get(nickname=request.user.username)
    extension = extensions.objects.get(id=extension_id)
    if request.method == 'POST':
        form = ExtensionEditForm(request.POST)
        if form.is_valid():
            extension.voicemail = form.cleaned_data['voicemail']
            extension.voicemail_pin = form.cleaned_data['voicemail_pin']
            extension.voicemail_delay = form.cleaned_data['voicemail_delay']
            extension.voicemail_emailnotify = form.cleaned_data['voicemail_emailnotify']
            extension.phonebook = form.cleaned_data['phonebook']
            extension.save()
            return HttpResponseRedirect('/extensions/')
    else:
        form = ExtensionEditForm(initial={
            'voicemail': extension.voicemail,
            'voicemail_pin': extension.voicemail_pin,
            'voicemail_delay': extension.voicemail_delay,
            'voicemail_emailnotify': extension.voicemail_emailnotify,
        })
    extension_list = extensions.objects.filter(id_members=member.id).order_by('extension')
    context = {'request': request, 'member': member, 'extension': extension, 'extension_list': extension_list, 'form': form}
    return render(request, 'voip/extension_edit.html', context)

@login_required
def extension_delete(request, extension_id):
    extension = extensions.objects.get(id=extension_id)
    logger.debug('extension_delete(%s) accessed from %s by %s' % (extension.extension,request.META.get('REMOTE_ADDR'),request.user.username) )
    extension = extensions.objects.get(id=extension_id)
    if not extension.astrt_sipusers_set.exists():
        extension.id_members = None
        extension.voicemail = False
        extension.voicemail_pin = "1234"
        extension.voicemail_delay = 15
        extension.emailnotify = False
        extension.phonebook = False
        extension.save()
    return HttpResponseRedirect('/extensions/')

@login_required
@transaction.commit_manually
def sipuser_add(request, extension_id):
    logger.debug('sipuser_add accessed from %s by %s' % (request.META.get('REMOTE_ADDR'),request.user.username) )
    extension = extensions.objects.get(id=extension_id)
    nickname = request.user.username
    from django.db import connection
    cursor = connection.cursor()
    secret = pwgen()
    cursor.execute("SELECT func_create_sipuser('%s','%s',%s)" % (nickname,secret,extension_id) )
    ret = cursor.fetchone()
    logger.debug("extension_id: %s - stored procedure 'func_create_sipuser' returned: %s" % (extension_id,ret) )
    pin = 1234
    timeout = 15
    cursor.execute("SELECT func_create_voicemail_from_phonenumberid(%s,'%s',%s)" % (extension_id, pin, timeout) )
    ret = cursor.fetchone()
    logger.debug("stored procedure 'func_create_voicemail' returned: %s" % ret)
    cursor.close() # is this needed and/or on the right position called?
    connection.commit()
    return HttpResponseRedirect('/extensions/')

@login_required
def sipuser_edit(request, sipuser_id):
    logger.debug('sipuser_edit accessed from %s by %s' % (request.META.get('REMOTE_ADDR'),request.user.username) )
    member = members.objects.get(nickname=request.user.username)
    sipuser = astrt_sipusers.objects.get(id=sipuser_id)
    if request.method == 'POST':
        form = SipuserEditForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['reset_pw']:
                sipuser.secret = pwgen()
            else:
                sipuser.secret = sipuser.secret
            if not form.cleaned_data['nat']:
                sipuser.nat = 'no'
            else:
                sipuser.nat = 'force_rport,comedia'
            sipuser.dtmfmode = form.cleaned_data['dtmfmode']
            sipuser.save()
            return HttpResponseRedirect('/extensions/')
    else:
        form = SipuserEditForm(initial={
            'secret': sipuser.secret,
            'nat': sipuser.nat,
            'dtmfmode': sipuser.dtmfmode,
        })
    context = {'request': request, 'member': member, 'sipuser': sipuser, 'form': form}
    return render(request, 'voip/sipuser_edit.html', context)

@login_required
def sipuser_delete(request, sipuser_id):
    logger.debug('sipuser_delete(%s) accessed from %s by %s' % (sipuser_id,request.META.get('REMOTE_ADDR'),request.user.username) )
    sipuser = astrt_sipusers.objects.get(id=sipuser_id)
    sipuser.delete()
    return HttpResponseRedirect('/extensions/')

# old code, will be deleted soon
def index_old(request):
    c = {}
    c.update(csrf(request))
    state = "Please log in below..."
    username = password = ''
    if request.GET.get('id_members'):
      u = members.objects.get(id=request.GET.get('id_members'))
      username = u.nickname
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        logger.debug("user tries to log in: %s" % username)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
          logger.debug("user authenticated: %s" % user.username)
          if user.is_active:
              auth.login(request, user)
              logger.debug("user logged in: %s" % user.username)
              #extension_list = extensions.objects.filter(id_members="150").order_by('extension')
              member = members.objects.get(nickname=user.username)
              extension_list = extensions.objects.filter(id_members=member.id).order_by('extension')
              context = {'extension_list': extension_list}
              return render(request, 'voip/extensions.html', context)
          else:
              state = "Your account is not active, please contact the site admin."
        else:
          state = "Your username and/or password were incorrect."

    #return render_to_response('voip/index.html',{'c':c, 'state':state, 'username': username})
    return render(request, 'voip/index.html',{'c':c, 'state':state, 'username': username})

