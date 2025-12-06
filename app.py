import streamlit as st
import time
import random

# --- 1. APP CONFIGURATION & STYLE ---
st.set_page_config(page_title="SnapDish Prototype", page_icon="📸", layout="centered")

# Visual System (from Pitch Deck)
COLORS = {
    "bg": "#050606",          # Near Black
    "frame": "#1a1a1a",       # Phone Frame
    "primary": "#FF5A36",     # Coral/Orange (Pentagon)
    "secondary": "#C68E5D",   # Warm Tan/Camel (Headings)
    "accent": "#3B6E8F",      # Teal Green (Triangle)
    "text_main": "#EAE0D5",   # Bone/Off-white
    "text_sub": "#9CA3AF",    # Soft Light Gray
    "danger": "#FF0055"       # Magenta
}

# CSS to enforce the iPhone Preview and "Vibe"
st.markdown(f"""
    <style>
    /* 1. Global Reset */
    .stApp {{
        background-color: #222; /* Desktop Background */
    }}
    
    /* 2. The iPhone Frame Container */
    .iphone-container {{
        background-color: {COLORS['bg']};
        border-radius: 40px;
        border: 8px solid {COLORS['frame']};
        padding: 20px;
        box-shadow: 0px 0px 50px rgba(0,0,0,0.7);
        min-height: 850px;
        font-family: 'Helvetica Neue', sans-serif;
    }}
    
    /* 3. Typography & Headings (Editorial Vibe) */
    h1, h2, h3 {{
        color: {COLORS['secondary']} !important;
        font-family: 'Arial Narrow', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    
    p, label, span, div {{
        color: {COLORS['text_main']};
    }}

    /* 4. Custom Component Styles */
    .primary-btn {{
        background-color: {COLORS['primary']};
        color: white;
        padding: 15px;
        border-radius: 30px;
        text-align: center;
        font-weight: bold;
        text-transform: uppercase;
        margin-top: 10px;
        cursor: pointer;
        border: none;
    }}
    
    .card {{
        background-color: rgba(255,255,255,0.05);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
    }}

    .tag {{
        display: inline-block;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        margin-right: 5px;
        font-weight: bold;
    }}

    /* Streamlit overrides */
    div[data-testid="stButton"] button {{
        width: 100%;
        border-radius: 30px;
        background-color: {COLORS['primary']};
        color: white;
        border: none;
        font-weight: bold;
        padding: 12px 0;
    }}
    div[data-testid="stButton"] button:hover {{
        background-color: {COLORS['danger']};
        color: white;
    }}
    
    /* Hide default Streamlit chrome */
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    </style>
""", unsafe_allow_html=True)

# --- 2. SESSION STATE MANAGEMENT ---
# This acts as the app's "Brain" / Database
if 'page' not in st.session_state:
    st.session_state.page = 'SPLASH'
if 'user' not in st.session_state:
    st.session_state.user = {
        'goals': [],
        'diet': [],
        'allergies': [],
        'skill': 'Intermediate',
        'name': 'Yvette'
    }
if 'inventory' not in st.session_state:
    st.session_state.inventory = [] # Detected ingredients
if 'scan_mode' not in st.session_state:
    st.session_state.scan_mode = 'FRIDGE' # or DISH

