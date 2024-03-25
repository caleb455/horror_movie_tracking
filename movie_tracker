import json

from BTCInput import read_int_ranged, read_text


class Movie:
    def __init__(
        self, 
        title = 'None', 
        release_date = 'None', 
        personal_rating = 'None', 
        tags = None
    ):
        self.title = title
        self.release_date = release_date
        self.personal_rating = personal_rating
        self.tags = tags
        self.__version = 1

    def to_dict(self): # Changed the function purpose
        dict = {
            'Title': self.title,
            'Release Date': self.release_date,
            'Personal Rating': self.personal_rating,
            'Tags': self.tags
        } #Defined as a dictionary ofc
        return dict

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def check_version(self):
        pass


def new_movie():
    print("\nAdd a new movie to your list")
    while True:
        title = read_text("\nEnter the title of the movie: ")
        release_date = read_text("\nEnter the release date (YYYY) of the movie: ")
        personal_rating = read_text(
            "\nEnter your personal rating (#/10) for the movie: "
        )
        tags = []
        new_movie = None
        while True:
            enter_tag = read_text("\nEnter a tag or 'cont' to continue: ")
            if enter_tag != "cont":
                tags.append(enter_tag)
                continue
            elif enter_tag == "cont":
                print("\nOk")
                break
            else:
                print("Sorry, that is not a viable input.")
                continue
        try:
            new_movie = Movie(
                title=title,
                release_date=release_date,
                personal_rating=personal_rating,
                tags=tags,
            ).to_dict()

        except Exception as e:
            print("\nError: ", e)
        if new_movie is not None:
            print(f"Title: {new_movie['Title']}") # Changed how the completed movie is printed
            print(f"Release Date: {new_movie['Release Date']}")
            print(f"Personal Rating: {new_movie['Personal Rating']}")
            tags = str(new_movie['Tags']).strip('[]').replace("'", '')
            print(tags)
        while True:
            confirmation = read_text("\nDoes this look good? (y/n) ")
            if confirmation == "y" and new_movie is not None:
                moviesJSONdata = json.dumps(new_movie, indent=4)
                JSONhorror_movies.append(moviesJSONdata)
                break
            elif confirmation == "n":
                break
            else:
                print("\nSorry, that is not a viable input.")
                continue
        break


def save_movies(file_name):
    print('\nSaved to "horror_movies" file')
    with open(file_name, "w") as output_file:
        json.dump(JSONhorror_movies, output_file)


def load_movies(file_name):
    print('Load "horror_movies" file')
    with open(file_name, "r") as input_file:
        return json.load(input_file)


def overwrite(file_name):
    with open(file_name, "w"):
        pass


introduction = """\nHello there, friend."""

options = """Your options for the program are as follows:

1. Add a new movie to your list
2. Display movies in your list
3. Edit a movie in your list
4. Save changes
5. Save changes and exit"""

menu = """\nPlease enter your input in the form of a number (1-5) or 6 for options: """

file_name = "horror_movies.json"
JSONhorror_movies = [] # Predefined this
try:
    JSONhorror_movies = load_movies(file_name)
except:
    print('\n"horror_movies" file not found')

horror_movies = []
for JSONhorror_movie in JSONhorror_movies:
    horror = json.loads(JSONhorror_movie)
    print((horror).strip("{}").replace("'", ""))
    horror = json.loads(horror)
    print(horror["title"])

print(introduction, options)

while True:
    command = read_int_ranged(prompt=menu, min_value=1, max_value=6)
    if command == 1:
        new_movie()
    elif command == 2:
        pass  # display_movies()
    elif command == 3:
        pass  # edit_movie()
    elif command == 4:
        save_movies(file_name)
    elif command == 5:
        save_movies(file_name)
        break
    elif command == 6:
        print("\n")
        print(options)
