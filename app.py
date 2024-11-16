import streamlit as st

# Mock music database (initially pre-filled)
MUSIC_DATABASE = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "mood": "Energetic", "spotify_link": "https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b"},
    {"title": "Shallow", "artist": "Lady Gaga & Bradley Cooper", "mood": "Romantic", "spotify_link": "https://open.spotify.com/track/2VxeLyX666F8uXCJ0dZF8B"},
    {"title": "Someone You Loved", "artist": "Lewis Capaldi", "mood": "Sad", "spotify_link": "https://open.spotify.com/track/7qEHsqek33rTcFNT9PFqLf"},
    {"title": "Happier", "artist": "Marshmello", "mood": "Happy", "spotify_link": "https://open.spotify.com/track/2dpaYNEQHiRxtZbfNsse99"},
    {"title": "Weightless", "artist": "Marconi Union", "mood": "Relaxed", "spotify_link": "https://open.spotify.com/track/4dZKhQIfmh3zjxBT9AH6sg"},
]

# User playlists (dynamic during runtime)
user_playlists = {}

def main():
    st.title("🎵 Music Playlist App (Spotify-Like) 🎧")
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Browse Music", "My Playlists", "Create Playlist", "Add Spotify Link"])

    if page == "Home":
        st.header("Welcome to Your Personal Music Playlist App!")
        st.write("🎶 Explore music by mood, create playlists, and enjoy Spotify tracks!")
    elif page == "Browse Music":
        browse_music()
    elif page == "My Playlists":
        view_playlists()
    elif page == "Create Playlist":
        create_playlist()
    elif page == "Add Spotify Link":
        add_spotify_link()

def browse_music():
    st.header("Browse Music by Mood")
    moods = sorted(set(song["mood"] for song in MUSIC_DATABASE))
    selected_mood = st.selectbox("Select a mood:", options=moods)

    filtered_songs = [song for song in MUSIC_DATABASE if song["mood"] == selected_mood]

    if filtered_songs:
        st.subheader(f"Songs for mood: {selected_mood}")
        for song in filtered_songs:
            st.write(f"🎵 **{song['title']}** - {song['artist']}")
            st.markdown(f"<iframe src='https://open.spotify.com/embed/track/{song['spotify_link'].split('/')[-1]}' width='300' height='80' frameborder='0' allowtransparency='true' allow='encrypted-media'></iframe>", unsafe_allow_html=True)
    else:
        st.write("No songs found for this mood.")

def create_playlist():
    st.header("Create Your Playlist")
    playlist_name = st.text_input("Enter a playlist name:")
    if not playlist_name:
        st.warning("Please enter a playlist name to proceed.")
        return

    selected_songs = st.multiselect(
        "Select songs to add to your playlist:",
        options=[f"{song['title']} - {song['artist']}" for song in MUSIC_DATABASE],
    )

    if st.button("Create Playlist"):
        if not selected_songs:
            st.error("Please select at least one song to create a playlist.")
        else:
            user_playlists[playlist_name] = [
                song for song in MUSIC_DATABASE if f"{song['title']} - {song['artist']}" in selected_songs
            ]
            st.success(f"Playlist '{playlist_name}' created successfully!")

def view_playlists():
    st.header("Your Playlists")
    if not user_playlists:
        st.write("You haven't created any playlists yet. Go to 'Create Playlist' to make one!")
        return

    playlist_name = st.selectbox("Select a playlist:", options=list(user_playlists.keys()))
    if playlist_name:
        st.subheader(f"Playlist: {playlist_name}")
        for song in user_playlists[playlist_name]:
            st.write(f"🎵 **{song['title']}** - {song['artist']}")
            st.markdown(f"<iframe src='https://open.spotify.com/embed/track/{song['spotify_link'].split('/')[-1]}' width='300' height='80' frameborder='0' allowtransparency='true' allow='encrypted-media'></iframe>", unsafe_allow_html=True)

def add_spotify_link():
    st.header("Add a Spotify Track")
    song_title = st.text_input("Enter the song title:")
    artist_name = st.text_input("Enter the artist name:")
    song_mood = st.selectbox("Select the mood of the song:", ["Energetic", "Romantic", "Sad", "Happy", "Relaxed"])
    spotify_link = st.text_input("Enter the Spotify track link (URL):")

    if st.button("Add Spotify Link"):
        if song_title and artist_name and song_mood and spotify_link:
            MUSIC_DATABASE.append({
                "title": song_title,
                "artist": artist_name,
                "mood": song_mood,
                "spotify_link": spotify_link,
            })
            st.success(f"'{song_title}' by {artist_name} added to the music library!")
        else:
            st.error("Please fill in all the fields.")

if __name__ == "__main__":
    main()
