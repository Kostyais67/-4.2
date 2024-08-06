u1 = User.objects.create_user(username='Kostya')

u2 = User.objects.create_user(username='Rushi')

Author.objects.create(authorUser=u1)

Author.objects.create(authorUser=u2)

Category.objects.create(name='IT')

Category.objects.create(name='games')

Category.objects.create(name='animals')

Category.objects.create(name='nature')

author = Author.objects.get(id=1)

Post.objects.create(author=author, categoryType='NW', title='sometitle', text='somebigtext')

author = Author.objects.get(id=2)

Post.objects.create(author=author, categoryType='AR', title='sometitle', text='somebigtext')

Post.objects.create(author=author, categoryType='AR', title='sometitle', text='somebigtext')

Post.objects.get(id=1).postCotegory.add(Category.objects.get(id=1))

Post.objects.get(id=1).postCotegory.add(Category.objects.get(id=2))

Post.objects.get(id=2).postCotegory.add(Category.objects.get(id=1))

Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='111')

Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='222')

Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).authorUser, text='333')

Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).authorUser, text='444')

Comment.objects.get(id=1).like()

Comment.objects.get(id=2).dislike()

Comment.objects.get(id=2).dislike()

Comment.objects.get(id=1).rating

Comment.objects.get(id=2).rating

Author.objects.get(id=1)

a = Author.objects.get(id=1)

a.update_rating()

a.ratingAuthor

Author.objects.get(id=2)

b = Author.objects.get(id=2)

b.update_rating()

b.ratingAuthor

for i in a:
...     i.ratingAythor
...     i.authorUser.username