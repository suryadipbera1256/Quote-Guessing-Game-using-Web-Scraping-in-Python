import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
import streamlit as st

# Function to scrape all quotes
@st.cache_data
def scrape_quotes():
    base_url = "http://quotes.toscrape.com"
    url = "/page/1"
    all_quotes = []

    while url:
        res = requests.get(f"{base_url}{url}")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })

        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        sleep(0.5)  # gentle delay

    return all_quotes

# Load quotes
quotes = scrape_quotes()
quote = st.session_state.get("quote", choice(quotes))
remaining_guesses = st.session_state.get("remaining_guesses", 4)

# UI
st.title("🧠 Quote Guessing Game")
st.write("Can you guess who said this quote?")
st.markdown(f"> {quote['text']}")

# Input
guess = st.text_input("Your guess:", key="guess_input")

# Game logic
if guess:
    if guess.lower() == quote["author"].lower():
        st.success("🎉 Correct! You guessed it right.")
        if st.button("Play Again"):
            st.session_state.quote = choice(quotes)
            st.session_state.remaining_guesses = 4
            st.rerun()
    else:
        st.session_state.remaining_guesses = remaining_guesses - 1
        remaining_guesses = st.session_state.remaining_guesses
        st.warning(f"Wrong guess. {remaining_guesses} guesses left.")

        # Hints
        if remaining_guesses == 3:
            res = requests.get(f"http://quotes.toscrape.com{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            st.info(f"Hint: Born on {birth_date} {birth_place}")
        elif remaining_guesses == 2:
            st.info(f"Hint: First name starts with '{quote['author'][0]}'")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            st.info(f"Hint: Last name starts with '{last_initial}'")
        elif remaining_guesses == 0:
            st.error(f"Out of guesses! The author was {quote['author']}")
            if st.button("Try Another"):
                st.session_state.quote = choice(quotes)
                st.session_state.remaining_guesses = 4
                st.rerun()