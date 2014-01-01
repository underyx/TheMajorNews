TheMajorNews
============

A Twitter bot that takes randomly generated headlines from
[@TwoHeadlines](https://twitter.com/TwoHeadlines), repeatedly translates them
to and from Korean until the sentence becomes absolutely garbled, and then
posts it to its own account, [@TheMajorNews](https://twitter.com/TheMajorNews).

Installation
============

 1. `git clone` this repo.
 2. Reconsider if you really need to set this thing up on your PC.
    (I mean, why would you?)
 3. Install the required libraries specified in `requirements.txt`
 4. Create a `config.py` file based on `config.py.template`
 5. Run the thing!

The Story
=========

On 2014 Jan 1st, 6:48am CET I remembered reading about an intriguing project on
the Internet a year or so before, where a guy wrote [a bot that bought him
random items from Amazon every month](http://randomshopper.tumblr.com/). I
decided to check what came of this whole thing—sadly, there haven't really been
updates recently. However, on the project's blog, I've seen a reference to
another thing this awesome guy, [Darius Kazemi](http://tinysubversions.com/)
made; this was [@TwoHeadlines](https://twitter.com/TwoHeadlines). After having
a good chuckle or two at a few of the bot's tweets, I had this idea to run a
tweet or two through this other great site I randomly found years ago,
[translationparty.com](http://translationparty.com). Being bored as I was, not
even 5 hours later I had the bot up and running. (And that time includes time
wasted on reddit, so it's not even that bad.)

Oh, also, you might be wondering where the name 'TheMajorNews' came from. Well,
Google Translate, of course!

>**en:** Two Headlines  
>**ko:** 두 주요 뉴스  
>**en:** The major news

Notes
=====

The Google Translate API which I'm using costs me actual, real money. So, if
anyone feels like it, tip me on [GitTip](https://www.gittip.com/Underyx/)! Good
news is: a mere 60 cents is enough to feed the bot for a whole day in worst
case scenario. I still ain't made of money, though, so I might be forced to
take the poor guy down after a few months if no one can spare a dime.
