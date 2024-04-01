from django.db.models import Max, Count

from django.shortcuts import render
from django.views import View

from .models import Author, Entry


class TrainView(View):
    def get(self, request):
        # Создайте здесь запросы к БД
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])

        # max_count_entry = Entry.objects.aggregate(max_count_entry=Max(Count('text'))
        self.answer2 = None #Entry.objects.aggregate(max_count_entries=Max(max_count_entry))  # TODO Какой автор имеет наибольшее количество опубликованных статей?

        self.answer3 = Entry.objects.filter(tags__name__in=['Кино', 'Здоровье'])  # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?

        self.answer4 = None  # TODO Сколько авторов женского пола зарегистрировано в системе?
        self.answer5 = None  # TODO Какой процент авторов согласился с правилами при регистрации?
        self.answer6 = None  # TODO Какие авторы имеют стаж от 1 до 5 лет?

        max_age_author = Author.objects.aggregate(max_age_author=Max('age'))
        self.answer7 = Author.objects.filter(age=max_age_author['max_age_author']) #TODO Какой автор имеет наибольший возраст?

        self.answer8 = None  # TODO Сколько авторов указали свой номер телефона?
        self.answer9 = None  # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer10 = None  # TODO Сколько статей написано каждым автором?

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)
