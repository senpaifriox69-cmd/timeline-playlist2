import streamlit as st

st.set_page_config(
    page_title="Our Timeline",
    page_icon="🎧",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.main {
    background-color: #0e0e10;
}
.timeline-card {
    background: #16161a;
    padding: 1.5rem;
    border-radius: 16px;
    margin-bottom: 1.5rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}
.timeline-title {
    font-size: 1.3rem;
    font-weight: 600;
}
.timeline-desc {
    color: #b3b3b3;
    margin-bottom: 0.8rem;
}
.long-message {
    background: linear-gradient(145deg, #1a1a1f, #121216);
    padding: 2rem;
    border-radius: 20px;
    font-size: 1.05rem;
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.title("🎶 Our Timeline Playlist")
st.caption("Songs, moments, and feelings — one timeline.")

# ---------- Timeline Data ----------
timeline = [
    {
        "title": "When I First Noticed My Feelings for You",
        "description": "That moment when everything feels so different.",
        "song": "https://open.spotify.com/embed/track/48CiA3IjkNZiyl6S6UbPCy"
    },
    {
        "title": "When You Started to Matter More",
        "description": "And I didn’t even realize I was falling for you.",
        "song": "https://open.spotify.com/embed/track/06zLpakRZhozCnk3bZnGFT?start=22"
    },
    {
        "title": "Our Sponty Galas",
        "description": "Doing random things with no plans — loving every second.",
        "song": "https://open.spotify.com/embed/track/6t4CmQGucLORsKZF4M6NNC?start=42"
    },
    {
        "title": "Right Now",
        "description": "This is where my heart is.",
        "song": "https://open.spotify.com/embed/track/0kE1SmlJNLg14dgdo9kJws?start=174"
    }
]

# ---------- Timeline UI ----------
for moment in timeline:
    st.markdown(f"""
    <div class="timeline-card">
        <div class="timeline-title">{moment['title']}</div>
        <div class="timeline-desc">{moment['description']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.components.v1.iframe(
        moment["song"],
        height=152,
        scrolling=False
    )


st.markdown("## Merry Christmas to mi Favorite Girl")

st.markdown("""
<div class="long-message">
I don’t know when exactly this turned into something real —  
maybe it was slow, maybe it was sudden —  
but somewhere between the laughs, the silence, and the random moments,  
you became someone I carry with me.

This playlist isn’t just about songs.  
It’s about timestamps of feelings I didn’t know how to say out loud.  
Every track starts somewhere specific, just like how you started meaning more to me without warning.

If you ever wonder where you stand,  
this is my answer —  
right here, right now, in every moment that led us here.
</div>
""", unsafe_allow_html=True)
