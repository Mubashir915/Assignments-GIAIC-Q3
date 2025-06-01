import streamlit as st
import json
import os

DATA_FILE = "library.json"

# Load library from file
def load_library():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save library to file
def save_library(library):
    with open(DATA_FILE, "w") as f:
        json.dump(library, f, indent=4)

# Format book info string
def format_book(book):
    status = "Read" if book["read"] else "Unread"
    return f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}"

# Main Streamlit app
def main():
    st.title("📚 Personal Library Manager")

    # Load library into session state
    if "library" not in st.session_state:
        st.session_state.library = load_library()

    library = st.session_state.library

    menu = ["Add Book", "Remove Book", "Search Book", "Show All Books", "Statistics"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Book":
        st.header("Add a new book")
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        year = st.number_input("Publication Year", min_value=0, max_value=2100, step=1)
        genre = st.text_input("Genre")
        read = st.checkbox("Have you read this book?")

        if st.button("Add Book"):
            if title and author and genre:
                book = {
                    "title": title.strip(),
                    "author": author.strip(),
                    "year": int(year),
                    "genre": genre.strip(),
                    "read": read
                }
                library.append(book)
                save_library(library)
                st.success(f"📚 Book '{title}' added successfully!")
            else:
                st.error("Please fill in all the fields.")

    elif choice == "Remove Book":
        st.header("Remove a book")
        if not library:
            st.info("Your library is empty.")
        else:
            titles = [book["title"] for book in library]
            book_to_remove = st.selectbox("Select book to remove", titles)
            if st.button("Remove Book"):
                for book in library:
                    if book["title"] == book_to_remove:
                        library.remove(book)
                        save_library(library)
                        st.success(f"🗑️ Book '{book_to_remove}' removed.")
                        break

    elif choice == "Search Book":
        st.header("Search books by Title or Author")
        search_term = st.text_input("Enter search term").strip().lower()
        search_by = st.radio("Search by", ("Title", "Author"))

        if st.button("Search"):
            if not search_term:
                st.warning("Please enter a search term.")
            else:
                if search_by == "Title":
                    results = [b for b in library if search_term in b["title"].lower()]
                else:
                    results = [b for b in library if search_term in b["author"].lower()]

                if results:
                    st.success(f"Found {len(results)} matching book(s):")
                    for book in results:
                        st.write(format_book(book))
                else:
                    st.error("No matching books found.")

    elif choice == "Show All Books":
        st.header("Your Library")
        if not library:
            st.info("Your library is empty.")
        else:
            for book in library:
                st.write(format_book(book))

    elif choice == "Statistics":
        st.header("Library Statistics")
        total = len(library)
        read_count = sum(1 for b in library if b["read"])
        percent_read = (read_count / total * 100) if total > 0 else 0

        st.write(f"Total books: **{total}**")
        st.write(f"Books read: **{read_count}**")
        st.write(f"Percentage read: **{percent_read:.2f}%**")

if __name__ == "__main__":
    main()
