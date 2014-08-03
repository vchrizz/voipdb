from django import forms

class ExtensionEditForm(forms.Form):
    voicemail = forms.BooleanField(label='Voicemail', required=False)
    voicemail_pin = forms.CharField(label='Voicemail PIN', min_length=4, max_length=4)
    voicemail_delay = forms.IntegerField(label='Voicemail Delay', min_value=1, max_value=999)
    voicemail_emailnotify = forms.BooleanField(label='E-Mail Notify', required=False)
    phonebook = forms.BooleanField(label='Telefonbuch', required=False)

class SipuserEditForm(forms.Form):
    reset_pw = forms.BooleanField(label='Reset Password', required=False, )
    #secret = forms.CharField(label='secret', min_length=16, max_length=16)
    nat = forms.BooleanField(label='NAT', required=False, )
    #nat = forms.CheckboxInput(check_test)
    CHOICES = (
        ('auto', 'Auto'),
        ('inband', 'Inband'),
        ('rfc2833', 'RFC2833'),
        ('info','INFO'),
    )
    dtmfmode = forms.ChoiceField(choices=CHOICES, required=True, label='DTMF Mode')
#    def __init__(self):
#        self.fields['voicemail'].initial  = True

#class sipForm(forms.ModelForm):
#    nat = forms.BooleanField(label='NAT', required=False)
#    class Meta:
#        model = sip
