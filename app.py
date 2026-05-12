"""
Kathmandu Ride Demand Forecaster
Author: Sudeep | Biratnagar, Nepal | 2025
A premium dark dashboard Streamlit app for ride demand prediction.
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go
import plotly.express as px

# ──────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Kathmandu Ride Demand Forecaster",
    page_icon="🛵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# CUSTOM CSS — Dark Premium Glassmorphism
# ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap');

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background: #0e1416;
    background-image: radial-gradient(circle at 2px 2px, rgba(76,214,251,0.04) 1px, transparent 0);
    background-size: 24px 24px;
}

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: rgba(23,28,31,0.95) !important;
    border-right: 1px solid rgba(61,73,77,0.4);
}
[data-testid="stSidebar"] * { color: #dee3e6 !important; }
[data-testid="stSidebar"] .stSelectbox > div > div,
[data-testid="stSidebar"] .stSlider > div { color: #dee3e6 !important; }

/* ── Glassmorphism card base ── */
.glass-card {
    background: rgba(48,54,56,0.55);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(134,147,152,0.18);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 16px;
}

/* ── Metric cards ── */
.metric-card {
    background: rgba(48,54,56,0.55);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(134,147,152,0.18);
    border-radius: 12px;
    padding: 20px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.metric-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 32px rgba(76,214,251,0.12);
}
.metric-card.blue  { border-left: 4px solid #4cd6fb; }
.metric-card.orange{ border-left: 4px solid #ff6b35; }
.metric-card.green { border-left: 4px solid #2ecc71; }
.metric-card.purple{ border-left: 4px solid #a855f7; }

.metric-icon  { font-size: 26px; margin-bottom: 8px; }
.metric-value {
    font-size: 26px; font-weight: 700;
    color: #dee3e6; font-family: 'JetBrains Mono', monospace;
}
.metric-label {
    font-size: 11px; font-weight: 500; letter-spacing: 0.08em;
    text-transform: uppercase; color: #869398; margin-top: 4px;
}

/* ── Header ── */
.app-header {
    padding: 24px 0 16px;
    border-bottom: 1px solid rgba(61,73,77,0.4);
    margin-bottom: 24px;
}
.app-title {
    font-size: 36px; font-weight: 700; color: #dee3e6;
    letter-spacing: -0.02em; margin: 0;
}
.app-subtitle {
    font-size: 16px; color: #869398; margin-top: 6px;
}
.info-banner {
    background: rgba(76,214,251,0.08);
    border: 1px solid rgba(76,214,251,0.25);
    border-radius: 10px; padding: 12px 18px;
    color: #4cd6fb; font-size: 14px; margin-top: 16px;
}

/* ── Prediction result card ── */
.pred-card {
    background: rgba(48,54,56,0.65);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(134,147,152,0.18);
    border-radius: 20px; padding: 36px;
    position: relative; overflow: hidden;
    margin-bottom: 24px;
}
.pred-number {
    font-size: 80px; font-weight: 800; line-height: 1;
    font-family: 'JetBrains Mono', monospace;
}
.pred-badge {
    display: inline-block;
    padding: 5px 14px; border-radius: 99px;
    font-size: 12px; font-weight: 700;
    letter-spacing: 0.1em; margin-bottom: 16px;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.7; }
}
.pred-recommendation {
    background: rgba(0,0,0,0.25);
    border-radius: 10px; padding: 14px 18px;
    color: #bcc9ce; font-size: 15px; margin-top: 20px;
    border-left: 3px solid currentColor;
}

/* ── Section titles ── */
.section-title {
    font-size: 18px; font-weight: 600;
    color: #dee3e6; margin-bottom: 16px;
    letter-spacing: -0.01em;
}

/* ── Predict button ── */
.stButton > button {
    background: linear-gradient(135deg, #ff6b35 0%, #eb8f3b 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    padding: 14px 0 !important;
    width: 100% !important;
    box-shadow: 0 4px 20px rgba(255,107,53,0.3) !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(255,107,53,0.45) !important;
}
.stButton > button:active { transform: scale(0.97) !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #0e1416; }
::-webkit-scrollbar-thumb { background: #3d494d; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #4cd6fb; }

/* ── Input widgets text color fix ── */
.stSelectbox label, .stSlider label,
.stCheckbox label, .stNumberInput label { color: #dee3e6 !important; }
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# CONSTANTS
# ──────────────────────────────────────────────
BASE_PATH = r"D:\projects\Ride-demand-forecasting"

ZONES = [
    "Thamel","Baneshwor","Koteshwor","Lalitpur","Bhaktapur",
    "Balaju","Kalanki","Chabahil","Maharajgunj","Patan",
    "Boudha","Kirtipur",
]
WEATHER_OPTIONS = ["Clear", "Rain", "Fog"]
DAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]

# Plotly dark chart defaults
CHART_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#dee3e6", family="Inter"),
    margin=dict(l=10, r=10, t=40, b=10),
    xaxis=dict(gridcolor="rgba(255,255,255,0.07)", showline=False),
    yaxis=dict(gridcolor="rgba(255,255,255,0.07)", showline=False),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=12)),
)

# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────
def safe_encode(le, value):
    """Safely encode a label; return 0 if unseen."""
    classes = list(le.classes_)
    return classes.index(value) if value in classes else 0

def demand_level(rides: float):
    """Return (level, color, emoji, recommendation) for a demand value."""
    if rides <= 20:
        return "LOW",    "#2ecc71", "🟢", "Normal operations — standard fleet is sufficient."
    elif rides <= 50:
        return "MEDIUM", "#f1c40f", "🟡", "Deploy an additional 20% of drivers to meet demand."
    elif rides <= 80:
        return "HIGH",   "#ff6b35", "🟠", "Surge pricing recommended + extra fleet dispatch."
    else:
        return "PEAK",   "#e74c3c", "🔴", "Maximum fleet deployment + aggressive surge pricing."

@st.cache_resource(show_spinner=False)
def load_model():
    """Load pkl model artefacts once and cache them."""
    import os
    def p(name): return os.path.join(BASE_PATH, name)
    with open(p("demand_model.pkl"), "rb") as f: model = pickle.load(f)
    with open(p("le_zone.pkl"),      "rb") as f: le_zone = pickle.load(f)
    with open(p("le_weather.pkl"),   "rb") as f: le_weather = pickle.load(f)
    with open(p("features.pkl"),     "rb") as f: features = pickle.load(f)
    return model, le_zone, le_weather, features

@st.cache_data(show_spinner=False)
def load_data():
    """Load and lightly preprocess the CSV."""
    import os
    df = pd.read_csv(os.path.join(BASE_PATH, "kathmandu_rides.csv"))
    df.columns = [c.strip().lower() for c in df.columns]
    return df

def glass_metric(icon, value, label, color_class):
    return f"""
    <div class="metric-card {color_class}">
        <div class="metric-icon">{icon}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>"""

# ──────────────────────────────────────────────
# LOAD ASSETS
# ──────────────────────────────────────────────
with st.spinner("Loading model & data…"):
    try:
        model, le_zone, le_weather, features = load_model()
        df = load_data()
        load_ok = True
    except Exception as e:
        st.error(f"❌ Failed to load files: {e}")
        load_ok = False
        st.stop()

# ──────────────────────────────────────────────
# HEADER
# ──────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <h1 class="app-title">🛵 Kathmandu Ride Demand Forecaster</h1>
    <p class="app-subtitle">AI-powered ride demand prediction for Kathmandu zones</p>
    <div class="info-banner">
        ℹ️ Built using a Gradient Boosting ML model trained on
        <strong>51,840 ride records</strong> across
        <strong>12 Kathmandu zones</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# SIDEBAR — PREDICTION INPUTS
# ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="margin-bottom:24px;">
        <h2 style="color:#4cd6fb;font-size:20px;font-weight:700;margin:0;">
            🔮 Predict Demand
        </h2>
        <p style="color:#869398;font-size:11px;font-family:'JetBrains Mono',monospace;
                  letter-spacing:0.08em;margin-top:4px;">V1.0 · KATHMANDU VALLEY</p>
    </div>
    """, unsafe_allow_html=True)

    zone      = st.selectbox("📍 Zone", ZONES)
    hour      = st.slider("⏰ Hour of Day", 0, 23, 8)
    day_name  = st.selectbox("📅 Day of Week", DAYS)
    month_name= st.selectbox("🗓️ Month", MONTHS)
    weather   = st.selectbox("🌤️ Weather", WEATHER_OPTIONS)
    temp      = st.slider("🌡️ Temperature (°C)", 10, 35, 22)
    is_weekend   = st.checkbox("🏖️ Weekend")
    is_festival  = st.checkbox("🎉 Festival Day")

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)
    predict_clicked = st.button("🔍 Predict Demand")

