# -*- coding: utf-8 -*-
from django import forms
from seguimiento.models import *

class formDocumento(forms.ModelForm):
    class Meta:
        model = Documento
    def is_valid(self):
        return True

class formPase(forms.ModelForm):
    class Meta:
        model = Pase
    def is_valid(self):
        return True
