# Task1
# import requests

# # Your OpenWeatherMap API Key (Replace with your actual API key)
# API_KEY = "e8ea21546ccb83d5f9429127cb0c6aea"
# BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# def get_weather(city):
#     """Fetch weather data for a given city."""
#     params = {
#         "q": city,
#         "appid": API_KEY,
#         "units": "metric"  # Get temperature in Celsius
#     }

#     try:
#         response = requests.get(BASE_URL, params=params)
#         response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
#         data = response.json()

#         # Extract required weather details
#         weather_info = {
#             "City": data["name"],
#             "Temperature": f"{data['main']['temp']}°C",
#             "Humidity": f"{data['main']['humidity']}%",
#             "Weather Condition": data["weather"][0]["description"].capitalize(),
#             "Wind Speed": f"{data['wind']['speed']} m/s"
#         }

#         return weather_info

#     except requests.exceptions.RequestException as e:
#         return f"Error: {e}"
#     except KeyError:
#         return "Invalid response from the server. Check API key and city name."

# def display_weather(info):
#     """Print weather information in a readable format."""
#     if isinstance(info, dict):
#         print("\n🌍 Weather Report 🌍")
#         for key, value in info.items():
#             print(f"{key}: {value}")
#     else:
#         print(info)

# if __name__ == "__main__":
#     city_name = input("Enter a city name: ")
#     weather_data = get_weather(city_name)
#     display_weather(weather_data)


# Task2
# import requests
# import random

# # Your TMDb API Key (Replace with your actual API key)
# API_KEY = "your_api_key_here"
# BASE_URL = "https://api.themoviedb.org/3"

# def get_genre_id(genre_name):
#     """Fetch genre ID from TMDb based on user input."""
#     url = f"{BASE_URL}/genre/movie/list"
#     params = {"api_key": API_KEY, "language": "en-US"}

#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()
#         genres = response.json()["genres"]

#         for genre in genres:
#             if genre["name"].lower() == genre_name.lower():
#                 return genre["id"]

#         return None  # Genre not found

#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching genre data: {e}")
#         return None

# def get_movies_by_genre(genre_id):
#     """Fetch movies from a specific genre."""
#     url = f"{BASE_URL}/discover/movie"
#     params = {"api_key": API_KEY, "with_genres": genre_id, "sort_by": "popularity.desc"}

#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()
#         movies = response.json()["results"]

#         return movies if movies else None  # Return movies list or None if empty

#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching movies: {e}")
#         return None

# def recommend_random_movie(genre_name):
#     """Recommend a random movie from the selected genre."""
#     genre_id = get_genre_id(genre_name)
    
#     if not genre_id:
#         print("⚠️ Genre not found. Please try again with a valid genre!")
#         return

#     movies = get_movies_by_genre(genre_id)
    
#     if not movies:
#         print("⚠️ No movies found in this genre. Try another one!")
#         return

#     random_movie = random.choice(movies)
#     title = random_movie["title"]
#     overview = random_movie["overview"]
#     rating = random_movie["vote_average"]
    
#     print("\n🎬 Movie Recommendation 🎬")
#     print(f"Title: {title}")
#     print(f"Rating: ⭐ {rating}/10")
#     print(f"Overview: {overview}")

# if __name__ == "__main__":
#     genre = input("Enter a movie genre (e.g., Action, Comedy, Horror): ")
#     recommend_random_movie(genre)

