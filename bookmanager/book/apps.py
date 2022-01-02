from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'
    # 配置在 admin 站点中的当前应用的标题名
    verbose_name = 'Book Manager'
