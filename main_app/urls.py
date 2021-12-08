from django.urls import path
from .views import Home, SignUp, ProfileDetail, PortfolioCreate, PortfolioDetail, PortfolioUpdate, PortfolioDelete, StockCreate, StockDelete, PortfolioAnalyze, PlotView, PlotMonte
from .views import PlotChart

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/signup/', SignUp.as_view(), name='signup'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    
    # PORTFOLIOS
    path('portfolios/new', PortfolioCreate.as_view(), name='portfolio_create'),
    path('portfolios/<int:pk>/', PortfolioDetail.as_view(), name='portfolio_detail'),
    path('portfolios/<int:pk>/update/', PortfolioUpdate.as_view(), name='portfolio_update'),
    path('portfolios/<int:pk>/delete/', PortfolioDelete.as_view(), name='portfolio_delete'),
    path('portfolios/<int:pk>/analyze/', PortfolioAnalyze.as_view(), name='portfolio_analyze'),

    # Plot Chart
    path('plot/', PlotMonte, name='plot'),
    # path('portfolios/<int:pk>/analyze/', PlotView.as_view(), name='portfolio_analyze'),
    

    # STOCKS
    path('portfolios/<int:pk>/new', StockCreate.as_view(), name='stock_create'),
    path('portfolios/<int:pk>/stock/<int:stock_pk>/', StockDelete.as_view(), name='stock_delete'),
]


# Obsolted Paths
# from .views import ProfileUpdate, PortfolioList
# path('portfolios/', PortfolioList.as_view(), name='portfolio_list'),
# path('profiles/<int:pk>/update', ProfileUpdate.as_view(), name='profile_update'),