import streamlit as st
import time

# --- 1. CONFIGURATION & "IPHONE MODE" STYLE ---
st.set_page_config(
    page_title="SnapDish Prototype",
    page_icon="📸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Color Palette (Extracted from your deck)
COLORS = {
    "bg": "#050606",          # Near Black (Deck Background)
    "primary": "#FF5A36",     # Coral/Orange (Actions/Pentagon)
    "secondary": "#C68E5D",   # Warm Camel (Headings)
    "accent": "#3B6E8F",      # Teal (Triangle)
    "text": "#EAE0D5",        # Off-white
    "card": "#1a1a1a",        # Dark Card
    "success": "#2E7D32"
}

# --- THE MAGIC CSS: FORCE IPHONE FRAME ON DESKTOP ---
st.markdown(f"""
    <style>
    /* 1. Force the main container to look like a phone */
    .block-container {{
        max-width: 390px;       /* iPhone 14/15 Pro width */
        padding-top: 3rem;
        padding-bottom: 5rem;   /* Space for bottom nav */
        margin: auto;           /* Center it */
        
        /* The "Phone" Border */
        border: 10px solid #222;
        border-radius: 40px;
        background-color: {COLORS['bg']};
        box-shadow: 0px 0px 30px rgba(0,0,0,0.5);
        min-height: 800px;
    }}
    
    /* 2. Global Background (Outside the phone) */
    .stApp {{
        background-color: #111; /* Dark Desktop Background */
        font-family: 'Helvetica Neue', sans-serif;
    }}

    /* 3. Hide Streamlit Chrome */
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* 4. Custom Typography (Deck Vibe) */
    h1, h2, h3 {{
        color: {COLORS['secondary']} !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    p, span, div {{
        color: {COLORS['text']};
    }}
    
    /* 5. Custom Buttons */
    div.stButton > button {{
        width: 100%;
        border-radius: 25px;
        background-color: {COLORS['primary']};
        color: white;
        border: none;
        padding: 12px 0;
        font-weight: bold;
        text-transform: uppercase;
        transition: all 0.2s;
    }}
    div.stButton > button:hover {{
        background-color: #ff7b5f;
        transform: scale(1.02);
    }}
    
    /* 6. Ghost/Secondary Button Variant */
    .ghost-btn {{
        background: transparent; 
        border: 1px solid {COLORS['secondary']}; 
        color: {COLORS['secondary']};
    }}
    
    /* 7. Cards ("Binder" Style) */
    .binder-card {{
        background-color: {COLORS['card']};
        border-left: 5px solid {COLORS['secondary']};
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 10px;
    }}
    
    /* 8. Bottom Nav (Sticky) */
    .fixed-nav {{
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 360px; /* Match phone width approx */
        background-color: #1a1a1a;
        border-radius: 30px;
        padding: 10px 0;
        display: flex;
        justify-content: space-around;
        z-index: 9999;
        border: 1px solid #333;
        box-shadow: 0 5px 15px rgba(0,0,0,0.5);
    }}
    
    .nav-btn {{
        background: none;
        border: none;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 5px 15px;
    }}
    .nav-btn:hover {{
        transform: scale(1.2);
    }}
    </style>
""", unsafe_allow_html=True)

# --- 2. SESSION STATE (The "Brain") ---
if 'page' not in st.session_state:
    st.session_state.page = 'SPLASH'
if 'user' not in st.session_state:
    st.session_state.user = {'name': 'Yvette', 'scans': 0}
if 'inventory' not in st.session_state:
    st.session_state.inventory = [] 
if 'scan_mode' not in st.session_state:
    st.session_state.scan_mode = 'FRIDGE'

def nav(page):
    st.session_state.page = page
    st.rerun()

# --- 3. PAGE RENDERERS (The Views) ---

def page_splash():
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; font-size: 3.5rem; color:{COLORS['primary']}!important; line-height:1;'>SNAP<br>DISH</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; opacity:0.8;'>One picture. One recipe.<br>Zero thinking.</p>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("GET STARTED"):
        nav("ONBOARDING_1")
    
    st.markdown(f"<div style='text-align:center; margin-top:20px;'><a style='color:{COLORS['secondary']}; text-decoration:none;' href='#'>Log in</a></div>", unsafe_allow_html=True)

def page_onboarding_1():
    st.markdown("### STEP 1/3")
    st.title("GOALS")
    st.markdown("What do you want SnapDish to help with?")
    
    goals = st.multiselect("Select goals:", 
        ["Reduce food waste", "Decide what to cook", "Eat healthier", "Save time"],
        default=["Reduce food waste"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("NEXT"):
        nav("ONBOARDING_2")

def page_onboarding_2():
    st.markdown("### STEP 2/3")
    st.title("DIET & PREFS")
    
    st.selectbox("I eat...", ["Omnivore", "Vegetarian", "Vegan", "Halal", "Kosher"])
    st.multiselect("Allergies...", ["Nuts", "Dairy", "Gluten", "Shellfish"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("NEXT"):
        nav("ONBOARDING_3")

def page_onboarding_3():
    st.markdown("### STEP 3/3")
    st.title("CONTEXT")
    
    st.markdown("**Cooking Skill**")
    st.slider("Skill", 1, 3, 2, format="")
    st.caption("Beginner | Intermediate | Confident")
    
    st.markdown("**Cooking Time**")
    st.select_slider("Minutes", ["15", "30", "45+"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("CREATE ACCOUNT"):
        nav("HOME")

def page_home():
    # Header
    c1, c2 = st.columns([3, 1])
    c1.markdown(f"## HI {st.session_state.user['name'].upper()} 👋")
    c2.markdown(f"<div style='background:{COLORS['secondary']}; color:black; width:40px; height:40px; border-radius:50%; text-align:center; line-height:40px; font-weight:bold;'>YL</div>", unsafe_allow_html=True)
    
    # Hero CTA
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0; padding: 20px; border: 1px dashed {COLORS['text']}; border-radius: 15px;">
        <h3 style="color:{COLORS['primary']}!important;">HUNGRY?</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📸 SNAP MY FRIDGE"):
        st.session_state.scan_mode = 'FRIDGE'
        nav("SCAN_CAMERA")
        
    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
    
    if st.button("🍽️ SCAN A DISH"):
        st.session_state.scan_mode = 'DISH'
        nav("SCAN_CAMERA")

    # Quick Picks
    st.markdown("---")
    st.markdown("### TONIGHT'S PICKS")
    
    # Card 1
    st.markdown(f"""
    <div class="binder-card" style="border-left-color: {COLORS['primary']}">
        <div style="height:100px; background:#333; border-radius:8px; margin-bottom:10px;"></div>
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong>Spicy Tofu Bowl</strong>
            <span style="color:{COLORS['primary']}; font-weight:bold;">15 min</span>
        </div>
        <div style="margin-top:5px; font-size:0.8rem;">
            <span style="color:{COLORS['accent']};">High Protein</span> • Budget
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("View Recipe"):
        nav("RECIPE")

def page_scan_camera():
    st.markdown(f"<h3 style='text-align:center;'>{st.session_state.scan_mode} MODE</h3>", unsafe_allow_html=True)
    
    # Camera UI
    st.markdown(f"""
    <div style="height: 400px; background: #000; border-radius: 20px; border: 2px solid {COLORS['text']}; display: flex; align-items: center; justify-content: center; flex-direction: column;">
        <span style="font-size: 3rem;">🔭</span>
        <p style="margin-top:20px;">Point at {st.session_state.scan_mode.lower()}...</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⚪ SHUTTER"):
        with st.spinner("Analyzing..."):
            time.sleep(1.5)
            if st.session_state.scan_mode == 'FRIDGE':
                st.session_state.inventory = ["Eggs", "Spinach", "Tomatoes", "Rice"]
                nav("SCAN_INGREDIENTS")
            else:
                nav("SCAN_DISH_BREAKDOWN")

    if st.button("← Back"):
        nav("HOME")

def page_scan_ingredients():
    st.title("WE SEE...")
    
    c1, c2 = st.columns(2)
    for item in st.session_state.inventory:
        c1.markdown(f"<div style='background:{COLORS['card']}; padding:5px; border-radius:5px; text-align:center; margin:2px;'>{item}</div>", unsafe_allow_html=True)
    
    st.text_input("Add missing item:", placeholder="e.g. Tofu")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("SEE RECIPES"):
        nav("SCAN_RESULTS")
    
    if st.button("RESCAN"):
        nav("SCAN_CAMERA")

def page_scan_results():
    st.title("COOK THIS")
    
    # Filters
    st.markdown(f"""
    <div style="display:flex; gap:10px; margin-bottom:20px;">
        <span style="color:{COLORS['primary']}; border:1px solid {COLORS['primary']}; padding:2px 8px; border-radius:10px; font-size:0.8rem;">Quick</span>
        <span style="color:{COLORS['accent']}; border:1px solid {COLORS['accent']}; padding:2px 8px; border-radius:10px; font-size:0.8rem;">Protein</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Result 1 (Perfect)
    st.markdown(f"""
    <div class="binder-card" style="border-left-color: {COLORS['success']}">
        <h4>Mediterranean Omelet</h4>
        <p style="color:{COLORS['success']}!important; font-size:0.8rem; font-weight:bold;">100% MATCH</p>
        <p style="font-size:0.8rem;">Uses: Eggs, Spinach, Tomatoes</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Select Omelet"):
        nav("RECIPE")

    # Result 2 (Missing)
    st.markdown(f"""
    <div class="binder-card" style="border-left-color: {COLORS['secondary']}">
        <h4>Chicken Salad</h4>
        <p style="color:{COLORS['secondary']}!important; font-size:0.8rem; font-weight:bold;">MISSING 1 ITEM</p>
        <p style="font-size:0.8rem;">Missing: Olive Oil</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Select Salad")

def page_recipe():
    # Hero
    st.markdown(f"<div style='height:150px; background:#333; margin:-20px -20px 20px -20px;'></div>", unsafe_allow_html=True)
    
    st.title("MEDITERRANEAN OMELET")
    st.markdown("**10 min • Easy • 320 Cal**")
    
    st.markdown("---")
    st.markdown("### INGREDIENTS")
    st.markdown("✅ Eggs (Have)\n✅ Spinach (Have)\n✅ Tomatoes (Have)")
    
    if st.button("COOK THIS"):
        nav("GUIDED")
        
    st.markdown("---")
    st.markdown("### STEPS")
    st.markdown("1. Whisk eggs.\n2. Chop veggies.\n3. Cook on medium heat.")

def page_guided():
    st.title("STEP 1/3")
    
    st.markdown(f"""
    <div style="height:300px; display:flex; align-items:center; justify-content:center; text-align:center;">
        <h1>WHISK<br>THE EGGS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("NEXT STEP"):
        st.balloons()
        time.sleep(1)
        nav("HOME")

def page_plan():
    st.title("WEEKLY PLAN")
    st.markdown("Generate a plan from your leftovers.")
    
    # Upsell
    st.markdown(f"""
    <div style="background: linear-gradient(45deg, {COLORS['secondary']}, {COLORS['primary']}); padding:2px; border-radius:12px; margin:20px 0;">
        <div style="background:{COLORS['bg']}; padding:20px; border-radius:10px; text-align:center;">
            <h3>UNLOCK AI PLANNER</h3>
            <p>Get zero-waste meal plans.</p>
            <h2 style="color:white!important;">$7.99/mo</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.button("START FREE TRIAL")
    st.button("View Free Grocery List")

def page_profile():
    st.title("PROFILE")
    st.markdown("### Yvette Luo")
    st.caption("Intermediate Chef")
    
    st.markdown("---")
    st.button("Dietary Preferences")
    st.button("Saved Recipes")
    st.button("Manage Subscription")
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("Log Out")

# --- 4. NAVIGATION BAR (Bottom) ---
def render_nav():
    # We use a custom HTML block for the sticky nav at the bottom of the "phone"
    # Note: Streamlit buttons inside HTML don't work easily, so we use st.columns at the bottom of the page
    # mimicking a sticky footer in the main flow.
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("🏠", key="n1"): nav("HOME")
    with c2:
        if st.button("📸", key="n2"): nav("SCAN_CAMERA")
    with c3:
        if st.button("📅", key="n3"): nav("PLAN")
    with c4:
        if st.button("👤", key="n4"): nav("PROFILE")

# --- 5. MAIN ROUTER ---
if st.session_state.page == 'SPLASH':
    page_splash()
elif st.session_state.page == 'ONBOARDING_1':
    page_onboarding_1()
elif st.session_state.page == 'ONBOARDING_2':
    page_onboarding_2()
elif st.session_state.page == 'ONBOARDING_3':
    page_onboarding_3()
elif st.session_state.page == 'HOME':
    page_home()
    render_nav()
elif st.session_state.page == 'SCAN_CAMERA':
    page_scan_camera()
elif st.session_state.page == 'SCAN_INGREDIENTS':
    page_scan_ingredients()
elif st.session_state.page == 'SCAN_DISH_BREAKDOWN':
    st.info("Dish breakdown simulation...")
    if st.button("Make Recipe"): nav("RECIPE")
elif st.session_state.page == 'SCAN_RESULTS':
    page_scan_results()
    render_nav()
elif st.session_state.page == 'RECIPE':
    page_recipe()
elif st.session_state.page == 'GUIDED':
    page_guided()
elif st.session_state.page == 'PLAN':
    page_plan()
    render_nav()
elif st.session_state.page == 'PROFILE':
    page_profile()
    render_nav()