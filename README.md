# Quote-Guessing-Game-using-Web-Scraping-in-Python
we will scrape a quote and details of the author from any web-site using python framework called BeautifulSoup and develop a guessing game using different data structures and algorithm.


1. Import Required Modules
All necessary libraries are imported at the beginning of the script.
2. Create a List to Store Scraped Quotes
Quotes are stored as dictionaries in a list with keys: text, author, and bio-link.
3. Scrape Data from the Website
The script loops through all pages of any site, extracting quotes and author details.
4. Extract Quote Details
Each quote includes:
- The quote text
- The author’s name
- A link to the author’s biography
5. Game Logic
- A random quote is selected.
- The user has 4 guesses to identify the author.
- After each incorrect guess, a hint is provided:
- Hint 1: Author’s birth date and location
- Hint 2: First letter of the author’s first name
- Hint 3: First letter of the author’s last name
- The game ends with a success message or reveals the correct author after all guesses are used.



