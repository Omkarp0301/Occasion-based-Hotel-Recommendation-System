import streamlit as st

from generate_recommendation import recommender

# Set the title of your app
st.title('Hotel Recommendation System')

st.image('https://thehoughtonhotel.com/wp-content/uploads/2023/02/Houghton-Hotel-3-5-scaled.jpg', caption='Your Image',
         use_column_width=True)

# Create 3 columns
col1, col2, col3 = st.columns(3)

# Column 1: Select the country
with col1:
    Location = st.selectbox('Select the country', ['NL', 'UK', 'FR', 'ES', 'IT', 'AT'])

# Column 2: Input the number of guests
with col2:
    number = st.number_input('Enter the number of guests', min_value=0, max_value=4, value=1)

# Column 3: Input the budget
with col3:
    budget = st.number_input('Budget?($/day)', min_value=100, max_value=50000, value=100)

# Create a text input for defining the room type
description = st.text_input('Enter the type of room you want')

# Generate recommendations based on user inputs
if st.button("Get Recommendations"):
    recommended_hotels = recommender(Location, description)
    st.header('Recommended Hotels')

    if not recommended_hotels.empty:  # Check if the DataFrame is not empty

        # Create a column for each hotel recommendation
        col1, col2, col3 = st.columns(3)

        # Display the hotel name, average score, and address in the first three columns
        with col1:
            st.subheader("Name")
        with col2:
            st.subheader("Average Score")
        with col3:
            st.subheader("Hotel_Address")

        for index, row in recommended_hotels[["Hotel_Name", "Average_Score", "Hotel_Address"]].head(
                50).iterrows():
            # Create a column for each hotel recommendation
            col1, col2, col3 = st.columns(3)

            # Display the hotel name, average score, and address in the first three columns
            with col1:
                st.write(row['Hotel_Name'])
            with col2:
                st.write(row['Average_Score'])
            with col3:
                st.write(row['Hotel_Address'])

            # Add a horizontal line (partition) between rows
            st.markdown("---")


    else:
        st.write("No recommendations found.")
