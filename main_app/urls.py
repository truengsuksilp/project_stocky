from django.urls import path
from .views import Home, SignUp, ProfileDetail, PortfolioList, PortfolioDetail, PortfolioCreate, PortfolioUpdate, StockCreate
# from .views import ProfileUpdate

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/signup/', SignUp.as_view(), name='signup'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile'),
    # path('profiles/<int:pk>/update', ProfileUpdate.as_view(), name='profile_update'),
    path('portfolios/', PortfolioList.as_view(), name='portfolio_list'),
    path('portfolios/new', PortfolioCreate.as_view(), name='portfolio_create'),
    path('portfolios/<int:pk>/', PortfolioDetail.as_view(), name='portfolio_detail'),
    path('portfolios/<int:pk>/new', StockCreate.as_view(), name='stock_create'),
    path('portfolios/<int:pk>/update/', PortfolioUpdate.as_view(), name='portfolio_update'),
]