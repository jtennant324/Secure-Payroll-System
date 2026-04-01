import hashlib

# CONCEPT: This simulates a 'Dictionary Attack'
# We are trying to find the 'Plain Text' version of a 'Hash'

# 1. Open your 'user_data.txt' and copy the long string of numbers/letters next to your name.
# 2. Paste it between the quotes below:
target_hash = "8353269e5518544db2b33dc2afc21855df92512d8cab0e629bf3abd24a71b3e6" 

# A list of common passwords a hacker might try
dictionary = ["password", "123456", "admin", "CVS2026", "Jessica2026"]

print(f"Attempting to crack hash: {target_hash}...\n")

for guess in dictionary:
    # Hash the guess to see if the 'smoothie' matches
    guess_hash = hashlib.sha256(guess.encode()).hexdigest()
    
    if guess_hash == target_hash:
        print(f"--- MATCH FOUND! ---")
        print(f"The password is: {guess}")
        break
    else:
        print(f"Testing: {guess}... No match.")