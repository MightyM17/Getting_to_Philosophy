# Getting to Philosophy
This is a fun project in which clicking the first link in the main text that is NOT in brackets and NOT italicised of a Wikipedia article, and then repeating the process for next articles, will bring you to Philosophy article.

https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy

For example :

https://en.wikipedia.org/wiki/Football_in_Spain ->
https://en.wikipedia.org/wiki/Association_football ->
https://en.wikipedia.org/wiki/Team_sport ->
https://en.wikipedia.org/wiki/Sport ->
https://en.wikipedia.org/wiki/Competition ->
https://en.wikipedia.org/wiki/Goal ->
https://en.wikipedia.org/wiki/Idea ->
https://en.wikipedia.org/wiki/Philosophy

It might get stuck in a loop sometimes

https://en.wikipedia.org/wiki/Mathematical_object ->
https://en.wikipedia.org/wiki/Abstract_concept ->
https://en.wikipedia.org/wiki/Abstraction ->
https://en.wikipedia.org/wiki/Rule_of_inference ->
https://en.wikipedia.org/wiki/Logical_form ->
https://en.wikipedia.org/wiki/Logic -> 
https://en.wikipedia.org/wiki/Rule_of_inference ->
https://en.wikipedia.org/wiki/Logical_form ->
https://en.wikipedia.org/wiki/Logic ->
https://en.wikipedia.org/wiki/Rule_of_inference ->
https://en.wikipedia.org/wiki/Logical_form ->
https://en.wikipedia.org/wiki/Logic ->
https://en.wikipedia.org/wiki/Rule_of_inference

(So basically if it gets to something Math related it goes into a loop.)
There may be more loops with other articles.

## Files
* wikipedia.py (script to automatically go to first link)

### Issues
~~The script deletes everything in brackets which includes wikipedia links like `https://en.wikipedia.org/wiki/Entente_(type_of_alliance)` which becomes `https://en.wikipedia.org/wiki/Entente_()` thus breaking the script.~~

Pages with images/tables in side like `https://en.wikipedia.org/wiki/History_of_Asian_art` can cause issues as they are considered before main text in html.
