import streamlit as st
import g4f
import yfinance as yf
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression 

st.set_page_config(page_title="AI Stock Predictor shahid_khan", layout="wide")

st.title("🚀 SHAHID'S QUANT-AI PREDICTOR v2.0")
st.subheader("Billionaire Trading Intelligence Hub")
with st.sidebar:
    st.title("🛡️ Shahid's Quant Lab")
    st.info("Billionaire Rule #1: Never lose money.")
    st.write("---")
    st.header("📈 Trading Guide")
    st.write("🔹 **BUY:** Price upar + Confidence > 60%")
    st.write("🔹 **SELL:** Price niche + Confidence > 60%")
    st.write("🔹 **WAIT:** Market confusing hai, sabr karo.")
    st.write("---")
    st.success("Developer: Shahid Khan")
    # --- 🤖 SHAHID'S AI ASSISTANT ---
    st.write("---")
    st.subheader("💬 AI Assistant")
        
        # Streamlit ka clean aur simple button
    mic_button = st.button("🎙️ Ek baar click karke bolo (Speak Hindi or English)")
        
    voice_text = ""
        
    if mic_button:
            st.sidebar.warning("🎧 Main sun raha hoon... 5 second tak bolo!")
            
            fs = 44100  # Sample rate
            seconds = 5  # Kitne second tak record karna hai
            
            try:
                # Direct hardware mic se audio record karna
                myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
                sd.wait()  # 5 second poore hone tak wait karega
                
                # Audio ko temporary WAV file mein save karna
                wavio.write("temp_voice.wav", myrecording, fs, sampwidth=2)
                st.sidebar.info("🤖 Recognizing your language and voice...")
                
                r = sr.Recognizer()
                with sr.AudioFile("temp_voice.wav") as source:
                    audio_data = r.record(source)
                    # 🌟 ASLI JADOO: Pehle English try karega, nahi toh Hindi script lagayega
                    try:
                        voice_text = r.recognize_google(audio_data, language='en-US')
                    except:
                        voice_text = r.recognize_google(audio_data, language='hi-IN')

                st.sidebar.success(f"🎤 Recognized: {voice_text}")
            except sr.UnknownValueError:
                st.sidebar.error("🤖 AI: Bhai, awaaz saaf nahi aayi, ek baar fir se bolo.")
            except Exception as e:
                st.sidebar.error("🤖 AI: Mic connect karne mein dikkat aa rahi hai.")

        # Text input box jo automatic bolne wali bhasha pakad lega
    user_input = st.text_input(
            "Bhai se kuch pucho:", 
            value=voice_text if voice_text else "",
            placeholder="Ask in English or Hindi..."
        )

# --- 🤖 SHAHID'S AI ASSISTANT WORKING LOGIC ---
    # --- 🤖 SHAHID'S AI ASSISTANT CLEAN LOGIC ---
    # --- 🤖 SHAHID'S DYNAMIC TRADING-ONLY AI CHATBOT FIXED ---
    if user_input:
            user_query = user_input.lower().strip()
            
            if "kaise kaam" in user_query or "how it works" in user_query:
                st.sidebar.success("🤖 AI: Bhai, ye app pichle 1 saal ka stock data scan karta hai aur Moving Averages (MA20/MA50) se kal ka price aur trend predict karta hai!")
            elif "accuracy" in user_query or "confidence" in user_query:
                st.sidebar.info("🤖 AI: Confidence Score dikhata hai ki AI market ke trend ko lekar kitna sure hai. Agar score 60% se upar ho toh signal strong hai!")
            else:
               with st.sidebar.spinner("🤖 Shahid billionaire mindset..."):
                try:
                    response = g4f.ChatCompletion.create(
                        model=g4f.models.default,
                        messages=[
                            {
                                "role": "system", 
                                "content": (
                                    "You are Shahid Khan's Smart AI Trading Assistant. "
                                    "CRITICAL RULE 1: Only answer questions related to Finance and Stock Market. "
                                    "CRITICAL RULE 2: Detect the language of the user text instantly. "
                                    "If the text is written in English alphabets (like 'hi can you tell me...'), you MUST reply 100% in pure English. Do not use any Hindi words. "
                                    "If the text is written in Hindi/Devanagari characters, you must reply in Hindi. "
                                    "Keep your answer professional, accurate, and short."
                                )
                            },
                            {"role": "user", "content": user_input}
                        ]
                    )
                    
                    if response:
                        st.sidebar.success(f"🤖 AI: {response}")
                        
                        # --- 🔊 AUTOMATIC DETECTOR FOR LADKI'S VOICE ---
                        try:
                            has_hindi = any('\u0900' <= char <= '\u097F' for char in response)
                            
                            if has_hindi:
                                detected_lang = 'hi'
                            else:
                                detected_lang = 'en'
                            
                            tts = gTTS(text=response, lang=detected_lang, slow=False)
                            tts.save("ai_response.mp3")
                            st.sidebar.audio("ai_response.mp3", format="audio/mp3", autoplay=True)
                        except Exception as voice_err:
                            pass
                    else:
                        st.sidebar.warning("🤖 AI: Server busy, please try again!")
                        
                except Exception as e:
                    st.sidebar.error(f"🤖 AI: Connection Issue. Error: {str(e)[:50]}")

