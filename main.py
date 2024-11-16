import streamlit as st

# Mock music database (initially pre-filled)
MUSIC_DATABASE = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "mood": "Energetic", "file": "mp3/1.mp3"},
    {"title": "Shallow", "artist": "Lady Gaga & Bradley Cooper", "mood": "Romantic", "file": "mp3/2.mp3"},
    {"title": "Someone You Loved", "artist": "Lewis Capaldi", "mood": "Sad", "file": "mp3/3.mp3"},
    {"title": "Happier", "artist": "Marshmello", "mood": "Happy", "file": "mp3/4.mp3"},
    {"title": "Weightless", "artist": "Marconi Union", "mood": "Relaxed", "file": "mp3/5.mp3"},
]

# User playlists (dynamic during runtime)
user_playlists = {}

def main():
    st.title("🎵 Music Playlist App (Like Spotify) 🎧")
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Browse Music", "My Playlists", "Create Playlist", "Upload Music"])

    if page == "Home":
        st.header("Welcome to Your Personal Music Playlist App!")
        st.write("🎶 Explore music by mood, create playlists, upload your music, and enjoy listening!")
    elif page == "Browse Music":
        browse_music()
    elif page == "My Playlists":
        view_playlists()
    elif page == "Create Playlist":
        create_playlist()
    elif page == "Upload Music":
        upload_music()

def browse_music():
    st.header("Browse Music by Mood")
    moods = sorted(set(song["mood"] for song in MUSIC_DATABASE))
    selected_mood = st.selectbox("Select a mood:", options=moods)

    filtered_songs = [song for song in MUSIC_DATABASE if song["mood"] == selected_mood]

    if filtered_songs:
        st.subheader(f"Songs for mood: {selected_mood}")
        for song in filtered_songs:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"🎵 **{song['title']}** - {song['artist']}")
            with col2:
                if st.button(f"Play '{song['title']}'", key=song["title"]):
                    st.audio(song["file"], format="audio/mp3")
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
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"🎵 **{song['title']}** - {song['artist']}")
            with col2:
                if st.button(f"Play '{song['title']}'", key=song["title"]):
                    st.audio(song["file"], format="audio/mp3")

def upload_music():
    st.header("Upload Your Music")
    uploaded_file = st.file_uploader("Upload MP3 file", type=["mp3"])
    song_title = st.text_input("Enter the song title:")
    artist_name = st.text_input("Enter the artist name:")
    song_mood = st.selectbox("Select the mood of the song:", ["Energetic", "Romantic", "Sad", "Happy", "Relaxed"])

    if st.button("Upload Music"):
        if uploaded_file and song_title and artist_name:
            # Save uploaded file to "mp3" directory
            with open(f"mp3/{uploaded_file.name}", "wb") as f:
                f.write(uploaded_file.getbuffer())
            # Add song to database
            MUSIC_DATABASE.append({
                "title": song_title,
                "artist": artist_name,
                "mood": song_mood,
                "file": f"mp3/{uploaded_file.name}",
            })
            st.success(f"'{song_title}' by {artist_name} added to the music library!")
        else:
            st.error("Please fill in all the fields and upload a valid MP3 file.")

if __name__ == "__main__":
    main()
