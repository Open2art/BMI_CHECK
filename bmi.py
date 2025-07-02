import streamlit as st

# --- CONFIG PAGE ---
st.set_page_config(page_title="Calculateur de Poids Santé / Health Weight Calculator",
                   page_icon="💪", layout="centered")

# --- Translations ---
TEXTS = {
    "fr": {
        "title": "💪 Calculateur de Poids Santé",
        "subtitle": "Calculez votre IMC, masse grasse et recevez des conseils santé adaptés à vos objectifs.",
        "header_info": "📝 Vos Informations",
        "sex": "Sexe",
        "age": "Âge",
        "height": "Taille (cm)",
        "weight": "Poids (kg)",
        "waist": "Tour de taille (cm)",
        "goal": "🎯 Objectif",
        "goals": ["Perte de poids", "Prise de masse", "Rester fit"],
        "results": "📊 Résultats",
        "bmi": "IMC",
        "interpretation": "Interprétation",
        "body_fat": "Masse grasse estimée",
        "selected_goal": "Objectif sélectionné",
        "health_tips": "💡 Conseils Santé",
        "advice_loss": [
            "Adoptez un léger déficit calorique (-300 à -500 kcal/jour)",
            "Faites 3 à 5 séances de cardio ou HIIT par semaine",
            "Privilégiez les légumes, protéines maigres et aliments non transformés"
        ],
        "advice_gain": [
            "Augmentez votre apport calorique (+300 à +500 kcal/jour)",
            "Entraînez-vous en musculation 4 à 6 fois/semaine",
            "Consommez suffisamment de protéines (1.6 à 2.2 g/kg)"
        ],
        "advice_fit": [
            "Maintenez une alimentation équilibrée et variée",
            "Soyez actif quotidiennement (marche, sport doux, musculation légère)",
            "Surveillez votre poids tous les mois pour rester dans votre zone de confort"
        ],
        "sex_options": ["Homme", "Femme"],
        "bmi_categories": [
            (18.5, "Insuffisance pondérale", "🔵"),
            (25, "Poids normal", "🟢"),
            (30, "Surpoids", "🟠"),
            (float('inf'), "Obésité", "🔴"),
        ],
        "tabs": ["Résultats", "Conseils Santé"],
        "language": "Langue",
        "theme": "Thème",
        "light": "Clair",
        "dark": "Sombre",
    },
    "en": {
        "title": "💪 Health Weight Calculator",
        "subtitle": "Calculate your BMI, body fat %, and get tailored health advice based on your goals.",
        "header_info": "📝 Your Information",
        "sex": "Sex",
        "age": "Age",
        "height": "Height (cm)",
        "weight": "Weight (kg)",
        "waist": "Waist circumference (cm)",
        "goal": "🎯 Goal",
        "goals": ["Weight loss", "Muscle gain", "Stay fit"],
        "results": "📊 Results",
        "bmi": "BMI",
        "interpretation": "Interpretation",
        "body_fat": "Estimated Body Fat",
        "selected_goal": "Selected Goal",
        "health_tips": "💡 Health Tips",
        "advice_loss": [
            "Adopt a slight calorie deficit (-300 to -500 kcal/day)",
            "Do 3 to 5 cardio or HIIT sessions per week",
            "Favor vegetables, lean proteins, and unprocessed foods"
        ],
        "advice_gain": [
            "Increase your calorie intake (+300 to +500 kcal/day)",
            "Train with weightlifting 4 to 6 times/week",
            "Consume enough protein (1.6 to 2.2 g/kg)"
        ],
        "advice_fit": [
            "Maintain a balanced and varied diet",
            "Be active daily (walking, light sport, gentle strength training)",
            "Monitor your weight monthly to stay in your comfort zone"
        ],
        "sex_options": ["Male", "Female"],
        "bmi_categories": [
            (18.5, "Underweight", "🔵"),
            (25, "Normal weight", "🟢"),
            (30, "Overweight", "🟠"),
            (float('inf'), "Obesity", "🔴"),
        ],
        "tabs": ["Results", "Health Tips"],
        "language": "Language",
        "theme": "Theme",
        "light": "Light",
        "dark": "Dark",
    }
}

# --- Themes ---
THEMES = {
    "light": {
        "background_image": "https://images.pexels.com/photos/1552242/pexels-photo-1552242.jpeg",
        "text_color": "#003366",
        "container_bg": "rgba(255, 255, 255, 0.9)",
        "result_bg": "#e0f7fa",
        "blur": 0,
        "button_bg": "#0072b1",
        "button_color": "#ffffff",
        "button_hover": "#005f8d",
    },
    "dark": {
        "background_image": "https://images.pexels.com/photos/1552242/pexels-photo-1552242.jpeg",
        "text_color": "#a0c8f0",
        "container_bg": "rgba(20, 30, 50, 0.85)",
        "result_bg": "rgba(10, 25, 45, 0.6)",
        "blur": 4,
        "button_bg": "#1e90ff",
        "button_color": "#e0e0e0",
        "button_hover": "#5599ff",
    }
}

