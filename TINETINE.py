import streamlit as st

st.set_page_config(
    page_title="Our Timeline",
    page_icon="🎧",
    layout="centered"
)

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
        "description": "That moment when I knew I was going on a crazy ride.",
        "song": "https://open.spotify.com/embed/track/48CiA3IjkNZiyl6S6UbPCy?start=33"
    },
    {
        "title": "When You Started to Matter More",
        "description": "And I didn’t even realize I was falling for you.",
        "song": "https://open.spotify.com/embed/track/06zLpakRZhozCnk3bZnGFT?start=22"
    },
    {
        "title": "Our Sponty Galas",
        "description": "Doing random things with no plans — cherishing every single moment of it",
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
HELLOOO MERRY CHRISTMAS TO YOU MI FAVORITE GIRL, I know this isn't much for a Christmas surprise but I hope you like this. Eto na rin yung part 2 ng letter ko hehehe.

</div>
""", unsafe_allow_html=True)


