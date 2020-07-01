import uuid
from .post import Post
from datetime import datetime
import database


class Blog(object):

    def __init__(self, author, title, description, _id=None):
        self.__id = uuid.uuid4().hex if _id is None else _id
        self.author = author
        self.title = title
        self.description = description
        self.post = None

    def new_post(self):
        title = input("Enter a title for the post: ")
        content = input("Enter some content for the post: ")
        date = input("Enter a date for the post or leave blank for today: ")
        self.post = Post(
            blog_id=self.__id,
            title=title,
            content=content,
            created_at=datetime.strptime(date, '%d%m%Y') if date else datetime.utcnow(),
            author=self.author
        )
        self.post.save_to_mongo()
        return self.post.json()

    def save_to_mongo(self):

        database.Database.insert(collection='blogs',
                                 data=self.json())

    def json(self):
        return {
            'id': self.__id,
            'author': self.author,
            'title': self.title,
            'description': self.description
        }

    @classmethod
    def from_mongo(cls, __i):
        blog = database.Database.find_one(
            collection='blogs',
            query={"id": __i}
        )
        return cls(author=blog.get('author'), title=blog.get('title'), description=blog.get('description'), _id=__i)

    def get_posts(self):
        return Post.from_blog(self.__id)
