import streamlit as st
import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
SPOTIFY_CLIENT_ID = "1746781a5bf14399be9b5b9528427e5d"
SPOTIFY_CLIENT_SECRET = "862ddf3c74fe4f628dfbf2ccea02265a"

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Page config
st.set_page_config(page_title="Music Recommender", page_icon="🎵", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Title styling */
    .main-title {
        text-align: center;
        color: white;
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: fadeIn 1s ease-in;
    }
    
    .subtitle {
        text-align: center;
        color: #f0f0f0;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Emotion card styling */
    .emotion-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem auto;
        max-width: 500px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    /* Song card styling */
    .song-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .song-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    .song-number {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.2rem;
    }
    
    .song-info {
        flex-grow: 1;
    }
    
    .song-name {
        color: #2d3748;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }
    
    .song-artist {
        color: #718096;
        font-size: 0.9rem;
    }
    
    /* Custom button styling */
    .stButton > button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.75rem 2.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(245, 87, 108, 0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(245, 87, 108, 0.6);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Label styling */
    label {
        color: white !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }
    
    /* Album image styling */
    .album-img {
        width: 80px;
        height: 80px;
        border-radius: 10px;
        object-fit: cover;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    
    /* Play button styling */
    .play-btn {
        background: #1DB954;
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
    }
    
    .play-btn:hover {
        background: #1ed760;
        transform: scale(1.05);
    }
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Emoji icons for emotions */
    .emotion-icon {
        font-size: 3rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-title">🎵 Emotion-Based Music Recommender 🎧</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Discover the perfect songs for your mood</p>', unsafe_allow_html=True)

# Emotion selection with icons
emotion_icons = {
    "Happy": "😊",
    "Sad": "😢",
    "Angry": "😠",
    "Relaxed": "😌"
}

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="emotion-container">', unsafe_allow_html=True)
    
    emotion = st.selectbox(
        "How are you feeling today?",
        ["Happy", "Sad", "Angry", "Relaxed"],
        format_func=lambda x: f"{emotion_icons[x]} {x}"
    )
    
    # Display emotion icon
    st.markdown(f'<div class="emotion-icon">{emotion_icons[emotion]}</div>', unsafe_allow_html=True)
    
    recommend_button = st.button("🎵 Find My Music")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Recommendations
if recommend_button:
    st.markdown(f"<h2 style='text-align: center; color: white; margin-top: 2rem;'>Top Songs for {emotion_icons[emotion]} {emotion} Mood</h2>", unsafe_allow_html=True)
    
    # Search query based on emotion
    results = sp.search(q=emotion + " mood", type='track', limit=5)
    tracks = results['tracks']['items']

    if tracks:
        # Auto-open first track
        first_track_url = tracks[0]['external_urls']['spotify']
        # Note: webbrowser.open_new_tab() might not work in Streamlit Cloud
        # webbrowser.open_new_tab(first_track_url)
        
        # Display tracks in cards
        for idx, track in enumerate(tracks):
            name = track['name']
            artist = track['artists'][0]['name']
            url = track['external_urls']['spotify']
            album_img = track['album']['images'][0]['url'] if track['album']['images'] else ""
            
            col1, col2, col3 = st.columns([1, 3, 1])
            
            with col2:
                st.markdown(f"""
                    <div class="song-card">
                        <div class="song-number">{idx+1}</div>
                        <img src="{album_img}" class="album-img" />
                        <div class="song-info">
                            <div class="song-name">{name}</div>
                            <div class="song-artist">🎤 {artist}</div>
                        </div>
                        <a href="{url}" target="_blank" class="play-btn">▶ Play</a>
                    </div>
                """, unsafe_allow_html=True)
                
    else:
        st.warning("🔍 No songs found. Try a different emotion.")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: rgba(255,255,255,0.7);'>Powered by Spotify API 🎵</p>",
    unsafe_allow_html=True
)
