from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index_file.html'
