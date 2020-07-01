# CLI Blog

This is a very basic blogging model implementation with interface at CLI level.

Users can create blogs, and create posts in their blogs and also read the same from database.

MongoDB is used for as a database in this project.

```
Dependencies for this project:
- pymongo
- prettytable
```

To install dependencies issue the following command
```
pip install -r requirements.txt
```
Before running this app, make sure you have mongoDB installed on your PC.
<br>

In case you wish to change the database name or collections names, same should be done in **constants.py**.
<br>

To run the project:
1. clone the repository locally
2. install the dependencies using requirements.txt (steps mentioned above)
3. open terminal/cmd and cd into the project home directory
4. issue command `python app.py`
