import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. Page Configuration & Styling
# Is se page full screen mein khulega
st.set_page_config(page_title="Rafay Decor | Premium Management", layout="wide")

# Floral Background CSS
# Humne background pe floral pic rakhi hai, but content clear dikhane ke liye glass effect diya hai.
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1526047932273-341f2a7631f9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80");
        background-size: cover;
    }
    .main-box {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        color: #333;
        margin-top: 20px;
    }
    .main-box h1 {
        color: #D4AF37;
        text-align: center;
        margin-bottom: 20px;
    }
    .main-box h2 {
        color: #444;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    .price-card {
        background-color: #fdfaf0;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #D4AF37;
        margin-bottom: 10px;
    }
    .price-card h4 {
        margin: 0;
        color: #333;
    }
    .price-card p {
        color: #D4AF37;
        font-weight: bold;
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar Navigation
st.sidebar.markdown("<h1 style='text-align: center; color: #D4AF37;'>Rafay Decor</h1>", unsafe_allow_html=True)
# Yahan humne navigation tabs define kiye hain.
page = st.sidebar.radio("Main Menu", ["Welcome Page", "Our Services & Pricing", "Staff & Responsibilities", "Online Booking", "Payment Portal", "Admin Dashboard"])

# Data file jahan bookings save hongi
FILE_NAME = "rafay_bookings.csv"

# --- PAGE 1: WELCOME PAGE ---
if page == "Welcome Page":
    st.markdown("""
    <div class='main-box'>
        <h1>Welcome to Rafay Decor</h1>
        <p style='font-size: 18px; text-align: center;'><i>Your premier partner in creating unforgettable memories.</i></p>
        <p>At Rafay Decor, we specialize in transforming your dreams into reality. From grand weddings to intimate birthdays, our floral arrangements, thematic setups, and bespoke decors are designed to leave a lasting impression.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 2-column layout hall ki pics dikhane ke liye
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='main-box' style='padding:15px;'><h3>Grand Wedding Hall</h3>", unsafe_allow_html=True)
        # Yeh photo hall ki setup hai
        st.image("https://images.unsplash.com/photo-1519167758481-83f550bb49b3?w=600", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='main-box' style='padding:15px;'><h3>Premium Table Decor</h3>", unsafe_allow_html=True)
        # Yeh photo catering/table decoration ki hai
        st.image("https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=600", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 2: SERVICES & PRICING (7 Types) ---
elif page == "Our Services & Pricing":
    st.title("💎 Our Decoration Packages")
    st.write("Browse through our most popular service categories:")
    
    # Humne yahan ek dictionary define ki hai pricing dikhane ke liye.
    services = {
        "🌸 Fresh Flower Decor": "Starting from RS. 40,000/-",
        "💡 Luxury Lighting Setup": "Starting from RS. 25,000/-",
        "🖥️ Digital LED Screening": "Starting from RS. 35,000/-",
        "🎈 Birthday Decoration": "Starting from RS. 15,000/-",
        "🕌 Nikah Theme Setup": "Starting from RS. 30,000/-",
        "🍽️ Catering & Table Decor": "Starting from RS. 20,000/-",
        "🎥 Photography Backdrop": "Starting from RS. 10,000/-"
    }
    # Loop ke zariye sab ko render karte hain.
    for service, price in services.items():
        st.markdown(f"""
        <div class='price-card'>
            <h4>{service}</h4>
            <p>{price}</p>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE 3: STAFF & RESPONSIBILITIES ---
elif page == "Staff & Responsibilities":
    st.title("👥 Our Team")
    st.write("We take pride in our dedicated team of professionals:")
    
    # Humne yahan sample staff data define kiya hai.
    staff_data = {
        "Staff Name": ["Irfan Ahmed", "Kamran Khan", "Sajid Ali", "Zubair", "Bilal"],
        "Role": ["Head Decorator", "Electrician", "Floral Artist", "Supervisor", "Transport"],
        "Responsibility": ["Stage Design", "Lighting & LED", "Flower Setup", "Labour Management", "Delivery"]
    }
    # pandas dataframe bana kar table mein show karenge.
    df_staff = pd.DataFrame(staff_data)
    st.table(df_staff)

# --- PAGE 4: BOOKING FORM ---
elif page == "Online Booking":
    st.title("📝 Online Event Reservation")
    st.write("Please fill in the form below to submit your booking request. Our team will contact you shortly.")
    
    # Streamlit form jo form submit karne pe hi process hota hai.
    with st.form("booking_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Customer Full Name *")
            phone = st.text_input("Phone Number *")
            date = st.date_input("Event Date")
        with col2:
            guests = st.number_input("Guest Count", min_value=10)
            # Service list wahi hai jo Pricing tab mein thi.
            service = st.selectbox("Select Decoration Package", ["Fresh Flower Decor", "Luxury Lighting", "Digital Screening", "Birthday", "Nikah Theme", "Catering & Table", "Photography Backdrop"])
            notes = st.text_area("Special Requirements (Optional)")
            
        submit = st.form_submit_button("Submit Request")
        
        # Form submit hone par save karega.
        if submit and name and phone:
            # unique Booking ID banata hai.
            booking_id = f"RD-{datetime.now().strftime('%d%m%y%H%M')}"
            new_data = pd.DataFrame({
                "ID": [booking_id],
                "Name": [name],
                "Phone": [phone],
                "Date": [str(date)],
                "Guests": [guests],
                "Service": [service],
                "Status": ["Pending"]
            })
            
            # Agar file nahi hai tou header ke sath banaega, warna append karega.
            if not os.path.isfile(FILE_NAME):
                new_data.to_csv(FILE_NAME, index=False)
            else:
                new_data.to_csv(FILE_NAME, mode='a', index=False, header=False)
                
            st.success(f"Mubarak Ho {name}! Aapki booking request submit ho gayi hai. Aapka ID {booking_id} hai. Payment complete kar ke apni booking confirm karein.")
        elif submit:
            st.error("Please enter a valid Name and Contact Number")

# --- PAGE 5: PAYMENT PORTAL ---
elif page == "Payment Portal":
    st.title("💳 Payment Options")
    st.write("Please use your Booking ID (e.g., RD-XXXX) as the reference for all payments. All bookings require a 50% advance deposit.")
    
    st.markdown("""
    <div class='price-card'>
        <h4>Bank Transfer</h4>
        <p>Alfalah Bank | Account: 1234-5678-90 | Title: Rafay Decor</p>
    </div>
    <div class='price-card'>
        <h4>JazzCash / EasyPaisa</h4>
        <p>Account Number: 0300-XXXXXXX | Title: Rafay Decor</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("After making the payment, please share the receipt with us on WhatsApp for confirmation.")

# --- PAGE 6: ADMIN DASHBOARD ---
elif page == "Admin Dashboard":
    st.title("📊 Management Panel")
    st.write("View and manage all event bookings:")
    
    # Bookings file padhte hain.
    if os.path.isfile(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        # dataframe show karte hain full width mein.
        st.dataframe(df, use_container_width=True)
        
        # Download button taake Excel mein khul sake.
        st.download_button(
            label="Download Bookings as CSV",
            data=df.to_csv(index=False),
            file_name="rafay_decor_bookings.csv",
            mime="text/csv"
        )
    else:
        st.info("No bookings recorded yet..")
