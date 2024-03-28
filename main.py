from Billboard_scraper import BillboardScraper
from spotify_auth import SpotifyAuth
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    spotify_auth = SpotifyAuth()
    # Redirect to Spotify for authentication
    auth_url = spotify_auth.Oauth_Obj.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Xử lý mã xác thực từ Spotify ở đây
    code = request.args.get('code')
    # Thực hiện các xác thực tiếp theo hoặc lưu mã xác thực
    return 'Authentication successful! You can close this window.'

def main():
    date_endpoint = input("What time do you want to travel to ?(Write in format YYYY-MM-DD): ")
    year = date_endpoint[0:4]

    billboard_scraper = BillboardScraper()
    top_100_songs_data = billboard_scraper.get_top_100_songs(date_endpoint=date_endpoint)

    spotify_auth = SpotifyAuth()
    spotify_auth.create_urls_data(data=top_100_songs_data,released_year=year)
    name_of_playlist = date_endpoint + ' Billboard 100'
    spotify_auth.create_playlist(name_of_playlist=name_of_playlist)
    spotify_auth.add_song_to_playlist()

    

if __name__ == "__main__":
    main()
    

