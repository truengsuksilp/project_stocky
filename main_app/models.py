from django.db.models import Model, OneToOneField, CASCADE, CharField, ForeignKey, TextField, DateTimeField, SlugField, DateField, IntegerField, DecimalField

from django.contrib.auth.models import User

# Create your models here.
class Portfolio (Model):
    user = ForeignKey(User, on_delete=CASCADE, default='no_login', related_name="portfolios")
    name = CharField(max_length=100, default='no_name')
    valuation = IntegerField(default=10000)
    date_of_valuation = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["date_of_valuation"]
    


class Stock (Model):
    portfolio = ForeignKey(Portfolio, on_delete=CASCADE, related_name='stocks')
    ticker = CharField(max_length=5)
    price = DecimalField(max_digits=10, decimal_places=2)
    date_of_valuation = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticker

# Extends user model as needed (e.g., location, bio)

# NOTE: ForeignKey referencing - related_names
    # related_name: portfolios -> users.portfolio
    # related_name: stocks -> portfolio.stocks.all() 🙂 