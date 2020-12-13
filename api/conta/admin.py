from django.contrib import admin

from conta.models import *

# Register your models here.
admin.site.register(Conta)
admin.site.register(ContaCorrente)
admin.site.register(ContaInvestimento)
admin.site.register(TipoInvestimento)
admin.site.register(Investimento)
admin.site.register(CartaoConta)