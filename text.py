import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

one_piece_text = """
Rubber bodied dreamer Monkey D Luffy gathers an eclectic pirate crew and braves the perilous Grand Line battling tyrants and monsters to claim the legendary One Piece and become King of the Pirates
There once lived a pirate named Gol D Roger He obtained wealth fame and power to earn the title of Pirate King When he was captured and about to be executed he revealed that his treasure called One Piece was hidden somewhere at the Grand Line This made all people set out to search and uncover the One Piece treasure but no one ever found the location of Gol D Rogers treasure and the Grand Line was too dangerous a place to overcome Twenty two years after Gol D Rogers death a boy named Monkey D Luffy decided to become a pirate and search for Gol D Rogers treasure to become the next Pirate King
J LeGault
The man who had acquired everything in this world the Pirate King is Gol D Roger The final words he said at the execution tower were My treasures If you want it Ill let you have it Look for it I left all of it at that place These words sent many to the seas chasing their dreams headed toward the Grand Line in search of One Piece And a new age began Seeking to be the greatest pirate in the world young Monkey D Luffy also heads toward the Grand Line in search of One Piece With his diverse crew joining him along the way consisting of a swordsman marksman navigator cook doctor archaeologist cyborg shipwright musician and a fishman helmsman this will be one memorable adventure
Ne0Freedom
Gol D Roger was known as the Pirate King the strongest and most infamous being to have sailed the Grand Line The capture and execution of Roger by the World Government brought a change throughout the world His last words before his death revealed the existence of the greatest treasure in the world One Piece It was this revelation that brought about the Grand Age of Pirates men who dreamed of finding One Piece which promises an unlimited amount of riches and fame and quite possibly the pinnacle of glory and the title of the Pirate King Enter Monkey D Luffy a 17 year old boy who defies your standard definition of a pirate Rather than the popular persona of a wicked hardened toothless pirate ransacking villages for fun Luffys reason for being a pirate is one of pure wonder the thought of an exciting adventure that leads him to intriguing people and ultimately the promised treasure Following in the footsteps of his childhood hero Luffy and his crew travel across the Grand Line experiencing crazy adventures unveiling dark mysteries and battling strong enemies all in order to reach the most coveted of all fortunes One Piece
"""
stopwords=list(STOP_WORDS)
print(stopwords)

nlp=spacy.load("en_core_web_sm")