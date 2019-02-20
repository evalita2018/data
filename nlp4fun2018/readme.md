EVALITA 2018 - NLP4FUN Data and Scripts
==========================================

Folders description:
* **dev**: development data
* **test**: test data with and without fake games (see the task report for more details)
* **gold**: gold standard annotations
* **out**: output of the participating systems
* *nlp4fun_eval-0.1.jar*: the evaluation script (require Java 1.7)

Evaluation scripts
---------------------

Usage: Evaluate [-g <arg>] [-s <arg>] [-v]<br>
 -g <arg>   Gold standard file<br>
 -s <arg>   System output file<br>
 -v         Verbose mode<br>

For example: *java -jar nlp4fun_eval-0.1.jar -g gold.xml -s system1.out*

# Fair Use Policy 

Please, cite the following paper if you intend to use our dataset for your own research:
>  Pierpaolo Basile, Marco de Gemmis, Lucia Siciliani, Giovanni Semeraro(2018) [Overview of the EVALITA 2018 Solving Language Games (NLP4FUN) Task](http://ceur-ws.org/Vol-2263/paper011.pdf) 
Proceedings of 6th Evaluation Campaign of Natural Language Processing and Speech Tools for Ital- ian. Final Workshop (EVALITA 2018), Turin, Italy. CEUR.org.

