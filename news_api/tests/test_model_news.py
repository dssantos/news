from django.test import TestCase
from news_api.models import News
from news_api.models import UserProfile


class NewsModelTest(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(
            name='Tim Peters', 
			email='tim@mail.com', 
			password='1'
        )
        self.obj = News(
            title='Zen of Python',
            author=self.user,
			text='''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(News.objects.exists())
