from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # Other fields here
    dn = models.CharField(max_length=254)
    uid = models.CharField(max_length=254)
    cn = models.CharField(max_length=254)
    sn = models.CharField(max_length=254)
    givenName = models.CharField(max_length=254)
    userPassword = models.CharField(max_length=254)
    shadowLastChange = models.IntegerField(null=True)
    shadowMax = models.IntegerField(null=True)
    shadowWarning = models.IntegerField(null=True)
    loginShell = models.CharField(max_length=254)
    uidNumber = models.IntegerField(null=True)
    gidNumber = models.IntegerField(null=True)
    homeDirectory = models.CharField(max_length=254)
    gecos = models.CharField(max_length=254)
    mail = models.EmailField(max_length=254)
    l = models.CharField(max_length=254)
    telephoneNumber = models.CharField(max_length=254)

def create_user_profile(sender, instance, created, **kwargs):
    #if created:
    #    UserProfile.objects.create(user=instance)
    UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

class members(models.Model):
    # First things first - wherever you have a model with a primary key named "id", just delete it.
    # Django already assumes that your table has an "id" column and defaults to an automatic primary key field - you don't need to define it in the class.
    # id = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=255)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    street = models.CharField(max_length=255)
    housenumber = models.CharField(max_length=10)
    zip = models.CharField(max_length=10)
    town = models.CharField(max_length=255)
    telephone = models.CharField(max_length=25)
    mobilephone = models.CharField(max_length=25)
    fax = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    homepage = models.CharField(max_length=50)
    created = models.DateTimeField('date created')
    changed = models.DateTimeField('date changed')
    mentor_id = models.IntegerField(default=0)
    instant_messenger_nick = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s' % (self.nickname)
    def check_password(self, password):
        return True
    class Meta:
        db_table = "members"
        verbose_name = "member"
        verbose_name_plural = "members"

class extensions(models.Model):
    # First things first - wherever you have a model with a primary key named "id", just delete it.
    # Django already assumes that your table has an "id" column and defaults to an automatic primary key field - you don't need to define it in the class.
    # id = models.IntegerField(primary_key=True)
    extension = models.CharField(max_length=10,unique=True)
    potsnumber = models.CharField(max_length=50,unique=True)
    voicemail = models.BooleanField(default=False)
    voicemail_pin = models.CharField(max_length=4,null=True)
    voicemail_emailnotify = models.BooleanField(default=False)
    voicemail_emailnotify_attach = models.BooleanField(default=False)
    voicemail_delay = models.IntegerField(default=15)
    voicemail_emailnotify = models.BooleanField(default=False)
    meetme = models.BooleanField(default=False)
    meetme_pin = models.CharField(max_length=4,null=True)
    meetme_admin_pin = models.CharField(max_length=4,null=True)
    h323 = models.NullBooleanField(default=False)
    h323_ip = models.CharField(max_length=15,null=True)
    phonebook = models.NullBooleanField(default=True)
    id_members = models.ForeignKey(members,null=True,db_column="id_members")
    redirect_delay = models.IntegerField(default=0,null=True)
    redirect_target = models.CharField(max_length=32,null=True)
    redirect = models.BooleanField(default=False)
    fax = models.BooleanField(default=False)
    fax_email = models.CharField(max_length=100,null=True)
    created = models.DateTimeField('date created')
    changed = models.DateTimeField('date changed')
    def __unicode__(self):
        return u'%s' % (self.extension)
    class Meta:
        verbose_name = "extension"
        verbose_name_plural = "extensions"
#    def save(self):
#        if not self.id:
#            self.voicemail = self.voicemail
#            self.voicemail_pin = self.voicemail_pin
#        self.voicemail_delay = self.voicemail_delay
#        super(extensions, self).save()

