# wordlebot
A bot that solves the wordle of the day (most of the time!)

# starting:

To start the bot, simply run the program and press enter whenver you want it to guess. If you want it to solve the current Wordle of the day, just don't touch anything. If you want it to solve a random word, just un-comment line #17 and comment line #18. Line 17 gets a random word while line 18 gets the current wordle of the day using time delta from a start day I set.

The bot works by assigning a point system to each word it thinks has a likelyhood of being the correct word based on how many correct letters and position are in it. If multiple words have the same score, the bot takes the last word from the list of same scored words. This is why the bot may get lower accuracy when dealing with words that have multiple rhymes. 

The bot gets it's words directly from a list in Wordle's source code. The bot will remove points for repeating letters as well as remove any word that contains incorrect letters from the list. The bot gets most words on it's 4th try although not always.

<img width="145" alt="Screen Shot 2022-03-16 at 10 23 37 AM" src="https://user-images.githubusercontent.com/100868154/158650374-52f96336-efc2-484c-b1be-e58bf7d519f0.png">
