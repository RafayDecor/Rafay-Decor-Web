import streamlit as st
from streamlit_option_menu import option_menu
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Rafay Decor | Event Excellence", page_icon="🌸", layout="wide")

# --- CUSTOM CSS FOR PINK, WHITE & FLORAL THEME ---
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/floral-paper.png");
        background-attachment: fixed;
    }
    h1, h2, h3 {
        color: #D81B60;
        font-family: 'Playfair Display', serif;
    }
    .stButton>button {
        background-color: #F8BBD0;
        color: black;
        border-radius: 20px;
        border: 1px solid #D81B60;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #D81B60;
        color: white;
    }
    .payment-card {
        padding: 20px;
        border-radius: 15px;
        background-color: #FFF5F8;
        border-left: 5px solid #D81B60;
        margin-bottom: 20px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    # Nayi Logo Image ka link yahan hai
    st.image("https://cdn-icons-png.flaticon.com/512/2833/2833315.png", width=120) 
    
    selected = option_menu(
        menu_title="Rafay Decor Menu",
        options=["Home", "Services & Gallery", "Packages", "Booking", "Payment Methods", "Our Team", "Policies", "Admin"],
        icons=["house", "images", "gift", "calendar-check", "credit-card", "people", "file-text", "person-badge"],
        menu_icon="cast", 
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#FFF5F8"},
            "icon": {"color": "#D81B60", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#F8BBD0"},
            "nav-link-selected": {"background-color": "#D81B60"},
        }
    )

# --- 1. HOME / WELCOME PAGE ---
if selected == "Home":
    st.title("🌸 Welcome to Rafay Decor")
    st.subheader("Transforming Your Moments Into Magical Memories")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        ### About Us
        Rafay Decor is a premier event management brand based in Karachi. Our goal is to make your events unique, elegant, and unforgettable. 
        Whether it is a Nikkah, Mehndi, or a Birthday celebration, we pay attention to every fine detail.
        
        **Our Vision:** To provide premium decoration at competitive and affordable prices.
        **Our Mission:** Delivering excellence through every flower and light we place.
        """)
    with col2:
        st.image("https://images.unsplash.com/photo-1519167758481-83f550bb49b3?auto=format&fit=crop&q=80&w=500", caption="Luxury Event Setup")

    st.divider()
    st.markdown("### 💡 AI Budget Estimator")
    guests = st.slider("Number of Guests", 50, 1000, 200)
    service_type = st.selectbox("Select Event Type", ["Wedding", "Birthday", "Corporate", "Mehndi"])
    if st.button("Calculate Estimated Budget"):
        price = guests * 500 if service_type == "Wedding" else guests * 300
        st.success(f"Estimated Budget for {service_type}: Rs. {price:,}")

# --- 2. SERVICES & GALLERY ---
elif selected == "Services & Gallery":
    st.title("🎨 Our Decorations & Services")
    tabs = st.tabs(["Weddings", "Mehndi/Nikkah", "Birthdays", "Others"])
    
    with tabs[0]:
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://images.unsplash.com/photo-1511795409834-ef04bbd61622?q=80&w=500", caption="Barat Stage")
            st.write("**Barat & Valima Setup:** Grand stages featuring premium floral arrangements and lighting.")
        with col2:
            st.image("https://images.unsplash.com/photo-1522673607200-1648832cee98?q=80&w=500", caption="Entrance Lighting")
            st.write("**Lighting:** Enchanting fairy lights, elegant chandeliers, and modern neon effects.")

    with tabs[1]:
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://images.unsplash.com/photo-1594135503300-61bc820f4f91?q=80&w=500", caption="Mehndi Stage")
            st.write("**Mehndi Decor:** Traditional vibrant yellow themes combined with floral aesthetics.")
        with col2:
            st.image("https://images.unsplash.com/photo-1606132958425-429971032145?q=80&w=500", caption="Nikkah Setup")
            st.write("**Nikkah Decor:** Sophisticated white and pastel themes for a serene atmosphere.")

    with tabs[2]:
        st.image("https://images.unsplash.com/photo-1530103043960-ef38714abb15?q=80&w=800", caption="Birthday Party")
        st.write("**Birthdays:** Creative balloon decor, customized theme backdrops, and dedicated kids' zones.")

# --- 3. PACKAGES ---
elif selected == "Packages":
    st.title("💎 Event Packages")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("### Basic\n**Rs. 50,000**\n- Standard Stage Decor\n- Basic Ambient Lighting\n- Professional Sound System")
    with c2:
        st.success("### Premium\n**Rs. 150,000**\n- Luxury Stage Design\n- Floral Entrance Walkway\n- 360 Photo Booth Experience")
    with c3:
        st.warning("### Royal\n**Rs. 300,000+**\n- Fresh Imported Flower Decor\n- Full Event Planning & Management\n- Professional Photography & Videography")

# --- 4. BOOKING PAGE ---
elif selected == "Booking":
    st.title("📅 Online Booking & Custom Inquiries")
    with st.form("booking_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("WhatsApp Number")
        event_date = st.date_input("Event Date", min_value=datetime.date.today())
        event_type = st.selectbox("Select Service Type", ["Barat", "Valima", "Mehndi", "Nikkah", "Birthday", "Corporate"])
        details = st.text_area("Specific Requirements / Custom Details")
        
        submit = st.form_submit_button("Submit Booking Request")
        if submit:
            st.balloons()
            st.success("Your request has been submitted successfully! Please proceed to 'Payment Methods' to pay the 50% advance to secure your date.")

# --- 5. PAYMENT METHODS ---
elif selected == "Payment Methods":
    st.title("💳 Secure Payment Options")
    st.markdown("A **50% advance payment** is mandatory to confirm and lock your booking date.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""<div class='payment-card'>
            <h3>📱 Mobile Wallets</h3>
            <p><b>JazzCash:</b> 03XX-XXXXXXX<br>Account Title: Rafay Decor</p>
            <hr>
            <p><b>EasyPaisa:</b> 03XX-XXXXXXX<br>Account Title: Shazia Irshad</p>
        </div>""", unsafe_allow_html=True)
        
    with col2:
        st.markdown("""<div class='payment-card'>
            <h3>🏦 Bank Transfer</h3>
            <p><b>Bank Alfalah:</b> 0123-4567-8910<br>Branch: North Karachi</p>
            <hr>
            <p><b>Meezan Bank:</b> 9876-5432-1098<br>IBAN: PK00 MEZN ...</p>
        </div>""", unsafe_allow_html=True)
    
    st.info("💡 **Note:** Please share a screenshot of the payment confirmation on our WhatsApp (+92 3XX-XXXXXXX) for verification.")

