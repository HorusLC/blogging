# if __name__=='__main__':
#     idgen = UuidGenerator()
#         blogger_repo = BloggerRepository(idgen, 'bloggers2.json')
#         blog_repo = JsonRepository(idgen, 'blogs.json')
#         blogger = Blogger('Dess', 'Kos', 'dkk', '123', '11', 'M', 'dao@abv.bg', '12-11-2021', 'Blogger', [], [], [],
#                           '10-1-2022', 'hi')
#
#         blogger = blogger_repo.create(blogger)
#         blogger_repo.save()
#         blog1 = Blog('IT infrastructure', 'Just another avg IT blog', '1-10-2021', '2-3-2022',
#                                  'it, programming, python',
#                                  'Education', blogger.id_)
#         blog1 = blog_repo.create(blog1)
#         blogger.blogs_created.append(blog1)
#         blogger_repo.update(blogger)
#         blogger_repo.save()
#
#         # blogger_repo.create(b1)
#         # blogger_repo.save()
#         blogger_repo.load()
#         for blogger in blogger_repo.find_all():
#             print(blogger)
#             for blog in blogger.blogs_created:
#                 print(blog.title)
#         # idgen = UuidGenerator()
#         # user_repo = BloggerRepository(idgen)
#         # b1 = Blogger('Dess', 'Kos', 'dkk', '123', '11', 'M', 'dao@abv.bg', '12-11-2021', 'Blogger', [], [], [],
#         #              '10-1-2022', 'hi')
#         # b2 = Blogger('Pancho', 'Panchev', 'pepino21', '1234', '1534', 'M', 'pao@abv.bg', '12-11-2021', 'Blogger', [],
#         #              [], [],
#         #              '9-1-2022', 'hi there')
#         # b3 = Blogger('Sancho', 'Sanchev', 'sanchez2', '12345', '1535', 'M', 'sanchoo@abv.bg', '10-11-2021', 'Blogger', [],
#         #              [], [],
#         #              '9-1-2022', 'hi there')
#         # user_repo.create(b1)
#         # user_repo.create(b2)
#         # user_repo.create(b3)
#         #
#         # for u in user_repo.find_all():
#         #     print(f'{u} with id: {u.id_}')
#         #
#         # u_email = user_repo.find_by_email('pao8@abv.bg')
#         # print(u_email)
#         #
#         # blog_repo = Repository(idgen)
#         #
#         # blog1 = entity.blog.Blog('IT infrastructure', 'Just another avg IT blog', '1-10-2021', '2-3-2022',
#         #                          'it, programming, python',
#         #                          'Education', 0, b1, [])
#         #
#         # blog2 = entity.blog.Blog('Cooking at its finest', 'Im a Michellin star Chef', '1-11-2021', '1-3-2022',
#         #                          'cooking,food',
#         #                          'Cooking', 0, b2, [])
#         #
#         # blog_repo.create(blog1)
#         # blog_repo.create(blog2)
#         # b1.blogs_created.append(blog1)
#         # b2.blogs_created.append(blog2)
#         # user_repo.update(b1)
#         # user_repo.update(b2)
#         #
#         # for blog in blog_repo.find_all():
#         #     print(blog)
#         #
#         # post1 = entity.post.Post('Machine Learning basics', 'Today we will talk about the basics of Neural Networks..',
#         #                          '1 - 2 - 2022', '1 - 2 - 2022', 'NeuralNets,DL', None, blog1, [])
#         #
#         # post2 = entity.post.Post('Cook the best pork steak!', 'Today we will talk about grilling the perfect stake..',
#         #                          '1 - 2 - 2022', '1 - 2 - 2022', 'NeuralNets,DL', None, blog2, [])
#         # posts_repo = Repository(idgen)
#         # posts_repo.create(post1)
#         # posts_repo.create(post2)
#         #
#         # blog1.posts.append(post1)
#         # blog2.posts.append(post2)
#         # blog_repo.update(blog1)
#         # blog_repo.update(blog2)
#         # print()
#         # for blog in blog_repo.find_all():
#         #     print('Posts in - ', blog)
#         #     for p in blog.posts:
#         #         print(p)
#         #     print()
#         #
#         # comment1 = Comment('Best post so far!', '2-1-2022', post1, author=b1)
#         # comment2 = Comment('Great content!', '2-3-2022', post2, author=b3)
#         # comment_repo = Repository(idgen)
#         # comment_repo.create(comment1)
#         # comment_repo.create(comment2)
#         #
#         # post1.comments.append(comment1)
#         # post2.comments.append(comment2)
#         # posts_repo.update(post1)
#         # posts_repo.update(post2)
#         #
#         # b1.comments_made.append(comment1)
#         # b3.comments_made.append(comment2)
#         # user_repo.update(b1)
#         # user_repo.update(b3)
#         #
#         # for blog in blog_repo.find_all():
#         #     print('Posts in : ', blog)
#         #     for p in blog.posts:
#         #         print(p)
#         #         print('With these comments:')
#         #         for c in p.comments:
#         #             print(f'{c.author.username}: {c.text}')
#         #             print()
#         #
#         #     print()
#         # user_repo.delete_by_id(b1.id_)  # 'on delete cascade' will be implemented in the actual application