# Map day/month names → integers
day_of_week = DAYS.index(day_name)           # 0=Mon … 6=Sun
month_num   = MONTHS.index(month_name) + 1  # 1-12
week_num    = ((month_num - 1) * 4) + (hour // 6) + 1  # rough week approx

# ──────────────────────────────────────────────
# PRE-COMPUTE DASHBOARD METRICS
# ──────────────────────────────────────────────
zone_avg   = df.groupby("zone")["demand"].mean()
busiest_zone = zone_avg.idxmax()

hour_avg   = df.groupby("hour")["demand"].mean()
peak_hour  = int(hour_avg.idxmax())

weather_avg = df.groupby("weather")["demand"].mean()
best_weather = weather_avg.idxmax()

weekend_avg  = df[df["is_weekend"] == 1]["demand"].mean()
weekday_avg  = df[df["is_weekend"] == 0]["demand"].mean()
wknd_diff    = ((weekend_avg - weekday_avg) / weekday_avg * 100)
wknd_label   = f"+{wknd_diff:.1f}%" if wknd_diff >= 0 else f"{wknd_diff:.1f}%"
total_rides  = f"{len(df):,}"
avg_demand   = f"{df['demand'].mean():.1f}"

# ──────────────────────────────────────────────
# TOP METRICS ROW
# ──────────────────────────────────────────────
st.markdown('<p class="section-title">📊 Live Dashboard Metrics</p>', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
c1.markdown(glass_metric("🚗", total_rides, "Total Rides (Dataset)", "blue"),   unsafe_allow_html=True)
c2.markdown(glass_metric("⏰", f"{peak_hour}:00", "Peak Hour", "orange"),        unsafe_allow_html=True)
c3.markdown(glass_metric("📍", busiest_zone, "Busiest Zone", "green"),           unsafe_allow_html=True)
c4.markdown(glass_metric("📈", avg_demand, "Avg Demand / Slot", "purple"),       unsafe_allow_html=True)

st.markdown("<div style='margin-top:8px;'></div>", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# PREDICTION RESULT
# ──────────────────────────────────────────────
if predict_clicked:
    zone_enc    = safe_encode(le_zone, zone)
    weather_enc = safe_encode(le_weather, weather)

    input_dict = {
        "hour": hour,
        "day_of_week": day_of_week,
        "month": month_num,
        "week": week_num,
        "is_weekend": int(is_weekend),
        "is_festival": int(is_festival),
        "temperature": temp,
        "zone_encoded": zone_enc,
        "weather_encoded": weather_enc,
    }

    # Build input frame aligned with training features
    input_df = pd.DataFrame([{f: input_dict.get(f, 0) for f in features}])

    predicted = float(model.predict(input_df)[0])
    predicted = max(0, predicted)
    level, color, emoji, reco = demand_level(predicted)

    badge_style = (
        f"background:{color}22;color:{color};"
        f"border:1px solid {color}55;"
    )
    num_style = f"color:{color};filter:drop-shadow(0 0 18px {color}66);"

    st.markdown(f"""
    <div class="pred-card">
        <div style="display:flex;flex-direction:column;gap:8px;
                    align-items:flex-start;margin-bottom:8px;">
            <span class="pred-badge" style="{badge_style}">
                {emoji} {level} DEMAND
            </span>
            <span style="color:#bcc9ce;font-size:14px;
                         font-family:'JetBrains Mono',monospace;
                         letter-spacing:0.06em;">
                {zone.upper()} · {hour:02d}:00 · {day_name} · {weather}
            </span>
        </div>
        <div style="display:flex;align-items:flex-end;gap:16px;flex-wrap:wrap;">
            <span class="pred-number" style="{num_style}">
                {predicted:.0f}
            </span>
            <span style="color:#869398;font-family:'JetBrains Mono',monospace;
                         font-size:13px;letter-spacing:0.08em;margin-bottom:12px;">
                PREDICTED RIDES
            </span>
        </div>
        <div class="pred-recommendation" style="border-left-color:{color};">
            💡 <strong>Recommendation:</strong> {reco}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ──────────────────────────────────────────────
# DASHBOARD CHARTS — ROW 1
# ──────────────────────────────────────────────
st.markdown('<p class="section-title">📉 Demand Analytics</p>', unsafe_allow_html=True)
col_l, col_r = st.columns(2)

# Chart 1 – Hourly Demand (line + fill)
with col_l:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    hourly = df.groupby("hour")["demand"].mean().reset_index()
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=hourly["hour"], y=hourly["demand"],
        mode="lines",
        line=dict(color="#4cd6fb", width=3),
        fill="tozeroy",
        fillcolor="rgba(76,214,251,0.12)",
        name="Avg Demand",
    ))
    fig1.update_layout(
        title="⏰ Hourly Demand Pattern",
        xaxis_title="Hour", yaxis_title="Avg Rides",
        **CHART_LAYOUT,
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Chart 2 – Zone Demand (bar)
with col_r:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    zone_data = (
        df.groupby("zone")["demand"].mean()
          .sort_values(ascending=False)
          .reset_index()
    )
    n = len(zone_data)
    bar_colors = [
        f"rgba(255,107,53,{0.5 + 0.5 * (1 - i / n)})" for i in range(n)
    ]
    fig2 = go.Figure(go.Bar(
        x=zone_data["zone"], y=zone_data["demand"],
        marker_color=bar_colors,
        text=zone_data["demand"].round(1),
        textposition="outside",
        textfont=dict(color="#dee3e6", size=10),
    ))
    fig2.update_layout(
        title="📍 Average Demand by Zone",
        xaxis_title="Zone", yaxis_title="Avg Rides",
        **CHART_LAYOUT,
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────
# DASHBOARD CHARTS — ROW 2
# ──────────────────────────────────────────────
col_l2, col_r2 = st.columns(2)

# Chart 3 – Heatmap Hour vs Day
with col_l2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    pivot = df.groupby(["day_of_week","hour"])["demand"].mean().reset_index()
    pivot_matrix = pivot.pivot(index="day_of_week", columns="hour", values="demand")
    pivot_matrix.index = [DAYS[i] for i in pivot_matrix.index]

    fig3 = go.Figure(go.Heatmap(
        z=pivot_matrix.values,
        x=[f"{h}:00" for h in pivot_matrix.columns],
        y=pivot_matrix.index,
        colorscale=[
            [0.0, "#0e1416"],
            [0.4, "#004e5f"],
            [0.7, "#4cd6fb"],
            [1.0, "#ff6b35"],
        ],
        showscale=True,
        colorbar=dict(
            tickfont=dict(color="#dee3e6"),
            outlinecolor="rgba(0,0,0,0)",
        ),
    ))
    fig3.update_layout(
        title="🗓️ Demand Heatmap (Hour × Day)",
        **{**CHART_LAYOUT, "margin": dict(l=10, r=40, t=40, b=10)},
    )
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Chart 4 – Weather breakdown
with col_r2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    w_data = df.groupby("weather")["demand"].mean().reset_index()
    fig4 = go.Figure(go.Pie(
        labels=w_data["weather"],
        values=w_data["demand"].round(2),
        hole=0.55,
        marker=dict(
            colors=["#4cd6fb", "#ff6b35", "#869398"],
            line=dict(color="#0e1416", width=2),
        ),
        textfont=dict(color="#dee3e6"),
    ))
    fig4.update_layout(
        title="🌤️ Demand by Weather Type",
        **CHART_LAYOUT,
    )
    st.plotly_chart(fig4, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────
# ZONE COMPARISON
# ──────────────────────────────────────────────
st.markdown('<p class="section-title">🗺️ Zone Hourly Pattern</p>', unsafe_allow_html=True)
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

sel_zones = st.multiselect(
    "Select zones to compare",
    options=ZONES,
    default=["Thamel", "Baneshwor", "Lalitpur"],
)

ZONE_COLORS = [
    "#4cd6fb","#ff6b35","#2ecc71","#a855f7",
    "#f1c40f","#e74c3c","#ffb77d","#00b4d8",
]

if sel_zones:
    fig5 = go.Figure()
    peak_h = int(hour_avg.idxmax())

    for idx, z in enumerate(sel_zones):
        z_df = df[df["zone"] == z].groupby("hour")["demand"].mean().reset_index()
        col = ZONE_COLORS[idx % len(ZONE_COLORS)]
        fig5.add_trace(go.Scatter(
            x=z_df["hour"], y=z_df["demand"],
            mode="lines+markers", name=z,
            line=dict(color=col, width=2),
            marker=dict(size=5),
        ))

    # Peak hour shading
    fig5.add_vrect(
        x0=peak_h - 0.5, x1=peak_h + 0.5,
        fillcolor="rgba(231,76,60,0.15)",
        line_width=0,
        annotation_text="Peak",
        annotation=dict(font_color="#e74c3c", font_size=11),
        annotation_position="top left",
    )
    fig5.update_layout(
        title="📈 Hourly Demand Comparison by Zone",
        xaxis_title="Hour", yaxis_title="Avg Demand",
        **CHART_LAYOUT,
    )
    st.plotly_chart(fig5, use_container_width=True)
else:
    st.info("Select at least one zone above.")

st.markdown('</div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────
# EXTRA METRICS — Weekend vs Weekday
# ──────────────────────────────────────────────
st.markdown('<p class="section-title">📋 Additional Insights</p>', unsafe_allow_html=True)
ia, ib, ic, id_ = st.columns(4)
ia.markdown(glass_metric("☀️", f"{weekday_avg:.1f}", "Avg Weekday Demand", "blue"),   unsafe_allow_html=True)
ib.markdown(glass_metric("🏖️", f"{weekend_avg:.1f}", "Avg Weekend Demand", "orange"), unsafe_allow_html=True)
ic.markdown(glass_metric("🌤️", best_weather, "Best Weather for Rides", "green"),     unsafe_allow_html=True)
id_.markdown(glass_metric("📊", wknd_label, "Weekend vs Weekday %", "purple"),        unsafe_allow_html=True)

# ──────────────────────────────────────────────
# FOOTER
# ──────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;margin-top:48px;padding:24px 0;
            border-top:1px solid rgba(61,73,77,0.35);">
    <p style="color:#869398;font-size:14px;
              font-family:'JetBrains Mono',monospace;
              letter-spacing:0.05em;">
        🛵 Kathmandu Ride Demand Forecaster &nbsp;|&nbsp;
        Data Science Portfolio Project &nbsp;|&nbsp;
        Sudeep &nbsp;|&nbsp; Biratnagar, Nepal &nbsp;|&nbsp; 2025
    </p>
</div>
""", unsafe_allow_html=True)