# ---------- AUTO FIX ----------
def fix_stock(name):
    name = name.upper().strip()
    mapping = {
        "TESLA": "TSLA",
        "APPLE": "AAPL",
        "RELIANCE": "RELIANCE.NS",
        "TCS": "TCS.NS",
        "TATASTEEL": "TATASTEEL.NS"
    }
    return mapping.get(name, name)
    # --- Is line se input box wapas aayega ---
name = st.text_input("Enter Stock (TSLA, AAPL, RELIANCE.NS, TCS.NS):")
if name:
    name = fix_stock(name)
    name = name.strip().upper()

if name:
    name = fix_stock(name)
    name = name.strip(). upper()
# Agar name khaali hai toh aage mat badho
if not name:
    st.info("Bhai, pehle 'TCS' ya 'RELIANCE' jaisa koi stock name dalo upar!")
    st.stop()

# Ab ye purana wala code chalne do
stock = yf.Ticker(name)
data = stock.history(period="1y")
 # Isse 'data' poore code ke liye fix ho jayega
st.session_state['market_data'] = data
if data is None or data.empty:
        st.error("❌ Stock not found")
        st.stop()
current_price = float(data['Close'].iloc[-1])        
# ✅ FINAL CALCULATION (YAHI ADD KAR)

volatility = data['Close'].std()

# simple trend + momentum (agar pehle se nahi hai to add karo)
trend_val = data['Close'].iloc[-1] - data['Close'].iloc[-5]
momentum = data['Close'].pct_change().mean()

jump_factor = (trend_val * 1.8) + (momentum * 100) + (volatility * 0.8)

prediction = current_price + jump_factor
difference = prediction - current_price
# --- 1. PEHLE DATA SET KARO ---
close = data['Close']
    
    # --- 2. INDICATORS CALCULATE KARO ---
data["MA20"] = close.rolling(20).mean()
data["MA50"] = close.rolling(50).mean()

    # --- 3. PRICE DATA NIKALO ---
current_price = float(close.iloc[-1])
yesterday_price = float(close.iloc[-2])
    # --- VOLUME TREND (Yellow line for fix ok) ---
avg_vol = data["Volume"].mean()
current_vol = data["Volume"].iloc[-1]
volume_trend = "High" if current_vol > avg_vol else "Normal"
    # --- 4. TREND AUR MOMENTUM ---
trend_status = "📈 UP" if current_price > data["MA20"].iloc[-1] else "📉 DOWN"
trend_val = current_price - data["MA20"].iloc[-1]
momentum = close.iloc[-1] - close.iloc[-5]
    
    # --- 5. SMART PREDICTION & LAMSAM LOGIC ---
raw_pred = current_price + (trend_val * 0.5) + (momentum * 0.3)
    
    # BHAI KA MAGIC: 0.7% ghataya taaki 345 ka 343 dikhe
prediction = raw_pred * 0.993 
difference = prediction - current_price
 # ---------- PRICE ----------   
    # ---------- INDICATORS ----------
data["MA20"] = close.rolling(20).mean()
data["MA50"] = close.rolling(50).mean()
   # --- SAB KUCH IF NAME: KE ANDAR HONA CHAHIYE ---

    # 1. Price Data
close = data['Close']
yesterday_price = float(close.iloc[-2])

    # 2. Indicators (Clean Version)
data['MA20'] = close.rolling(window=20).mean()
data['MA50'] = close.rolling(window=50).mean()
    
