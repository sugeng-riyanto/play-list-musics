# Import the Streamlit library for creating the web app
import streamlit as st

# Mock music database (initially pre-filled with some sample songs)
MUSIC_DATABASE = [
    # Each song is represented as a dictionary with title, artist, mood, and Spotify link
    {"title": "Blinding Lights", "artist": "The Weeknd", "mood": "Energetic", "spotify_link": "https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b"},
    {"title": "Shallow", "artist": "Lady Gaga & Bradley Cooper", "mood": "Romantic", "spotify_link": "https://open.spotify.com/track/2VxeLyX666F8uXCJ0dZF8B"},
    {"title": "Someone You Loved", "artist": "Lewis Capaldi", "mood": "Sad", "spotify_link": "https://open.spotify.com/track/7qEHsqek33rTcFNT9PFqLf"},
    {"title": "Happier", "artist": "Marshmello", "mood": "Happy", "spotify_link": "https://open.spotify.com/track/2dpaYNEQHiRxtZbfNsse99"},
    {"title": "Weightless", "artist": "Marconi Union", "mood": "Relaxed", "spotify_link": "https://open.spotify.com/track/4dZKhQIfmh3zjxBT9AH6sg"},
]

# A dynamic dictionary to store user-created playlists during runtime
user_playlists = {}

# Main function that controls the app
def main():
    # Set the title of the web application
    st.title("🎵 Music Playlist App (Spotify-Like) 🎧")
    
    # Add a sidebar with navigation options
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Browse Music", "My Playlists", "Create Playlist", "Add Spotify Link"])

    # Conditional rendering based on selected page
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

# Function to browse music by mood
def browse_music():
    st.header("Browse Music by Mood")
    
    # Extract all unique moods from the music database and sort them
    moods = sorted(set(song["mood"] for song in MUSIC_DATABASE))
    
    # Dropdown to select a mood
    selected_mood = st.selectbox("Select a mood:", options=moods)

    # Filter songs based on the selected mood
    filtered_songs = [song for song in MUSIC_DATABASE if song["mood"] == selected_mood]

    # Display the songs for the selected mood
    if filtered_songs:
        st.subheader(f"Songs for mood: {selected_mood}")
        for song in filtered_songs:
            st.write(f"🎵 **{song['title']}** - {song['artist']}")
            # Embed Spotify player for each song
            st.markdown(f"<iframe src='https://open.spotify.com/embed/track/{song['spotify_link'].split('/')[-1]}' width='300' height='80' frameborder='0' allowtransparency='true' allow='encrypted-media'></iframe>", unsafe_allow_html=True)
    else:
        st.write("No songs found for this mood.")

# Function to create a new playlist
def create_playlist():
    st.header("Create Your Playlist")
    
    # Input field to name the playlist
    playlist_name = st.text_input("Enter a playlist name:")
    if not playlist_name:
        st.warning("Please enter a playlist name to proceed.")
        return

    # Multiselect dropdown to choose songs for the playlist
    selected_songs = st.multiselect(
        "Select songs to add to your playlist:",
        options=[f"{song['title']} - {song['artist']}" for song in MUSIC_DATABASE],
    )

    # Button to create the playlist
    if st.button("Create Playlist"):
        if not selected_songs:
            st.error("Please select at least one song to create a playlist.")
        else:
            # Save the playlist in the user_playlists dictionary
            user_playlists[playlist_name] = [
                song for song in MUSIC_DATABASE if f"{song['title']} - {song['artist']}" in selected_songs
            ]
            st.success(f"Playlist '{playlist_name}' created successfully!")

# Function to view existing playlists
def view_playlists():
    st.header("Your Playlists")
    
    # Check if there are any user-created playlists
    if not user_playlists:
        st.write("You haven't created any playlists yet. Go to 'Create Playlist' to make one!")
        return

    # Dropdown to select a playlist
    playlist_name = st.selectbox("Select a playlist:", options=list(user_playlists.keys()))
    if playlist_name:
        st.subheader(f"Playlist: {playlist_name}")
        # Display the songs in the selected playlist
        for song in user_playlists[playlist_name]:
            st.write(f"🎵 **{song['title']}** - {song['artist']}")
            # Embed Spotify player for each song
            st.markdown(f"<iframe src='https://open.spotify.com/embed/track/{song['spotify_link'].split('/')[-1]}' width='300' height='80' frameborder='0' allowtransparency='true' allow='encrypted-media'></iframe>", unsafe_allow_html=True)

# Function to add a new Spotify track to the database
def add_spotify_link():
    st.header("Add a Spotify Track")
    
    # Input fields to get song details from the user
    song_title = st.text_input("Enter the song title:")
    artist_name = st.text_input("Enter the artist name:")
    song_mood = st.selectbox("Select the mood of the song:", ["Energetic", "Romantic", "Sad", "Happy", "Relaxed"])
    spotify_link = st.text_input("Enter the Spotify track link (URL):")

    # Button to add the new song to the database
    if st.button("Add Spotify Link"):
        if song_title and artist_name and song_mood and spotify_link:
            # Append the new song to the music database
            MUSIC_DATABASE.append({
                "title": song_title,
                "artist": artist_name,
                "mood": song_mood,
                "spotify_link": spotify_link,
            })
            st.success(f"'{song_title}' by {artist_name} added to the music library!")
        else:
            st.error("Please fill in all the fields.")

# Entry point for the application
if __name__ == "__main__":
    main()
