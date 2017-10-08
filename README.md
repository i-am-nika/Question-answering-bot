# Question-answering-bot San123
Telegram bot, who answers more than 30.000 questions, using Wikipedia

SUMMARY:

The San123 (@San123_bot in Telegram) is a question-answering system that implements 
Levenshtein Distance to calculates differences between sequences
and can answer about 30.000 questions from WikiQA Dataset**. 

Examples of questions:
"how are glacier caves formed?"
"How are the directions of the velocity and force vectors related in a circular motion"
"how a beretta model 21 pistols magazines works"
"how much is 1 tablespoon of water"
"how a rocket engine works"
"how bruce lee died"
"how old were golden girls at time of show"
---------------------------------------------------------------------------------------------------------------------------
Please cite it if you use this code:
* San123
#__author__ = "Tetyana Chernenko"
#__version__ = "1.0.0"
#__maintrainer__ = "Tetyana Chernenko"
#__email__ = "tatjana.chernenko@gmail.com"

** Microsoft Research WikiQA Corpus
@InProceedings{YangYihMeek:EMNLP2015:WikiQA,
  author    = {Yang, Yi  and  Yih, Wen-tau  and  Meek, Christopher},
  title     = {{WikiQA}: {A} Challenge Dataset for Open-Domain Question Answering},
  booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  month     = {September},
  year      = {2015},
  address   = {Lisbon, Portugal},
  publisher = {Association for Computational Linguistics}
}
---------------------------------------------------------------------------------------------------------------------------
BEFORE YOU START:

- Install python-leventshtein

- Download WikiQA Corpus (http://research.microsoft.com/en-US/downloads/4495da01-db8c-4041-a7f6-7984a4f6a905/default.aspx). 
Save the WikiQA.tsv file from this Corpus in a separate folder. 
Write the whole name of this folder instead of <YOUR FOLDER> for "path_dic" in the source code.

- Write the HTTP API of your bot instead of <YOUR BOT TOKEN> for "token" in the source code.


---------------------------------------------------------------------------------------------------------------------------

VERSION 1.0.0: October 8, 2017

"""

#san123_bot.py
#usage:
#$ ./san123_bot.py
 #__author__ = "Tetyana Chernenko"
#__copyright__ = "Copyright (c) 2017 Tetyana Chernenko. All rights reserved."
#__credits__ = ["Tetyana Chernenko"]
#__license__ = "GNU General Public License v3.0"
#__version__ = "1.0.0"
#__maintrainer__ = "Tetyana Chernenko"
#__email__ = "tatjana.chernenko@gmail.com"
#__status__ = "Development"