# --- 6. OUR TEAM ---
elif selected == "Our Team":
    st.title("👥 Our Professional Staff")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/4084/4084329.png", width=150)
        st.write("**Event Manager:** Handles overall coordination and execution.")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3462/3462198.png", width=150)
        st.write("**Receptionist:** Manages guest welcoming and general inquiries.")
    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/3532/3532822.png", width=150)
        st.write("**Lead Decorator:** Specialist in floral arrangements and stage setups.")

# --- 7. POLICIES ---
elif selected == "Policies":
    st.title("📜 Terms & Conditions")
    st.write("""
    1. **Booking:** A 50% non-refundable advance payment is required to reserve the date.
    2. **Cancellation:** No refunds will be provided if the booking is cancelled within 7 days of the event.
    3. **Damages:** Any damage caused to the decoration items by guests will be billed to the client.
    4. **Timings:** Standard event duration is capped at 4-6 hours. Additional charges apply for extra hours.
    """)
    st.divider()
    feedback = st.text_area("We value your feedback. Share your experience with us:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your valuable feedback!")

# --- 8. ADMIN SIDE ---
elif selected == "Admin":
    st.title("🔐 Admin Dashboard")
    password = st.text_input("Enter Admin Password", type="password")
    if password == "admin123":
        st.write("### Recent Bookings Overview")
        st.table({"Date": ["2026-06-12", "2026-06-15"], "Customer": ["Ahmed Ali", "Sara Khan"], "Status": ["Paid", "Pending"]})
        st.metric(label="Total Monthly Revenue", value="Rs. 450,000", delta="+15% vs Last Month")
    else:
        st.warning("Restricted Access: Please enter the correct administrator password.")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write("📞 Contact: +92 3xx xxxxxxx")
st.sidebar.write("📍 Location: Karachi, Pakistan")