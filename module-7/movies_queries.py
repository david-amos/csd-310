# David Amos 4/15/2024 Module 7.2 Assignment
# This program queries the movies database
import mysql.connector
from mysql.connector import errorcode
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}


try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    cursor = db.cursor()
    cursor.execute("SELECT studio_id, studio_name FROM studio")
    studios = cursor.fetchall()
    print("-- Displaying Studio RECORDS --")
    for studio in studios:
        print("Studio ID: {}".format(studio[0]))
        print("Studio Name: {}".format(studio[1]))
        print("")

    cursor.execute("SELECT genre_id, genre_name FROM genre")
    genres = cursor.fetchall()
    print("-- Displaying Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}".format(genre[0]))
        print("Genre Name: {}".format(genre[1]))
        print("")

    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    films = cursor.fetchall()
    print("-- Displaying Short Film RECORDS --")
    for film in films:
        print("Film Name: {}".format(film[0]))
        print("Runtime: {}".format(film[1]))
        print("")

    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    directors = cursor.fetchall()
    print("-- Displaying Director RECORDS in Order --")
    for director in directors:
        print("Film Name: {}".format(director[0]))
        print("Director: {}".format(director[1]))
        print("")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)
except:
    print("Error other than database connection occured")

finally:
    db.close()