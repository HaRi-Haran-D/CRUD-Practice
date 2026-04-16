from django.db import models

class ItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    
    # def cheap_items(self):
    #     return self.filter(price__lt=5)
    
    # def expensive_items(self):
    #     return self.filter(price__gt=5)
    
    # def search(self, keyword):
    #     return self.filter(name__icontains=keyword)