delta = close.diff()
gain = delta.clip(lower=0).rolling(window=14).mean()
loss = (-delta.clip(upper=0)).rolling(window=14).mean()
rs = gain / loss
rsi = float(100 - (100 / (1 + rs.iloc[-1])))
    # --- 📊 Real Market Candlestick Chart ---
st.subheader("📊 Price Action Analysis")
        
        # Candlestick chart banana
fig = go.Figure(data=[go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            name='Market Data'
        )])
        # --- 🤖 SHAHID'S ML BRAIN ---
        # 1. Moving Average calculate karo (Nayi intelligence)
data['MA20'] = data['Close'].rolling(window=20).mean()
df_ml = data[['Close', 'MA20']].dropna() # Khali rows hatao
        
        # 2. Data ko ML ke layak banana
y = df_ml['Close'].values.reshape(-1, 1)
X = np.arange(len(y)).reshape(-1, 1)
y = data['Close'].values.reshape(-1, 1)
X = np.arange(len(y)).reshape(-1, 1)

        # AI Model ko training dena
model = LinearRegression()
model.fit(X, y)

        # Kal (Next Day) ka prediction nikalna
next_day = np.array([[len(y)]])
prediction = model.predict(next_day)[0][0]
# AI ka Confidence Level (Accuracy) nikalna
accuracy = model.score(X, y) * 100
st.write(f"🎯 **AI Confidence Score:** {accuracy:.2f}%")
# --- 🚦 SHAHID'S SMART SIGNALS ---
st.markdown("---")
st.subheader("🚦 AI Trading Signal")
        
        # BUY SIGNAL: Prediction upar hai aur confidence 60% se zyada
if prediction > float(data['Close'].iloc[-1]) and accuracy > 60:
            st.success(f"✅ **BUY SIGNAL:** AI ₹{prediction:.2f} ka target dekh raha hai. Confidence solid hai!")
        
        # SELL SIGNAL: Prediction niche hai aur confidence 60% se zyada
elif prediction < float(data['Close'].iloc[-1]) and accuracy > 60:
            st.error(f"🔻 **SELL SIGNAL:** AI ko lagta hai price ₹{prediction:.2f} tak girega. Bach ke raho!")
        
        # WAIT SIGNAL: Jab AI khud sure na ho
else:
            st.info("✋ **WAIT:** AI abhi pakka nahi hai (Low Confidence). Sideways market mein trade mat karo.")
if accuracy > 70:
   st.success("🔥 High Confidence: Trend majboot hai!")
else:
    st.warning("⚠️ Low Confidence: Market unpredictable hai.")   
# MA Lines ko chart par dikhana
fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], name='MA20 (Short)', line=dict(color='orange', width=1.5)))
fig.add_trace(go.Scatter(x=data.index, y=data['MA50'], name='MA50 (Long)', line=dict(color='blue', width=1.5)))

        # Chart ka look professional (Dark Mode) banana
fig.update_layout(
            title=f"{name} Live Analysis",
            yaxis_title="Stock Price",
            xaxis_title="Date",
            template="plotly_dark",
            xaxis_rangeslider_visible=False,
            height=600
        )
        # --- 🚀 SCREEN PAR CHART DIKHANA ---
st.plotly_chart(fig, use_container_width=True)
st.write("---")
st.caption("⚠️ **Disclaimer:** Shahid's AI predictions are based on historical patterns. Stock markets are risky. Always do your own research.")
st.info("💡 **Billionaire Tip:** Jab Confidence Score 80% se upar ho, tabhi trend ko majboot maanein.")

# Screen par chart dikhana
        # Pehle Chart (fig) ko define karo
import plotly.graph_objects as go
fig = go.Figure(data=[go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])])
fig.update_layout(template="plotly_dark", xaxis_rangeslider_visible=False, height=500)
        
        # Ab Chart ko screen par dikhao
# Bina kisi variable jhanjhat ke chart dikhao
st.write(fig)
# --- 💎 ADVANCED BILLIONAIRE DASHBOARD ---
st.markdown("---")
st.header("🚀 Shahid's Intelligence Hub")
        
        # 1. Row of Metrics (Boxes mein data chamkega)
col1, col2, col3 = st.columns(3)
# Defining data for the boxes below
# --- PEHLE SARA CALCULATION KARO (Line 122 ke upar) ---


        # --- AB SCREEN PAR DIKHAO (Jo pehle se likha hai) ---
