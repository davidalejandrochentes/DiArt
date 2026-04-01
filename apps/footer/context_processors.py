from .models import Footer, SocialLink


def footer_context(request):
    footer = Footer.objects.first()
    social_links = SocialLink.objects.filter(activo=True)
    return {
        "footer": footer,
        "social_links": social_links,
    }
