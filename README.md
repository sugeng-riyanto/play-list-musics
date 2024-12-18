

# 🎵 Music Playlist App (Spotify-Like) 🎧

This Streamlit-based web application allows users to browse music by mood, create personalized playlists, and explore Spotify tracks through an embedded player. The app is beginner-friendly and can be extended for more features.

---

## Features

- **Browse Music by Mood**: Explore songs based on moods like Energetic, Romantic, Sad, Happy, and Relaxed.
- **Create Playlists**: Make your own playlists by selecting songs from the music library.
- **View Playlists**: Access and enjoy the playlists you’ve created.
- **Add New Songs**: Add new tracks to the music database with a Spotify link.
- **Spotify Integration**: Embedded Spotify player for seamless music streaming.

---

## Installation and Setup

1. **Install Python**: Ensure Python 3.7 or higher is installed on your system.

2. **Install Streamlit**: 
   ```bash
   pip install streamlit
   ```

3. **Clone or Download the Repository**:
   Download this project from the GitHub repository or manually save the script.

4. **Run the Application**:
   Open your terminal and navigate to the folder where the script is located. Run the following command:
   ```bash
   streamlit run app.py
   ```

5. **Access the App**:
   Once the server starts, open the link provided in the terminal (usually `http://localhost:8501`) in your browser.

---

## How to Use

### Home Page
- Welcome screen with a brief description of the app.

### Browse Music
1. Navigate to the **Browse Music** section using the sidebar.
2. Select a mood from the dropdown menu.
3. Explore songs matching the selected mood, with embedded Spotify players.

### Create Playlist
1. Navigate to the **Create Playlist** section.
2. Enter a playlist name in the text field.
3. Select songs from the library to include in your playlist.
4. Click "Create Playlist" to save your playlist.

### View Playlists
1. Navigate to the **My Playlists** section.
2. Choose a playlist from the dropdown menu.
3. View and play songs in the selected playlist.

### Add Spotify Link
1. Navigate to the **Add Spotify Link** section.
2. Fill in the song details: Title, Artist, Mood, and Spotify Link.
3. Click "Add Spotify Link" to update the music database.

---

## File Structure

```
.
├── app.py         # Main application script
├── requirements.txt # Optional for listing required Python packages
└── README.md      # Instructions for users
```

---

## Requirements

- Python 3.7 or higher
- Streamlit library

Install the dependencies using:
```bash
pip install -r requirements.txt
```

---

## Example Music Database

The app comes with a pre-filled music library. You can expand the library dynamically by adding songs through the **Add Spotify Link** section.

---

## Future Enhancements

- User login for personalized experiences.
- Playlist sharing options.
- Advanced filtering and sorting for songs.
- Integration with Spotify API for dynamic recommendations.

---

## Contact

For questions or suggestions, feel free to reach out at [your-email@example.com]. 

Happy listening! 🎶
