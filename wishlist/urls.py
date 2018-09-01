from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views
from wishlist import endpoints

urlpatterns = [
    # Django rest framework style (not in use)
    path('wishlists/', views.WishListCreate.as_view()),
    path('wishlists_items/', views.WishListItemCreate.as_view()),

    # path('wishlist', endpoints.WishListViewSet),

    # WISHLIST API
    # Get a specific wishlist with wishlistId
    path('wishlist/get/<int:wish_list_id>', views.get_wish_list_items),
    # Get all wishlists owned by userId passed in
    path('wishlist/get_all/<int:user_id>', views.get_wish_lists_by_user),
    # If no user ID is passed in, return all wishlist title + ids
    path('wishlist/get_all', views.get_all_wish_lists),
    # Make a new wishlist owned by userId passed in
    path('wishlist/new/<int:user_id>', views.new_wish_list),
    # Update wishlist with wishlistId
    path('wishlist/update/<int:wish_list_id>', views.update_wish_list),
    # Delete wishlist with wishlistId
    path('wishlist/delete/<int:wish_list_id>', views.remove_wish_list),
    # TODO: PLEDGE API
]
