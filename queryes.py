import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag
    from django.db.models import Count, Sum

    obj = Entry.objects.filter(author__name__contains='author')
    print(obj)

    obj = Entry.objects.filter(author__authorprofile__city=None)
    print(obj)
    """<QuerySet [<Entry: Знакомство с Парижем>,
    <Entry: Инновации в области виртуальной реальности>]>"""



    obj = Entry.objects.annotate(Count('author'))
    print(obj)

    obj = Entry.objects.annotate(author_count=Count('author')).values('id', 'author_count')
    print(obj)

    obj = Entry.objects.filter(tags__name__in=['Кино', 'Здоровье'])
    print(obj)