st.markdown("---")
st.header("🚀 Shahid's Intelligence Hub")
st.subheader(f"Current Market Price: ₹{current_price:,.2f}")
st.info(f"AI Prediction for tomorrow: ₹{prediction:,.2f}")
# --- 💰 SHAHID'S BILLIONAIRE RISK CALCULATOR ---
st.markdown("---")
st.header("💎 Shahid's Billionaire Strategy")
        
        # Checking if data exists to avoid any NameError
if 'prediction' in locals() and 'current_price' in locals():
            col_risk1, col_risk2 = st.columns(2)
            
            with col_risk1:
                investment = st.number_input("Aap kitna invest karna chahte hain?", value=10000)
                # Auto-fill target price from AI prediction
                target_p = st.number_input("Target Price (AI based):", value=float(prediction))

            # Calculation
            potential_profit = ((target_p - current_price) / current_price) * investment
            roi = (potential_profit / investment) * 100

            with col_risk2:
                st.metric("Expected Profit", f"₹{potential_profit:,.2f}", delta=f"{roi:.2f}% ROI")
                
if roi > 5:
 st.success("🚀 Billionaire Move: Profit ke chances solid hain!")
elif roi < 0:
 st.warning("⚠️ Risk Alert: Paisa doobne ka khatra hai!")
st.markdown("---")
st.header("🚀 Shahid's Intelligence Hub")
st.subheader(f"Current Market Price: ₹{current_price:,.2f}")
st.info(f"AI Prediction for tomorrow: ₹{prediction:,.2f}")
# 3. Profit Calculator (Billionaire Mindset #
with st.expander("💰 Calculate Your Potential Profit"):
            invest = st.number_input("If you invest (₹/$):", value=10000)
            profit = (difference / current_price) * invest
st.write(f"### Predicted Return: ₹{profit:,.2f}")
st.caption("Disclaimer: AI predictions are based on patterns, not guarantees.")
    # --- 🎯 TARGET LOGIC (Big Jump ₹543 to ₹789) ---
st.subheader("🎯 AI Next Day Target")
if difference > 0:
 st.success(f"🚀 Kal ka Expected Target: ₹{prediction:.2f}")
else:
 st.warning(f"📉 Kal ka Expected Support: ₹{prediction:.2f}")
# --- 🎯 TARGET LOGIC (Big Jump ₹543 to ₹789) ---
volatility = data['Close'].std() 
jump_factor = (trend_val * 1.8) + (momentum * 1.5) + (volatility * 0.8)
        
prediction = current_price + jump_factor
difference = prediction - current_price

st.subheader("🎯 AI Next Day Target")
if difference > 0:
     st.success(f"🚀 Kal ka Expected Target: ₹{prediction:.2f}")
else:
     st.warning(f"📉 Kal ka Expected Support: ₹{prediction:.2f}")
volume_trend = "High" if data["Volume"].iloc[-1] > data["Volume"].mean() else "Normal"

    # 3. SMART PREDICTION & LAMSAM LOGIC
    #trend = current_price - data["MA20"].iloc[-1]
momentum = close.iloc[-1] - close.iloc[-5]
    
    # Original Prediction
raw_pred = current_price + (trend_val*0.5) + (momentum * 0.3)
    
    # --- BHAI KA 343 WALA LOGIC (0.7% margin) ---
lamsam_price = raw_pred * 0.993 
difference = lamsam_price - current_price

    # 4. UI DISPLAY
st.subheader("📊 Market Data")
st.write(f"💰 Current Price: {current_price:.2f}")
st.write(f"📅 Yesterday Price: {yesterday_price:.2f}")

st.subheader("🤖 AI Prediction PRO MAX")
    # Yahan hum lamsam_price dikhayenge jo 343 ke aas-paas hoga
st.write(f"🚀 Next Day Price (Approx): {lamsam_price:.2f}")
st.write(f"📉 Difference: {difference:.2f}")

    # RSI & Signals
st.subheader("📈 Indicators")
st.write(f"📊 RSI: {rsi:.2f}")
if rsi > 70:
        st.error("🚩 Overbought: Sambhal kar, gir sakta hai!")
elif rsi < 30:
     st.success("✅ Oversold: Kharidne ka sahi mauka!")
else:
    st.info("⚖️ Neutral Market")
# --- SHAHID'S BRANDING ---
    st.write("---")
    st.write("### 🚀 Created with ❤️ by Shahid Khan")
    st.caption("Billionaire Mindset Edition | AI Stock Predictor v1.0")
