import streamlit as st
import time
import random

# --- 1. CONFIGURATION & VISUAL STYLE ---
st.set_page_config(
    page_title="SnapDish | Investor Demo",
    page_icon="📸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Color Palette from Pitch Deck
COLORS = {
    "bg": "#0E0E0E",          # Jet Black (Deep dark gray)
    "card_bg": "#1C1C1E",     # Slightly lighter for cards
    "primary": "#FF5A36",     # Vibrant Coral (Actions)
    "secondary": "#C68E5D",   # Warm Camel (Headings)
    "text": "#EAE0D5",        # Off-white/Bone
    "accent_teal": "#3B6E8F", # Slate Teal
    "success": "#2E7D32"
}

# Custom CSS to force the "Vibe"
st.markdown(f"""
    <style>
    /* Global App Style */
    .stApp {{
        background-color: {COLORS['bg']};
        font-family: 'Helvetica Neue', sans-serif;
    }}
    
    /* Headings */
    h1, h2, h3 {{
        color: {COLORS['secondary']} !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    
    h4, h5, h6 {{
        color: {COLORS['text']} !important;
        font-weight: 600;
    }}
    
    /* Text */
    p, label, span {{
        color: {COLORS['text']} !important;
    }}
    
    /* Buttons (Primary Action) */
    div.stButton > button:first-child {{
        background-color: {COLORS['primary']} !important;
        color: white !important;
        border-radius: 8px;
        border: none;
        padding: 12px 24px;
        font-weight: bold;
        text-transform: uppercase;
        width: 100%;
        transition: transform 0.1s ease;
    }}
    div.stButton > button:first-child:hover {{
        transform: scale(1.02);
        filter: brightness(110%);
    }}
    
    /* Secondary/Ghost Buttons */
    .ghost-btn {{
        background-color: transparent;
        border: 1px solid {COLORS['secondary']};
        color: {COLORS['secondary']};
        padding: 8px 16px;
        border-radius: 6px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        margin: 5px;
    }}

    /* Cards ("Binder" Style) */
    .binder-card {{
        background-color: {COLORS['card_bg']};
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid {COLORS['secondary']};
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }}
    
    .recipe-card {{
        background-color: {COLORS['card_bg']};
        border: 1px solid #333;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
    }}

    /* Bottom Nav Mockup */
    .nav-container {{
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: {COLORS['card_bg']};
        padding: 15px 0;
        display: flex;
        justify-content: space-around;
        border-top: 1px solid #333;
        z-index: 999;
    }}
    .nav-item {{
        text-align: center;
        font-size: 24px;
        cursor: pointer;
        color: {COLORS['secondary']};
    }}
    
    /* Metrics */
    div[data-testid="stMetricValue"] {{
        color: {COLORS['primary']} !important;
    }}
    div[data-testid="stMetricLabel"] {{
        color: {COLORS['text']} !important;
    }}
    </style>
""", unsafe_allow_html=True)

# --- 2. STATE MANAGEMENT ---
if "page" not in st.session_state:
    st.session_state.page = "Splash"
if "inventory" not in st.session_state:
    st.session_state.inventory = []
if "demo_mode" not in st.session_state:
    st.session_state.demo_mode = False

def navigate_to(page):
    st.session_state.page = page
    st.rerun()

# --- 3. SCREENS ---

def splash_screen():
    st.markdown("<div style='height: 15vh;'></div>", unsafe_allow_html=True)
    
    # Logo / Branding
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown(f"<h1 style='text-align: center; font-size: 3rem; color:{COLORS['primary']} !important;'>SNAP<br>DISH</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; opacity: 0.8;'>One picture. One recipe. Zero thinking.</p>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        if st.button("GET STARTED"):
            navigate_to("Onboarding")
            
    st.markdown("<div style='text-align: center; margin-top: 50px; color: #555;'>INVESTOR DEMO BUILD v0.1</div>", unsafe_allow_html=True)

def onboarding_screen():
    st.title("SETUP PROFILE")
    
    st.markdown(f"""
    <div class="binder-card">
        <h4>What's your goal?</h4>
        <p>Help us tailor your AI chef.</p>
    </div>
    """, unsafe_allow_html=True)
    
    goal = st.radio("Select Primary Goal", ["Reduce Food Waste", "Save Time", "Eat Healthier"], label_visibility="collapsed")
    
    st.markdown("### DIETARY PREFS")
    diet = st.multiselect("Any restrictions?", ["Vegetarian", "Vegan", "Gluten-Free", "Keto", "Halal"], default=[])
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("CREATE ACCOUNT"):
        st.toast("Profile Created!", icon="✅")
        time.sleep(1)
        navigate_to("Home")

def home_screen():
    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"<h2>HI YVETTE 👋</h2>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='background:{COLORS['primary']}; width:40px; height:40px; border-radius:50%; text-align:center; line-height:40px; font-weight:bold;'>Y</div>", unsafe_allow_html=True)
    
    st.markdown("<p style='opacity:0.7;'>What are we cooking tonight?</p>", unsafe_allow_html=True)
    
    # Primary CTA
    st.markdown("---")
    if st.button("📸 SNAP MY FRIDGE"):
        navigate_to("Scan")
    st.markdown("---")
    
    # Quick Picks
    st.markdown("### TONIGHT'S PICKS")
    
    # Card 1
    st.markdown(f"""
    <div class="recipe-card">
        <div style="height: 120px; background-color: #333; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #777;">
            [Food Image: Spicy Tofu Bowl]
        </div>
        <h4 style="margin-top: 10px; color: {COLORS['secondary']} !important;">Spicy Tofu Bowl</h4>
        <div style="display: flex; gap: 10px; font-size: 0.8rem;">
            <span style="color: {COLORS['primary']} !important;">🔥 15 min</span>
            <span style="color: {COLORS['accent_teal']} !important;">💪 22g Protein</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Card 2
    st.markdown(f"""
    <div class="recipe-card">
        <div style="height: 120px; background-color: #333; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #777;">
            [Food Image: Avocado Toast]
        </div>
        <h4 style="margin-top: 10px; color: {COLORS['secondary']} !important;">Loaded Avo Toast</h4>
        <div style="display: flex; gap: 10px; font-size: 0.8rem;">
            <span style="color: {COLORS['primary']} !important;">⚡ 5 min</span>
            <span style="color: {COLORS['accent_teal']} !important;">🌱 Vegan</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Bottom Nav Spacer
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

def scan_screen():
    st.markdown(f"<h3 style='text-align:center;'>CAMERA VIEW</h3>", unsafe_allow_html=True)
    
    # Mock Camera View
    camera_placeholder = st.empty()
    
    # Instructions
    st.markdown(f"""
    <div style="border: 2px dashed {COLORS['text']}; border-radius: 12px; height: 300px; display: flex; align-items: center; justify-content: center; flex-direction: column;">
        <h1 style="font-size: 3rem;">📸</h1>
        <p>Point at your open fridge</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("SHUTTER"):
            # Simulation of AI Processing
            with st.spinner("AI Analysing Ingredients..."):
                time.sleep(2) # Fake processing time
                st.session_state.inventory = ["Eggs", "Spinach", "Cherry Tomatoes", "Feta Cheese", "Leftover Chicken"]
                navigate_to("Results")

    if st.button("← Back"):
        navigate_to("Home")

def results_screen():
    st.title("WE FOUND")
    
    # Detected Ingredients
    col1, col2 = st.columns(2)
    for i, item in enumerate(st.session_state.inventory):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
            <div style="background: {COLORS['card_bg']}; padding: 10px; border-radius: 8px; margin-bottom: 10px; text-align: center; border: 1px solid {COLORS['accent_teal']};">
                {item} ✅
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("---")
    st.subheader("YOU CAN COOK:")
    
    # Result 1: Perfect Match
    with st.container():
        st.markdown(f"""
        <div class="binder-card" style="border-left-color: {COLORS['primary']};">
            <h3 style="margin-bottom: 0;">Mediterranean Omelet</h3>
            <p style="color: {COLORS['primary']} !important; font-weight: bold; font-size: 0.9rem;">USES 4/5 INGREDIENTS</p>
            <p style="font-size: 0.9rem;">Eggs • Spinach • Tomatoes • Feta</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("COOK THIS NOW", key="cook1"):
            st.balloons()
            st.toast("Starting Cooking Mode...", icon="🔥")
    
    # Result 2: Missing Item
    with st.container():
        st.markdown(f"""
        <div class="binder-card" style="border-left-color: {COLORS['secondary']}; opacity: 0.8;">
            <h3 style="margin-bottom: 0;">Chicken Salad</h3>
            <p style="color: #888 !important; font-weight: bold; font-size: 0.9rem;">MISSING: OLIVE OIL</p>
            <p style="font-size: 0.9rem;">Chicken • Spinach • Tomatoes • Feta</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("VIEW RECIPE", key="cook2"):
            pass

    if st.button("Scan Again"):
        navigate_to("Scan")

def plan_screen():
    st.title("WEEKLY PLAN")
    
    # Premium Upsell Visual
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {COLORS['secondary']}, {COLORS['primary']}); padding: 2px; border-radius: 12px;">
        <div style="background: {COLORS['bg']}; border-radius: 10px; padding: 20px; text-align: center;">
            <h3 style="color: {COLORS['primary']} !important;">UNLOCK AUTO-PILOT</h3>
            <p>Get a weekly plan generated from your leftovers.</p>
            <ul style="text-align: left; margin: 20px 0; color: {COLORS['text']};">
                <li>✅ Zero-waste grocery lists</li>
                <li>✅ Macro tracking</li>
                <li>✅ Unlimited AI scans</li>
            </ul>
            <h2 style="color: white !important;">$7.99/mo</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("START FREE TRIAL")
    
    st.markdown("---")
    if st.button("← Back Home"):
        navigate_to("Home")

# --- 4. MAIN APP ROUTER ---

# Render the active page
if st.session_state.page == "Splash":
    splash_screen()
elif st.session_state.page == "Onboarding":
    onboarding_screen()
elif st.session_state.page == "Home":
    home_screen()
elif st.session_state.page == "Scan":
    scan_screen()
elif st.session_state.page == "Results":
    results_screen()
elif st.session_state.page == "Plan":
    plan_screen()

# --- 5. BOTTOM NAVIGATION (Sticky) ---
if st.session_state.page in ["Home", "Results", "Plan"]:
    st.markdown(f"""
    <div class="nav-container">
        <div class="nav-item">🏠</div>
        <div class="nav-item" style="color: {COLORS['primary']}; font-weight: bold;">📸</div>
        <div class="nav-item">📅</div>
        <div class="nav-item">👤</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hacky way to make nav interactive (in a real app these would be buttons)
    # Since st.button inside HTML isn't native, we use a sidebar for actual nav in this demo
    with st.sidebar:
        st.title("Dev Navigation")
        if st.button("Go Home"): navigate_to("Home")
        if st.button("Go Plan"): navigate_to("Plan")
        if st.button("Go Splash"): navigate_to("Splash")