class sip(models.Model):
    # First things first - wherever you have a model with a primary key named "id", just delete it.
    # Django already assumes that your table has an "id" column and defaults to an automatic primary key field - you don't need to define it in the class.
    # id = models.IntegerField(primary_key=True)
    secret = models.CharField(max_length=50)
    nat = models.BooleanField(default=True)
    dtmfmode = models.CharField(max_length=25,null=True,default="rfc2833")
    port = models.IntegerField()
    provider = models.BooleanField(default=False)
    provider_host = models.CharField(max_length=255,null=True)
    provider_fromuser = models.CharField(max_length=255,null=True)
    provider_fromdomain = models.CharField(max_length=255,null=True)
    provider_secret = models.CharField(max_length=50,null=True)
    id_voip_extensions = models.ForeignKey(extensions,null=True,db_column="id_voip_extensions")
    alt_sip_username = models.CharField(max_length=50,null=True)
    alt_accountcode = models.CharField(max_length=200,null=True)
    calleridnum = models.CharField(max_length=32,null=True)
    calleridtext = models.CharField(max_length=50,null=True)
    created = models.DateTimeField('date created')
    changed = models.DateTimeField('date changed')
    def __unicode__(self):
        return u'%s' % (self.id)
    class Meta:
        verbose_name_plural = "sip"
        ordering = ['id']

class astrt_sipusers(models.Model):
    # id = models.IntegerField()
    # Error: One or more models did not validate:
    # voip.astrt_sipusers: "id": You can't use "id" as a field name, because each model automatically gets an "id" field if none of the fields have primary_key=True. You need to either remove/rename your "id" field or add primary_key=True to a field.
    name = models.CharField(max_length=80)
    accountcode = models.CharField(max_length=20, null=True)
    amaflags = models.CharField(max_length=7, null=True)
    callgroup = models.CharField(max_length=10, null=True)
    callerid = models.CharField(max_length=80, null=True)
    canreinvite = models.CharField(max_length=3, default="yes", null=True)
    context = models.CharField(max_length=80, null=True)
    defaultip = models.CharField(max_length=45, null=True)
    dtmfmode = models.CharField(max_length=7, null=True)
    fromuser = models.CharField(max_length=80, null=True)
    fromdomain = models.CharField(max_length=80, null=True)
    host = models.CharField(max_length=31, default="")
    insecure = models.CharField(max_length=4, null=True)
    language = models.CharField(max_length=2, null=True)
    mailbox = models.CharField(max_length=50, null=True)
    md5secret = models.CharField(max_length=80, null=True)
    nat = models.CharField(max_length=29, default="")
    permit = models.CharField(max_length=95, null=True)
    deny = models.CharField(max_length=95, null=True)
    mask = models.CharField(max_length=95, null=True)
    pickupgroup = models.CharField(max_length=10, null=True)
    port = models.CharField(max_length=5, default="")
    qualify = models.CharField(max_length=3, null=True)
    restrictcid = models.CharField(max_length=1, null=True)
    rtptimeout = models.CharField(max_length=3, null=True)
    rtpholdtimeout = models.CharField(max_length=3, null=True)
    secret = models.CharField(max_length=80, null=True)
    type = models.CharField(max_length=10, default="friend") # no max_length defined in db?
    username = models.CharField(max_length=80, default="")
    allow = models.CharField(max_length=200, default="!all,g729,ilbc,gsm,ulaw,alaw", null=True)
    musiconhold = models.CharField(max_length=100, null=True)
    regseconds = models.BigIntegerField(default="0")
    ipaddr = models.CharField(max_length=45, default="")
    regexten = models.CharField(max_length=80, default="")
    cancallforward = models.CharField(max_length=3, default="yes", null=True)
    lastms = models.IntegerField(default=0)
    defaultuser = models.CharField(max_length=80, null=True)
    fullcontact = models.CharField(max_length=160, null=True)
    regserver = models.CharField(max_length=30, null=True)
    useragent = models.CharField(max_length=100, null=True)
    callbackextension = models.CharField(max_length=40, null=True)
    # phonenumberid = models.BigIntegerField()
    phonenumberid = models.ForeignKey(extensions,null=True,db_column="phonenumberid")
    outbound_phonenumberid = models.BigIntegerField(default=1)
    class Meta:
        db_table = "astrt_sipusers"
