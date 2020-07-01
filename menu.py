from database import Database
import constants
from models.blog import Blog
from prettytable import PrettyTable
from models.post import Post


class Menu(object):

    def __init__(self):
        self.user = input(
            "Enter your author name (this name is case sensitive and will be used to access your blog and it's posts): "
        )
        self._account = self._user_has_account()
        if self._account is not None:
            self._blog = self._account
            print("Welcome back {}.".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        return Database.find_one(collection=constants.BLOG_COLLECTION, query={'author': self.user})

    def _prompt_user_for_account(self):
        print("\nSeems you do not have an associated account, let's on board you by creating a new blog.")
        title = input("Enter a title for your Blog: ")
        description = input("Enter description for your Blog: ")
        self._blog = Blog(
            author=self.user,
            description=description,
            title=title
        )
        self._blog.save_to_mongo()
        self._blog = self._blog.json()
        print("[+] Successfully created!!")

    def run_menu(self):
        row = input("Do you wish to read (R) or write (W) the blogs? (R/W) :")
        if row.upper() == 'R':
            print('Choose a blog:')
            table = PrettyTable(['S.No', 'Blog Title'])
            blog_map = {}
            for i, b in enumerate([d for d in Database.find(collection=constants.BLOG_COLLECTION, query={})]):
                table.add_row([i+1, b.get('title')])
                blog_map.setdefault(i + 1, b)
            print(table)
            user_selection = input('Enter your selection(S.No.): ')
            try:
                user_selection = int(user_selection)
                if user_selection > len(blog_map):
                    int('a')
                selected_blog = blog_map.get(user_selection)
                blog_posts = Post.from_blog(selected_blog.get('id'))
                post_table = PrettyTable(['id', 'title', 'content', 'author', 'created_at'])
                for i, post in enumerate(blog_posts):
                    post_table.add_row(
                        [
                            post.get('id'),
                            post.get('title'),
                            post.get('content'),
                            post.get('author'),
                            post.get('created_at'),
                        ]
                    )
                print("\nPrinting all POSTS for BLOG <{}>".format(selected_blog.get('title')), end="\n")
                print(post_table)
            except ValueError:
                print("Invalid value detected, aborting...")
        elif row.upper() == 'W':
            Blog(author=self._blog).new_post()
            pass
        else:
            print("Thank you for blogging with us!")