# --- SIDEBAR LANGUE & THEME ---
with st.sidebar:
    lang = st.selectbox(label="🌐 " + "Language / Langue", options=["fr", "en"], index=0)
    theme = st.radio(label="🌗 " + TEXTS[lang]["theme"], options=["light", "dark"], index=0)

t = TEXTS[lang]
th = THEMES[theme]

# --- CSS dynamique ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: url("{th['background_image']}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        color: {th['text_color']};
    }}
    .block-container {{
        backdrop-filter: blur({th['blur']}px);
        background-color: {th['container_bg']};
        border-radius: 12px;
        padding: 2rem;
        color: {th['text_color']};
    }}
    h1, h2, h3 {{
        color: {th['text_color']};
    }}
    .stSelectbox label, .stTextInput label, .stSlider label {{
        font-weight: bold;
        color: {th['text_color']};
    }}
    .result {{
        background-color: {th['result_bg']};
        padding: 15px;
        border-radius: 8px;
        color: {th['text_color']};
    }}
    .tab-buttons {{
        display: flex;
        gap: 15px;
        margin-bottom: 1rem;
    }}
    .tab-button {{
        flex: 1;
        padding: 10px 0;
        background-color: {th['button_bg']};
        color: {th['button_color']};
        font-weight: bold;
        border-radius: 10px;
        cursor: pointer;
        text-align: center;
        user-select: none;
        transition: background-color 0.3s ease;
    }}
    .tab-button:hover {{
        background-color: {th['button_hover']};
    }}
    .tab-button.selected {{
        box-shadow: 0 0 8px 2px {th['button_color']};
        font-size: 1.1rem;
    }}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.title(t["title"])
st.markdown(t["subtitle"])

# --- USER INPUT ---
st.header(t["header_info"])
col1, col2 = st.columns(2)
with col1:
    sexe = st.selectbox(t["sex"], t["sex_options"])
    age = st.number_input(t["age"], min_value=10, max_value=100, value=30)
with col2:
    taille = st.number_input(t["height"], min_value=100, max_value=250, value=170)
    poids = st.number_input(t["weight"], min_value=30, max_value=200, value=70)

objectif = st.selectbox(t["goal"], t["goals"])
tour_taille = st.slider(t["waist"], 50, 150, 80)

# --- CALCULATIONS ---
taille_m = taille / 100
imc = poids / (taille_m ** 2)

if sexe == t["sex_options"][0]:
    mg = 64 - 20 * (taille_m / (tour_taille / 100))
else:
    mg = 76 - 20 * (taille_m / (tour_taille / 100))
mg = max(5, round(mg, 1))

def interpretation_imc(imc_val):
    for seuil, texte, emoji in t["bmi_categories"]:
        if imc_val < seuil:
            return texte, emoji
    return "", ""

interpret, emoji = interpretation_imc(imc)

# --- Results / Tips tabs with buttons ---
if "active_tab" not in st.session_state:
    st.session_state.active_tab = t["tabs"][0]

col1, col2 = st.columns(2)
with col1:
    if st.button(t["tabs"][0]):
        st.session_state.active_tab = t["tabs"][0]
with col2:
    if st.button(t["tabs"][1]):
        st.session_state.active_tab = t["tabs"][1]



# --- Display sections ---
if st.session_state.active_tab == t["tabs"][0]:
    st.header(t["results"])
    st.markdown(f"""
    <div class='result'>
        <h3>{t["bmi"]} : {imc:.1f} {emoji}</h3>
        <p><strong>{t["interpretation"]} :</strong> {interpret}</p>
        <p><strong>{t["body_fat"]} :</strong> {mg}%</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.header(t["health_tips"])

    def conseils(obj):
        if obj == t["goals"][0]:
            return t["advice_loss"]
        elif obj == t["goals"][1]:
            return t["advice_gain"]
        else:
            return t["advice_fit"]
    
     # Store advice as an HTML list
    conseils_html = "".join(f"<li>✅ {conseil}</li>" for conseil in conseils(objectif))

    # Display advice block with style
    st.markdown(f"""
    <div class='result'>
        <h3>{t['selected_goal']} : {objectif}</h3>
        <ul>
            {conseils_html}
        </ul>
    </div>
    """, unsafe_allow_html=True)