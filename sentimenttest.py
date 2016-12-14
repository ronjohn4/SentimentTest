"""Framework for comparing sentiment results.

Sentiment libraries return varying results mainly because they are created with various purposes.
This framework runs through a list of sample sentences and displays the sentiment results for human
comparison.  There are 3 libraries compared in this iteration.
"""
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
import pysentiment as ps
import afinn

# The test sentences have been sampled from several of the tested libraries.
sentences = [
"VADER is smart, handsome, and funny.",
"VADER is smart, handsome, and funny!",
"VADER is very smart, handsome, and funny.",
"VADER is VERY SMART, handsome, and FUNNY.",
"VADER is VERY SMART, handsome, and FUNNY!!!",
"VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!",
"The book was good.",
"The book was kind of good.",
"The plot was good, but the characters are uncompelling and the dialog is not great.",
"A really bad, horrible book.",
"At least it isn't a horrible book.",
":) and :D",
"",
"Today sux",
"Today sux!",
"Today SUX!",
"Today kinda sux! But I'll get by, lol"
"Most automated sentiment analysis tools are shit.",
"VADER sentiment analysis is the shit.",
"Sentiment analysis has never been good.",
"Sentiment analysis with VADER has never been this good.",
"Warren Beatty has never been so entertaining.",
"I won't say that the movie is astounding and I wouldn't claim that \
the movie is too banal either.",
"I like to hate Michael Bay films, but I couldn't fault this one",
"It's one thing to watch an Uwe Boll film, but another thing entirely \
to pay for it",
"The movie was too good",
"This movie was actually neither that funny, nor super witty.",
"This movie doesn't care about cleverness, wit or any other kind of \
intelligent humor.",
"Those who find ugly meanings in beautiful things are corrupt without \
being charming.",
"There are slow and repetitive parts, BUT it has just enough spice to \
keep it interesting.",
"The script is not fantastic, but the acting is decent and the cinematography \
is EXCELLENT!",
"Roger Dodger is one of the most compelling variations on this theme.",
"Roger Dodger is one of the least compelling variations on this theme.",
"Roger Dodger is at least compelling as a variation on the theme.",
"they fall in love with the product",
"but then it breaks",
"usually around the time the 90 day warranty expires",
"the twin towers collapsed today",
"However, Mr. Carter solemnly argues, his client carried out the kidnapping \
under orders and in the ''least offensive way possible.''"
]

# pysentiment SETUP
hiv4 = ps.HIV4()

# afinn setup
afinn = afinn.Afinn()

for sentence in sentences:
    print(sentence)

    # vaderSentiment
    vs = vaderSentiment(sentence)
    print("  {0:16}  pos:{1:5.3f}  neg:{2:5.3f}".format('vaderSentiment', s['pos'], vs['neg']))

    # pysentiment
    tokens = hiv4.tokenize(sentence)
    score = hiv4.get_score(tokens)
    print("  {0:16}  pos:{1:5.3f}  neg:{2:5.3f}".format('pysentiment', score['Positive'], score['Negative']))

    # afinn
    print("  {0:16}  val:{1:5.3f}".format('AFinn', afinn.score(sentence)))

    print()
