"""HipoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from recipes.views import recipe_detail, index, NewRecipe, like_recipe, rate_recipe, search, UpdateRecipe, ingredient, DeleteRecipe
from django.urls import path, include
from users.views import SignUp
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),
    path('search/', search, name='search'),
    path('new_recipe/', login_required(NewRecipe.as_view()), name='new_recipe'),
    path('update_recipe/<int:pk>/', login_required(UpdateRecipe.as_view()), name='update_recipe'),
    path('delete_recipe/<int:pk>/', login_required(DeleteRecipe.as_view()), name='delete_recipe'),
    path('like_recipe/<int:pk>/', like_recipe, name="like_recipe"),
    path('rate_recipe/<int:pk>/', rate_recipe, name="rate_recipe"),
    path('ingredient/<str:ingredient_value>/', ingredient, name='ingredient'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