def navigate(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- 3. UI COMPONENT HELPERS ---
def header(text):
    st.markdown(f"<h2 style='margin-bottom: 5px;'>{text}</h2>", unsafe_allow_html=True)

def subheader(text):
    st.markdown(f"<p style='color: {COLORS['secondary']}; font-weight: bold; font-size: 0.9rem; text-transform: uppercase;'>{text}</p>", unsafe_allow_html=True)

def bottom_nav():
    st.markdown("---")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("🏠", key="nav_home"): navigate("HOME")
    with c2:
        if st.button("📸", key="nav_scan"): navigate("SCAN_ENTRY")
    with c3:
        if st.button("📅", key="nav_plan"): navigate("PLAN")
    with c4:
        if st.button("👤", key="nav_profile"): navigate("PROFILE")

# --- 4. SCREEN RENDERERS ---

def screen_splash():
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; font-size: 4rem; color: {COLORS['primary']} !important;'>SNAP<br>DISH</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: {COLORS['text_sub']};'>One picture. One recipe.<br>Zero thinking.</p>", unsafe_allow_html=True)
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    if st.button("GET STARTED"):
        navigate("ONBOARDING_1")
    
    st.markdown(f"<p style='text-align: center; font-size: 0.8rem; margin-top: 20px;'>Already have an account? <span style='color:{COLORS['secondary']}'>Log in</span></p>", unsafe_allow_html=True)

def screen_onboarding_1():
    header("GOALS")
    st.progress(25)
    st.markdown(f"<p style='font-size: 1.2rem;'>What do you want SnapDish to help with?</p>", unsafe_allow_html=True)
    
    goals = st.multiselect("Select all that apply", 
                           ["Reduce food waste", "Decide what to cook", "Eat healthier", "Save time"],
                           default=["Reduce food waste"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("NEXT"):
        st.session_state.user['goals'] = goals
        navigate("ONBOARDING_2")

def screen_onboarding_2():
    header("PREFERENCES")
    st.progress(50)
    
    subheader("Diet")
    diet = st.selectbox("I eat...", ["Omnivore", "Vegetarian", "Vegan", "Halal", "Kosher"])
    
    subheader("Allergies")
    allergies = st.multiselect("Avoid...", ["Nuts", "Dairy", "Gluten", "Shellfish"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("NEXT"):
        st.session_state.user['diet'] = diet
        st.session_state.user['allergies'] = allergies
        navigate("ONBOARDING_3")

def screen_onboarding_3():
    header("CONTEXT")
    st.progress(75)
    
    subheader("Cooking Skill")
    st.select_slider("Skill Level", options=["Beginner", "Intermediate", "Confident"], value="Intermediate")
    
    subheader("Time per meal")
    st.select_slider("Minutes", options=["15", "30", "45+"], value="30")
    
    subheader("Cooking for")
    st.radio("People", ["Just me", "Me + 1", "Family (3-4)"], horizontal=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("CREATE ACCOUNT"):
        navigate("HOME")

def screen_home():
    # Top
    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown(f"<h1 style='margin:0;'>HI {st.session_state.user['name'].upper()} 👋</h1>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div style='width:40px; height:40px; border-radius:50%; background:{COLORS['secondary']}; text-align:center; padding-top:10px; color:black; font-weight:bold;'>YL</div>", unsafe_allow_html=True)
    
    # Hero CTA
    st.markdown(f"""
        <div style="background-color: {COLORS['card_bg'] if 'card_bg' in COLORS else '#111'}; border: 1px dashed {COLORS['secondary']}; border-radius: 20px; padding: 30px; text-align: center; margin: 20px 0;">
            <div style="font-size: 3rem;">📸</div>
            <h3 style="color: {COLORS['text_main']} !important; margin: 10px 0;">HUNGRY?</h3>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("SNAP MY FRIDGE"):
        st.session_state.scan_mode = 'FRIDGE'
        navigate("SCAN_CAMERA")
        
    if st.button("SCAN A DISH"):
        st.session_state.scan_mode = 'DISH'
        navigate("SCAN_CAMERA")

    # Mid Section
    st.markdown("<br>", unsafe_allow_html=True)
    subheader("Tonight's Quick Picks")
    
    # Recipe Card 1
    st.markdown(f"""
    <div class="card">
        <div style="height: 100px; background: #333; border-radius: 8px; margin-bottom: 10px;"></div>
        <div style="display:flex; justify-content:space-between;">
            <strong>Spicy Tofu Bowl</strong>
            <span style="color:{COLORS['primary']}">15 min</span>
        </div>
        <div style="margin-top: 5px;">
            <span class="tag" style="background:{COLORS['accent']}; color:white;">High Protein</span>
            <span class="tag" style="border:1px solid {COLORS['secondary']}; color:{COLORS['secondary']};">Budget</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("View Recipe"):
        navigate("RECIPE_DETAIL")
        
    bottom_nav()

def screen_scan_camera():
    header("SCAN MODE")
    
    # Toggle
    mode = st.session_state.scan_mode
    c1, c2 = st.columns(2)
    with c1:
        if st.button("FRIDGE", disabled=(mode=='FRIDGE')): st.session_state.scan_mode = 'FRIDGE'; st.rerun()
    with c2:
        if st.button("DISH", disabled=(mode=='DISH')): st.session_state.scan_mode = 'DISH'; st.rerun()

    # Camera View
    st.markdown(f"""
    <div style="height: 350px; border: 2px solid {COLORS['text_main']}; border-radius: 20px; display: flex; align-items: center; justify-content: center; flex-direction: column; background: #000;">
        <span style="font-size: 3rem;">🔭</span>
        <p style="text-align: center; padding: 20px;">
            {'Point at your fridge ingredients.' if mode == 'FRIDGE' else 'Point at a finished dish.'}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("⚪ SHUTTER"):
        with st.spinner("AI Processing..."):
            time.sleep(1.5)
            if mode == 'FRIDGE':
                st.session_state.inventory = ["Eggs", "Spinach", "Tomatoes", "Rice"]
                navigate("SCAN_INGREDIENTS")
            else:
                st.session_state.inventory = ["Chicken", "Brown Rice", "Broccoli", "Soy Sauce"] # dish breakdown
                navigate("SCAN_DISH_BREAKDOWN")

    if st.button("Cancel"):
        navigate("HOME")

def screen_scan_ingredients():
    header("WE SEE...")
    
    # Ingredient Grid
    col1, col2 = st.columns(2)
    for i, item in enumerate(st.session_state.inventory):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"<div class='card' style='text-align:center;'>{item} ✅</div>", unsafe_allow_html=True)
            
    st.text_input("Add missing:", placeholder="e.g. Tofu")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("SEE RECIPES"):
        navigate("SCAN_RESULTS")
    
    if st.button("RESCAN"):
        navigate("SCAN_CAMERA")

def screen_scan_results():
    header("COOK TONIGHT")
    
    # Filters
    st.markdown(f"""
    <div style="display: flex; gap: 10px; overflow-x: auto; padding-bottom: 10px;">
        <span class="tag" style="border:1px solid {COLORS['accent']}; color:{COLORS['accent']};">High Protein</span>
        <span class="tag" style="border:1px solid {COLORS['primary']}; color:{COLORS['primary']};">Quick</span>
        <span class="tag" style="border:1px solid {COLORS['secondary']}; color:{COLORS['secondary']};">Vegan</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Result 1
    st.markdown(f"""
    <div class="card" style="border-left: 5px solid {COLORS['primary']}">
        <div style="display:flex; justify-content:space-between;">
            <h3 style="margin:0; font-size:1.2rem;">Mediterranean Omelet</h3>
            <span>100% Match</span>
        </div>
        <p style="font-size: 0.8rem; margin: 5px 0;">Uses: Eggs, Spinach, Tomatoes</p>
        <div style="display: flex; gap: 5px;">
             <span class="tag" style="background:{COLORS['card_bg']};">10 min</span>
             <span class="tag" style="background:{COLORS['card_bg']};">Easy</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Cook Omelet"):
        navigate("RECIPE_DETAIL")
        
    # Result 2
    st.markdown(f"""
    <div class="card" style="border-left: 5px solid {COLORS['secondary']}">
        <div style="display:flex; justify-content:space-between;">
            <h3 style="margin:0; font-size:1.2rem;">Fried Rice</h3>
            <span>Missing: Soy Sauce</span>
        </div>
        <p style="font-size: 0.8rem; margin: 5px 0;">Uses: Rice, Eggs, Spinach</p>
    </div>
    """, unsafe_allow_html=True)

    bottom_nav()

def screen_recipe_detail():
    # Hero Image
    st.markdown(f"<div style='height: 200px; background: #333; border-radius: 0 0 20px 20px; margin: -20px -20px 20px -20px;'></div>", unsafe_allow_html=True)
    
    header("MEDITERRANEAN OMELET")
    st.markdown(f"""
    <div style="display: flex; gap: 15px; margin-bottom: 20px;">
        <span>⏱️ 10 min</span>
        <span>🔥 320 cal</span>
        <span>👨‍🍳 Easy</span>
    </div>
    """, unsafe_allow_html=True)
    
    subheader("What you'll use")
    st.markdown("""
    - ✅ **Eggs** (You have)
    - ✅ **Spinach** (You have)
    - ✅ **Tomatoes** (You have)
    - ❌ **Salt & Pepper** (Missing)
    """)
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.button("+ Shop")
    with c2:
        if st.button("COOK THIS"):
            navigate("GUIDED_MODE")
            
    st.markdown("---")
    subheader("Steps")
    st.markdown("""
    1. Whisk eggs in a bowl.
    2. Chop spinach and tomatoes.
    3. Heat pan and pour eggs.
    """)
    
    st.markdown("---")
    subheader("Nutrition")
    st.progress(80)
    st.caption("High Protein Goal met!")

    if st.button("← Back"):
        navigate("HOME")

def screen_guided_mode():
    header("STEP 1/3")
    st.markdown(f"""
    <div style="height: 400px; display: flex; align-items: center; justify-content: center; text-align: center;">
        <h1 style="color: white !important;">WHISK EGGS<br>IN A BOWL</h1>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("NEXT STEP"):
        st.toast("Cooking Complete! Streak +1")
        time.sleep(1)
        navigate("HOME")

def screen_plan():
    header("WEEKLY PLAN")
    
    # Calendar Grid Mockup
    days = ["M", "T", "W", "T", "F", "S", "S"]
    cols = st.columns(7)
    for i, d in enumerate(days):
        with cols[i]:
            st.markdown(f"<div style='text-align:center; font-weight:bold; color:{COLORS['secondary']}'>{d}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='height:30px; background:#333; margin-top:5px; border-radius:4px;'></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("✨ GENERATE PLAN"):
        with st.expander("Plan Options", expanded=True):
            st.markdown("How many meals?")
            st.slider("Meals", 3, 21, 5)
            st.markdown("Budget Priority?")
            st.select_slider("Budget", ["Low", "Med", "High"])
            if st.button("Create Plan"):
                st.success("Plan Generated!")
                
    subheader("Grocery List")
    st.checkbox("Olive Oil")
    st.checkbox("Chicken Breast")
    st.checkbox("Garlic")
    
    if st.button("Export to Instacart"):
        st.toast("Link copied!")
        
    bottom_nav()

def screen_profile():
    header("PROFILE")
    
    col1, col2 = st.columns([1, 3])
    with col1:
         st.markdown(f"<div style='width:60px; height:60px; border-radius:50%; background:{COLORS['secondary']}; text-align:center; padding-top:15px; font-weight:bold; font-size:1.5rem; color:black;'>YL</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("### Yvette Luo\nIntermediate Chef")

    st.markdown("---")
    
    # Subscription Card
    st.markdown(f"""
    <div style="border: 2px solid {COLORS['primary']}; border-radius: 12px; padding: 20px; background: rgba(255, 90, 54, 0.1);">
        <h3 style="color: {COLORS['primary']} !important;">GET PREMIUM</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li>✅ Unlimited AI Scans</li>
            <li>✅ Macro Tracking</li>
            <li>✅ Zero-Waste Plans</li>
        </ul>
        <h2 style="color: white !important;">$7.99/mo</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.button("START 7-DAY FREE TRIAL")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("Edit Preferences")
    st.button("Log Out")
    
    bottom_nav()

# --- 5. MAIN APP EXECUTION ---

# Create a central column to act as the "Phone Screen"
c_left, c_main, c_right = st.columns([1, 2, 1])

with c_main:
    # Open the Phone Container
    st.markdown('<div class="iphone-container">', unsafe_allow_html=True)
    
    # Router
    if st.session_state.page == 'SPLASH': screen_splash()
    elif st.session_state.page == 'ONBOARDING_1': screen_onboarding_1()
    elif st.session_state.page == 'ONBOARDING_2': screen_onboarding_2()
    elif st.session_state.page == 'ONBOARDING_3': screen_onboarding_3()
    elif st.session_state.page == 'HOME': screen_home()
    elif st.session_state.page == 'SCAN_ENTRY': 
        st.session_state.scan_mode = 'FRIDGE' # Default
        screen_scan_camera()
    elif st.session_state.page == 'SCAN_CAMERA': screen_scan_camera()
    elif st.session_state.page == 'SCAN_INGREDIENTS': screen_scan_ingredients()
    elif st.session_state.page == 'SCAN_DISH_BREAKDOWN': 
        st.info("Dish Breakdown: Chicken, Rice, Broccoli")
        if st.button("Create Recipe"): navigate("RECIPE_DETAIL")
    elif st.session_state.page == 'SCAN_RESULTS': screen_scan_results()
    elif st.session_state.page == 'RECIPE_DETAIL': screen_recipe_detail()
    elif st.session_state.page == 'GUIDED_MODE': screen_guided_mode()
    elif st.session_state.page == 'PLAN': screen_plan()
    elif st.session_state.page == 'PROFILE': screen_profile()

    # Close the Phone Container
    st.markdown('</div>', unsafe_allow_html=True)