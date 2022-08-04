# H_ng Man (abandoned in development, maybe come back to later)

This is a game of h_ngman with a twist, **you** are the executioner.

**Your Goal**: To **kill** the player, in this case, the AI. The minimum number of tries is 6, however, you can set the number of tries to a custom value or use the preset values.

Since you are playing against the AI, you might need to know the AI strategy.

There are 3 modes, **EASY**, **MEDIUM**, and **DARN NEAR IMPOSSIBLE**, and **SPICY**

## AI Strategy:
**EASY:**
- There are 3 buckets of unique letters, sorted by frequency in general conversation. The AI picks a random item from each bucket starting from the bucket containing the most frequent letters down to the least frequent letters.
    - First Bucket: These are the 8 most frequent letters
    [E, T, A, O, I, N, S, R]
    - Second Bucket: These are the next 9 more frequent letters
    [H, D, L, U, C, M, F, Y, W]
    - Third Bucket: These are the 9 least frequent letters
    [G, P, B, V, K, X, Q, J, Z]

**MEDIUM**:
- Let's call the number of letters in a word **X**
- The AI first gets the length of the word to guess, then searches a database of words (it's "brain") for the 4 most common letters in an **X**-Lettered word. It then randomly picks a letter from the list.
- If it's an incorrect guess, it remvoes that letter, and regenerates the list for the four most common letters per **X** Lettered word.
- If it's a correct guess, then it generates a new list of four items that contain the correct guesses.
- Rinse and Repeat Baby

**DARN NEAR IMPOSSIBLE**:
- Again, let's call the number of guesses in a word **X**
- The AI first gets the length of the word to guess, then searches a database of words (it's "brain") and guesses the most common letter in an **X**-Lettered word. 
- If the guess is incorrect, then it elminates that item from the alphabetical list and generates a new letter to guess.
- If the generated guess is correct, then the AI generates a new guess based on the previous guess
- Rinse and repeat baby


**SPICY**:
- A random mix of all three solution methods
