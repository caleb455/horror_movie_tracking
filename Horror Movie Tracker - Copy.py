import json
from BTCInput import *

class Movie():
    
    def __init__(self, title, release_date, personal_rating, tags):
        self.title = title
        self.release_date = release_date
        self.personal_rating = personal_rating
        self.tags = tags
        self.__version = 1

    def __str__(self):
        template = '''Title: {0}
Release Date: {1}
Personal Rating: {2}
Tags: {3}'''
        return template.format(self.title, self.release_date, self.personal_rating, self.tags)
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


    def check_version(self):
        pass

def new_movie():
    print("\nAdd a new movie to your list")
    while True:
        title = read_text("\nEnter the title of the movie: ")
        release_date = read_text("\nEnter the release date (YYYY) of the movie: ")
        personal_rating = read_text("\nEnter your personal rating (#/10) for the movie: ")
        tags = []
        while True:
            enter_tag = read_text("\nEnter a tag or 'cont' to continue: ")
            if enter_tag != 'cont':
                tags.append(enter_tag)
                continue
            elif enter_tag == 'cont':
                print('\nOk')
                break
            else:
                print("Sorry, that is not a viable input.")
                continue
        try:
            new_movie = Movie(title=title,release_date=release_date,personal_rating=personal_rating,tags=tags)
            dict_movie = new_movie.__dict__


        except Exception as e:
            print("\nError: ", e)
        print('\n' )
        print(new_movie)
        while True:
            confirmation = read_text("\nDoes this look good? (y/n) ")
            if confirmation == 'y':
                print("\nOk")
                moviesJSONdata = json.dumps(dict_movie.toJson(), indent=4)
                JSONhorror_movies.append(moviesJSONdata)
                break
            elif confirmation == 'n':
                print("\nOk")
                break
            else:
                print("\nSorry, that is not a viable input.")
                continue
        break
        




def save_movies(file_name):
    print('\nSaved to "horror_movies" file')
    with open (file_name, "w") as output_file:
        json.dumps(JSONhorror_movies, output_file)
   
def load_movies(file_name):
    print('Load "horror_movies" file')
    global JSONhorror_movies
    with open(file_name, 'r') as input_file:
        JSONhorror_movies = json.load(input_file)

def overwrite(file_name):
    with open(file_name, 'w'):
        pass


introduction = '''\nHello there, friend.'''

options = '''Your options for the program are as follows:

1. Add a new movie to your list
2. Display movies in your list
3. Edit a movie in your list
4. Save changes
5. Save changes and exit'''

menu = '''\nPlease enter your input in the form of a number (1-5) or 6 for options: '''

file_name = 'horror_movies.json'
try:
    load_movies(file_name)
except:
    print('\n"horror_movies" file not found')
    JSONhorror_movies = []

horror_movies = []
for JSONhorror_movie in JSONhorror_movies:
    horror = json.loads(JSONhorror_movie)
    print((horror).strip('{}').replace("'", ""  ))
    horror = json.loads(horror)
    print(horror['title'])
   
    
   

print(introduction, options)

while True:
    command = read_int_ranged(prompt = menu, min_value = 1, max_value = 6)
    if command == 1:
       new_movie()
    elif command == 2:
        pass#display_movies()
    elif command == 3:
        pass #edit_movie()
    elif command == 4:
        save_movies(file_name)
    elif command == 5:
        save_movies(file_name)
        break
    elif command == 6:
        print('\n')
        print(options)