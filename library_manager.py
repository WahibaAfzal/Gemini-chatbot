import streamlit as st
import pandas as pd
import os

# File to store library data
LIBRARY_FILE = "library.csv"

# Default books
FAMOUS_BOOKS = [
    {"Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Year": 1925, "Genre": "Fiction", "Read": False, "PDF": "https://www.planetebook.com/free-ebooks/the-great-gatsby.pdf"},
    {"Title": "1984", "Author": "George Orwell", "Year": 1949, "Genre": "Dystopian", "Read": False, "PDF": "https://www.planetebook.com/free-ebooks/1984.pdf"},
    {"Title": "Pride and Prejudice", "Author": "Jane Austen", "Year": 1813, "Genre": "Romance", "Read": False, "PDF": "https://www.planetebook.com/free-ebooks/pride-and-prejudice.pdf"}
]

# Load or create library file
if os.path.exists(LIBRARY_FILE):
    df = pd.read_csv(LIBRARY_FILE)
else:
    df = pd.DataFrame(FAMOUS_BOOKS)
    df.to_csv(LIBRARY_FILE, index=False)

st.title("📚 Simple Library Manager")

menu = st.sidebar.radio("Menu", ["Add Book", "Search Book", "View Library", "Statistics"])

if menu == "Add Book":
    st.header("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, step=1)
    genre = st.text_input("Genre")
    read = st.checkbox("Have you read this book?")
    pdf_link = st.text_input("PDF Link (Optional)")
    
    if st.button("Add Book"):
        new_book = pd.DataFrame([[title, author, year, genre, read, pdf_link]], columns=df.columns)
        df = pd.concat([df, new_book], ignore_index=True)
        df.to_csv(LIBRARY_FILE, index=False)
        st.success("Book added successfully!")
        st.rerun()




elif menu == "Search Book":
    st.header("Search a Book")

  
    book_titles = df["Title"].dropna().unique().tolist()
    author_names = df["Author"].dropna().unique().tolist()
    
    
    search_suggestions = sorted(set(book_titles + author_names))

   
    search_query = st.selectbox("Search by title or author", [""] + search_suggestions)

    if search_query:
      
        filtered_df = df[
            df["Title"].str.lower().str.contains(search_query.lower(), na=False) |
            df["Author"].str.lower().str.contains(search_query.lower(), na=False)
        ]

        if not filtered_df.empty:
            st.table(filtered_df)
        else:
            st.warning("No matching books found in your library.")


elif menu == "View Library":
    st.header("Your Library")
    for index, row in df.iterrows():
        st.write(f"📖 {row['Title']} by {row['Author']} ({row['Year']}) - {row['Genre']} - {'✅ Read' if row['Read'] else '❌ Unread'}")
        col1, col2 = st.columns(2)
        with col1:
            if row["PDF_Link"]:
                st.markdown(f"[📖 Read Now]({row['PDF_Link']})")
        with col2:
            if st.button(f"❌ Remove {row['Title']}", key=index):
                df = df.drop(index).reset_index(drop=True)
                df.to_csv(LIBRARY_FILE, index=False)
                st.rerun()

elif menu == "Statistics":
    st.header("📊 Library Statistics")
    total_books = len(df)
    read_books = df["Read"].sum()
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    
    st.metric("📚 Total Books", total_books)
    st.metric("✅ Books Read", read_books)
    st.progress(percentage_read / 100)
    st.write(f"📖 Read Percentage: {percentage_read:.2f}%")
