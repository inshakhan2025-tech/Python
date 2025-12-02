import streamlit as st

# Set the title and header for the Streamlit app
st.title("Amazon Demo Website")
st.header("Welcome to the Demo of Amazon Website!")

# Add a search bar like on Amazon's homepage
search_query = st.text_input("Search for products", "Laptop")

# Display search results
st.subheader(f"Search Results for: {search_query}")

# Example product data (in reality, you would fetch this from an API)
products = [
    {"name": "Laptop A", "price": "$599.99", "image": "https://via.placeholder.com/150", "link": "#"},
    {"name": "Laptop B", "price": "$899.99", "image": "https://via.placeholder.com/150", "link": "#"},
    {"name": "Laptop C", "price": "$499.99", "image": "https://via.placeholder.com/150", "link": "#"},
    {"name": "Laptop D", "price": "$1099.99", "image": "https://via.placeholder.com/150", "link": "#"},
]

# Display the products in a grid
for product in products:
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.image(product['image'], width=100)
    
    with col2:
        st.markdown(f"### {product['name']}")
        st.markdown(f"**Price**: {product['price']}")
        st.markdown(f"[View Product]({product['link']})")

# Footer
st.markdown("___")
st.text("Amazon Demo Website - Powered by Streamlit")
