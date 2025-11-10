from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class LifestyleView(TemplateView):
    template_name = "lifestyle.html"

class SocietyView(TemplateView):
    template_name = "society.html"

class CitizenView(TemplateView):
    template_name = "citizen.html"

class CommunityView(TemplateView):
    template_name = "community.html"

class EmotionalView(TemplateView):
    template_name = "emotional.html"

class HealthView(TemplateView):
    template_name = "health.html"

class LocalView(TemplateView):
    template_name = "local.html"


