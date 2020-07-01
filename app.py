from models.blog import Blog
from database import Database
import pprint


Database.initialize()

myBlog = Blog(author='demoAuthor', description='This is DemoAuthor\'s blog', title='Demo\'s Blog')
myBlog.save_to_mongo()
myBlog.new_post()

print("Your blog is: ", Blog.from_mongo(myBlog.json().get('id')).json(), end='\n\n')

for post in myBlog.get_posts():
    print(pprint.pprint(post))