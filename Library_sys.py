import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# file for load data
library_file = "library.csv"
def load_data():
    try:
        df = pd.read_csv(library_file)
        return df
    except FileNotFoundError:
        return pd.DataFrame()

# file for save data
def save_data(df):
    df.to_csv(library_file, index=False)

# streamlit home app
st.title("📚 Personal Library Management System")

# load data
df = load_data()


#menu
st.sidebar.title("📌Menu")
option = st.sidebar.radio("Select an option", ["Home","Add Book", "View Books", "Search Books","Remove Book","Statistics","Update Book"])
#home
if option == "Home":
    st.write("""Welcome to the Personal Library Management System. This app allows you to manage your library of books.
    You can add, view, search, and update your books in the library.
    You can also see statistics about your library.
    You can also remove a book from your library.
    """)
    st.image('https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')
    st.snow()
    st.markdown("---")
    st.markdown('© 2025 Digital Library - created by [Osama](https://github.com/Osamahassan2005)')
# add book
if option == "Add Book":
    st.subheader("Add Book")
    with st.form("add_book"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.number_input("Year", min_value=0, step=1)
        genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Science Fiction",
         "Mystery", "Romance", "Fantasy", "Horror", "Thriller", "Biography", "History", 
         "Travel", "Self-Help", "Business", "Technology", "Art", "Cooking", "Health", "Science", "Math", "Language", "Other"])
        read = st.checkbox("Read")
        submit_button = st.form_submit_button("Add Book")

        if submit_button:
            new_book = {
                "Title": title,
                "Author": author,
                "Year": year,
                "Genre": genre,
                "Read": read
            }
            df = pd.concat([df, pd.DataFrame([new_book])], ignore_index=True)
            save_data(df)
            st.success("Book added successfully!")
        else:
            st.error("Please fill in all fields")

# view books
if option == "View Books":
    st.subheader("View Books")
    if df.empty:
        st.info("No books in the library yet")
    else:
        st.table(df)

# search books
if option == "Search Books":
    st.subheader("Search Books")
    try:
        
        search_by = st.selectbox("Search by", ["Title", "Author", "Year", "Genre"])
        search_query = st.text_input("Search query")
        
        if st.button("Search"):
            if search_query:
                try:
                    if search_by == "Title":
                        results = df[df["Title"].fillna('').str.contains(search_query, case=False)]
                    elif search_by == "Author":
                        results = df[df["Author"].fillna('').str.contains(search_query, case=False)]
                    elif search_by == "Year":
                        try:
                            year_query = int(search_query)
                            results = df[df["Year"].fillna(-1) == year_query]
                        except ValueError:
                            st.error("Please enter a valid year")
                            results = pd.DataFrame()
                    elif search_by == "Genre":
                        results = df[df["Genre"].fillna('').str.contains(search_query, case=False)]
                    
                    if not results.empty:
                        st.table(results)
                    else:
                        st.error(f"No results found for '{search_query}' in {search_by}")
                        
                except Exception as e:
                    st.error(f"Error during search: {str(e)}")
            else:
                st.error("Please enter a search query")
                
    except FileNotFoundError:
        st.error("Library database not found. Please add some books first.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# delete book
if option == "Remove Book":
    st.subheader("Remove Book")
    delete_book = st.selectbox("Select a book to remove", df["Title"])
    if st.button("Remove"):
        df = df[df["Title"] != delete_book]
        save_data(df)
        st.success("Book removed successfully!")
    else:
        st.error("Please select a book to remove")

# statistics
if option == "Statistics":
    st.subheader("Statistics")
    st.table(df)
    plt.figure(figsize=(10, 5))
    plt.bar(df["Read"].value_counts().index, df["Read"].value_counts().values)
    plt.xlabel("Read")
    plt.ylabel("Count")
    plt.title("Read Statistics")
    st.pyplot(plt)

# update book
if option == "Update Book":
    st.subheader("Update Book")
    try:
        df = pd.read_csv(library_file)
        book_titles = df['Title'].tolist()
        
        book_to_update = st.selectbox("Select book to update:", book_titles)
        
        if book_to_update:
            book_data = df[df['Title'] == book_to_update].iloc[0]
            
            new_title = st.text_input("Title", value=book_data['Title'])
            new_author = st.text_input("Author", value=book_data['Author'])
            new_year = st.text_input("Year", value=book_data['Year'])
            new_genre = st.selectbox("Genre", 
                                   ['Fiction', 'Non-Fiction', 'Biography', 'Science Fiction', 
                                    'Mystery', 'Romance', 'Horror', 'Thriller', 'Fantasy', 
                                    'Drama', 'Comedy', 'Action', 'Adventure', 'Animation',
                                    'Children', 'Young Adult'],
                                   index=book_data['Genre'])
            new_read = st.checkbox("Read", value=book_data['Read'])
            
            if st.button("Update Book"):
                df.loc[df['Title'] == book_to_update, 'Title'] = new_title
                df.loc[df['Title'] == book_to_update, 'Author'] = new_author
                df.loc[df['Title'] == book_to_update, 'Year'] = new_year
                df.loc[df['Title'] == book_to_update, 'Genre'] = new_genre
                df.loc[df['Title'] == book_to_update, 'Read'] = new_read
                
                df.to_csv(library_file, index=False)
                st.success("Book updated successfully!")
                
    except FileNotFoundError:
        st.error("No books found in the library. Please add some books first.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
   
