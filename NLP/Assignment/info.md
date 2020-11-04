## Searching Text

There are many ways to examine the context of a text apart from simply reading it. A concordance view shows us every occurrence of a given word, together with some context. Here we look up the word monstrous in *Moby Dick* by entering text1 followed by a period, then the term concordance, and then placing "monstrous" in parentheses:

**from nltk.book import *
text1.concordance("monstrous")**

A concordance permits us to see words in context. For example, we saw that monstrous occurred in contexts such as the ___ pictures and a ___ size . What other words appear in a similar range of contexts? We can find out by appending the term similar to the name of the text in question, then inserting the relevant word in parentheses:

**text1.similar("monstrous")**

The term common\_contexts allows us to examine just the contexts that are shared by two or more words, such as monstrous and very. We have to enclose these words by square brackets as well as parentheses, and separate them with a comma:

**text2.common_contexts(["monstrous", "very"])**

most frequesnt words :

from collections import Counter
Counter(words).most_common(15)

from nltk.book import *
fdist1 = FreqDist(words)
fdist1.most_common(50)

A collocation is a sequence of words that occur together unusually often. Thus red wine is a collocation, whereas the wine is not. A characteristic of collocations is that they are resistant to substitution with words that have similar senses; for example, maroon wine sounds definitely odd.

To get a handle on collocations, we start off by extracting from a text a list of word pairs, also known as bigrams. This is easily accomplished with the function bigrams():

list(bigrams([]))
text8.collations()

| Example | Description |
| --- | --- |
| fdist = FreqDist(samples) | create a frequency distribution containing the given samples |
| fdist\[sample\] += 1 | increment the count for this sample |
| fdist\['monstrous'\] | count of the number of times a given sample occurred |
| fdist.freq('monstrous') | frequency of a given sample |
| fdist.N() | total number of samples |
| fdist.most\_common(n) | the n most common samples and their frequencies |
| for sample in fdist: | iterate over the samples |
| fdist.max() | sample with the greatest count |
| fdist.tabulate() | tabulate the frequency distribution |
| fdist.plot() | graphical plot of the frequency distribution |
| fdist.plot(cumulative=True) | cumulative plot of the frequency distribution |
| fdist1 |= fdist2 | update fdist1 with counts from fdist2 |
| fdist1 < fdist2 | test if samples in fdist1 occur less frequently than in fdist2 |
___
