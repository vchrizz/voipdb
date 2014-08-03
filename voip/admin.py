from django.contrib import admin
from voip.models import members,extensions,sip

class MembersAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'firstname', 'lastname', 'street', 'housenumber', 'zip', 'town', 'mobilephone', 'email', 'homepage', ]
    list_filter = ['town', ]

class ExtensionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'extension', 'potsnumber', 'voicemail', 'voicemail_pin', 'voicemail_delay', 'phonebook', ]
    list_filter = ['voicemail', 'phonebook', ]

class SipAdmin(admin.ModelAdmin):
    list_display = ['id', 'nat', 'dtmfmode', 'port', 'provider', 'provider_host', 'calleridnum', 'calleridtext', ]
    list_filter = ['nat', ]

admin.site.register(members, MembersAdmin)
admin.site.register(extensions, ExtensionsAdmin)
admin.site.register(sip, SipAdmin)
