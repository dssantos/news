from news_api.models import UserProfile
from news_api.models import News


# Create users samples
admin = UserProfile.objects.create_user(email='admin@mail.com', name='admin', password='1')
admin.is_superuser=True
admin.is_staff=True
admin.save()

user1 = UserProfile.objects.create_user(email='timpeters@mail.com', name='Tim Peters', password='1')
user1.save()
user2 = UserProfile.objects.create_user(email='henriquebastos@mail.com', name='Henrique Bastos', password='1')
user2.save()

# Create News samples
news1 = News.objects.create(
    title='Zen of Python',
    author=user1,
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
news1.save()

news2 = News.objects.create(
    title='Small Acts Manifesto',
    author=user2,
    text='''Small Acts Make Great Revolutions
We are discovering better ways of building communities by connecting people.

Through this endeavor we have come to value:

Trust - which must be respected and never put at risk;
Dialog - is the way to establish a truly trustful relationship;
Personal Contact - the richest experience, not matched by any media or technology;
Transparency - the mean to maintain a sustainable community;
Diversity - people have many interests, but if you need a label, label yourself as a human;
Self-organization - leaders come and go, but there should be no owners;
Example - that's how you teach, live and learn;
Consistency - things take time, intensity is not always the answer;
Give, give, give! - you'll be impressed by how fast things will come back;
Do it! - as simple as you can, just what is essential to pass it forward.
Together, these elements build the foundation of a Small Act capable of transforming people's lives.'''
)
news2.save()
