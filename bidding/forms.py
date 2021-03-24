from django import forms

from .models import *


class SupplysideCreationForm(forms.ModelForm):
    class Meta:
        model = Supplyside
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['province'].queryset= Province.objects.none()
        self.fields['district'].queryset= District.objects.none()
        self.fields['municipality'].queryset= Municipality.objects.none()
        self.fields['commodity'].queryset = Commodity.objects.none()
        self.fields['seed_type'].queryset = SeedType.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['province'].queryset = Province.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['province'].queryset = self.instance.country.province_set.order_by('name')
        
        if 'province' in self.data:
            try:
                province_id = int(self.data.get('province'))
                self.fields['district'].queryset = District.objects.filter(province_id=province_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.province.district_set.order_by('name')

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['municipality'].queryset = Municipality.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['municipality'].queryset = self.instance.district.municipality_set.order_by('name')

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['commodity'].queryset = Commodity.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['commodity'].queryset = self.instance.category.commodity_set.order_by('name')

        if 'commodity' in self.data:
            try:
                commodity_id = int(self.data.get('commodity'))
                self.fields['seed_type'].queryset = SeedType.objects.filter(commodity_id=commodity_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['seed_type'].queryset = self.instance.commodity.seed_type_set.order_by('name')


class DemandsideCreationForm(forms.ModelForm):
    class Meta:
        model = Demandside
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['province'].queryset= Province.objects.none()
        self.fields['district'].queryset= District.objects.none()
        self.fields['municipality'].queryset= Municipality.objects.none()
        self.fields['commodity'].queryset = Commodity.objects.none()
        self.fields['seed_type'].queryset = SeedType.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['province'].queryset = Province.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['province'].queryset = self.instance.country.province_set.order_by('name')
        
        if 'province' in self.data:
            try:
                province_id = int(self.data.get('province'))
                self.fields['district'].queryset = District.objects.filter(province_id=province_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.province.district_set.order_by('name')

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['municipality'].queryset = Municipality.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['municipality'].queryset = self.instance.district.municipality_set.order_by('name')

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['commodity'].queryset = Commodity.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['commodity'].queryset = self.instance.category.commodity_set.order_by('name')

        if 'commodity' in self.data:
            try:
                commodity_id = int(self.data.get('commodity'))
                self.fields['seed_type'].queryset = SeedType.objects.filter(commodity_id=commodity_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['seed_type'].queryset = self.instance.commodity.seed_type_set.order_by('name')