# ironITA@Evalita 2018

The IronITA (Irony Detection in Italian Tweets) shared task will be organised within Evalita 2018, the 6th evaluation campaign of Natural Language Processing and Speech tools for Italian, which will be held in Turin, Italy, on December 12 or 13, 2018. Evalita will be co-located with CLiC-it 2018	



# Fair Use Policy 

Please, cite the following paper if you intend to use our dataset for your own research:
>  Alessandra Teresa Cignarella, Simona Frenda, Valerio Basile, Cristina Bosco, Viviana Patti, Paolo Rosso (2018) [Overview of the EVALITA 2018 Task on Irony Detection in Italian Tweets (IronITA)](http://ceur-ws.org/Vol-2263/paper005.pdf) Proceedings of 6th Evaluation Campaign of Natural Language Processing and Speech Tools for Ital- ian. Final Workshop (EVALITA 2018), Turin, Italy. CEUR.org.

 ## Introduction and Motivation

Irony is a figurative language device that conveys the opposite of literal meaning profiling intentionally a secondary or extended meaning. Users on the Web usually tend to use irony like a good creative device to express their thoughts in context of short-texts like tweets, reviews, posts or commentaries. But irony as well as other figurative language devices (for example metaphor) is very difficult to deal with and precisely for its traits of recalling an other meaning or obfuscating the real meaning, it hinders correct sentiment analysis of texts and, therefore, correct opinion mining. Indeed, the presence of ironic devices in a text can work as an unexpected “polarity reverser” (one says something “good” to mean something “bad”), thus undermining systems’ accuracy.

Considering the majority of state-of-the-art studies in Computational Linguistics, “irony” is as an umbrella term which includes satire, sarcasm and parody due to fuzzy boundaries between them, and especially sarcasm is defined as sharp or cutting ironic expressions with the intent to convey scorn or insult [Gibbs, 2000]. The importance to detect irony and sarcasm is interesting per se, but also due to the possibility of reaching better predictions in sentiment analysis and for understanding what is the real opinion and orientation (positive or negative) of users about a specific subject (product, service, topic, issue, person, organization, or event).

IronITA is, on the one hand, in continuity with previous shared tasks organized in the last years within the context of the EVALITA evaluation campaign (see for instance the irony detection subtask proposed at SENTIPOLC in the 2014 and 2016 editions [Basile et al., 2014, Barbieri et al., 2016]) and, on the other hand, also inspired by the recent experience within the Semeval2018-Task 3  - Irony detection in English tweets. We propose also for the Italian community a shared task which is specifically dedicated to irony detection, proposing both the classical binary classification task (irony vs not irony), with a wider amount of data, and a related subtask, which gives to participants the possibility to reason on different types of irony.

In particular, as a difference with Semeval2018-Task3, in the context of this subtask, we will propose to the participants to distinguishing sarcasm as a specific type of irony different from other forms of irony. This is motivated by the growing interest for detecting this particular kind of irony, characterized by its sharp tones and aggressive intention [Gibbs, 2000, Joshi et al., 2017, Sulis et al., 2016], which is often present in many interesting domains, such as for instance the political domain and the one related to hate speech [Poletto et al., 2017].

## Target Audience

The task is open to everyone from industry and academia. We in particular encourage the participations of researchers, industrial teams, and students.

## Task description

We propose two different subtasks for the automatic detection of irony on Twitter. Participants may choose to participate to both the task or only to one sub-task.

A) Irony detection

The first subtask is a two-class (or binary) classification task where the system has to predict whether a tweet is ironic or not:

Given a message, decide whether the message is ironic or not.

B) Different types of irony (with special focus on sarcasm identification)

The second subtask is a multi-class classification task where the system has to predict one out of three labels describing i) sarcasm; ii) irony which cannot be categorized as sarcasm (i.e. other kinds of verbal irony or descriptions of situational irony which do not show the characteristics of sarcasm); iii) non-irony:

Given a message, decide whether the message is  sarcastic, ironic but not sarcastic or not ironic

Notice that in our interpretation sarcasm is a specific kind of irony.

Overall, this drop-down task that we propose aims at being an incentive to investigate more deeply the linguistic device of irony. Still nowadays, in fact, it is interpretable as a difficult job especially when dealing with social media data, where the shortness of text and the extraction of the statement from his context usually makes it hard to understand irony even for humans.

## relation with the HaSpeeDe@evalita2018 shared task

We plan to share a part of data set in slight overlap with another task proposal in parallel to ours at EVALITA 2018. In particular, we will include in our 
set tweets related to three social groups deemed as potential Hate Speech targets in the Italian context [Poletto et al., 2017]. This portion of tweets overlaps with the task proposed at EVALITA 2018: Hate Speech Detection (HaSpeeDe).

## data

The dataset will include short documents taken from Twitter.
A detailed description of data (topics, annotation scheme applied, data format, etc.) will be realeased soon in the Task guidelines.

## evaluation

Each participating team will initially have access to the training data only. Later, the unlabelled test data will be released (see the timeframe below). After the assessment, the labels for the test data will be released as well.

The evaluation will be performed according to the standard metrics known in literature (accuracy, precision, recall and F1-score). The submissions will be ranked by F1-score (precision, recall and F-measure). Details on evaluation metrics to be applied for the evaluation of the participant results will be published in the Task guidelines soon. 

## references

[Basile et al., 2014] Basile, V., Bolioli, A., Nissim, M., Patti, V., and Rosso, P. (2014). Overview of the Evalita 2014 sentiment polarity classification task. In Proceedings of the 4th evaluation campaign of Natural Language Processing and Speech tools for Italian (EVALITA’14).

[Benamara et al., 2017] Benamara, F., Grouin, C., Karoui, J., Moriceau, V., and Robba, I., editors (2017). Analyse d’opinion et langage figuratif dans des tweets : présentation et résultats du Défi Fouille de Textes DEFT2017. TALN 2017, Orléans.

[Bosco et al., 2017] Bosco, C., Patti, V., Bogetti, M., Conoscenti, M., Ruffo, G., Schifanella, R., and Stranisci, M. (2017). Tools and resources for detecting hate and prejudice against immigrants in social media. In Symposium on Social Interactions in Complex Intelligent Systems (SICIS) at AISB 2017, pages 79–84. AISB.

[Cignarella et al., 2017] Cignarella, A. T., Bosco, C., and Patti, V. (2017). Twittirò: A social media corpus with a multi-layered annotation for irony. In CEUR Workshop Proceedings, volume 2006, pages 1–6. CEUR.

[Ghosh et al., 2015] Ghosh, A., Li, G., Veale, T., Rosso, P., Shutova, E., Barnden, J., and Reyes, A. (2015). Semeval-2015 task 11: Sentiment Analysis of Figurative Language in Twitter. In Proceedings of SemEval 2015, Co-located with NAACL, page 470–478. ACL.

[Gibbs, 2000] Gibbs, R. W. (2000). Irony in talk among friends. Metaphor and symbol, 15(1-2):5–27. [Joshi et al., 2017] Joshi, A., Bhattacharyya, P., and Carman, M. J. (2017). Automatic sarcasm detection: A survey. ACM Comput. Surv., 50(5):73:1–73:22.

[Karoui et al., 2017] Karoui, J., Farah, B., Moriceau, V., Patti, V., Bosco, C., and Aussenac-Gilles, N. (2017). Exploring the impact of pragmatic phenomena on irony detection in tweets: A multilingual corpus study. In Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 1, Long Papers, volume 1, pages 262–272.

[Mohammad et al., 2017] Mohammad, S. M., Sobhani, P., and Kiritchenko, S. (2017). Stance and sentiment in tweets. ACM Transactions on Internet Technology (TOIT), 17(3):26.

[Poletto et al., 2017] Poletto, F., Stranisci, M., Sanguinetti, M., Patti, V., and Bosco, C. (2017). Hate speech annotation: Analysis of an Italian Twitter corpus. In CEUR Wokshop Proceedings, volume 2006. CEUR.

[Sanguinetti et al., 2018] Sanguinetti, M., Bosco, C., Lavelli, A., Mazzei, A., Antonelli, O., and Tamburini, F. (in press, 2018). PoSTWITA-UD: an Italian Twitter treebank in Universal Dependencies. In Proceedings of LREC18.

[Sanguinetti et al., 2017] Sanguinetti, M., Bosco, C., Mazzei, A., Lavelli, A., and Tamburini, F. (2017). Annotating Italian social media texts in Universal Dependencies. In Proceedings of the Fourth International Conference on Dependency Linguistics (Depling 2017), pages 229–239.

[Stranisci et al., 2016] Stranisci, M., Bosco, C., Farías, D. I. H., and Patti, V. (2016). Annotating sentiment and irony in the online italian political debate on #labuonascuola. In Chair), N. C. C., Choukri, K., Declerck, T., Goggi, S., Grobelnik, M., Maegaard, B., Mariani, J., Mazo, H., Moreno, A., Odijk, J., and Piperidis, S., editors, Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC 2016), Paris, France. European Language Resources Association (ELRA).

[Sulis et al., 2016] Sulis, E., Hernández Farías, I., Rosso, P., Patti, V., and Ruffo, G. (2016). Figurative messages and affect in twitter: Differences between #irony, #sarcasm and #not. Knowledge-Based Systems, 108:132 – 143. New Avenues in Knowledge Bases for Natural Language Processing. 

# organizers

Alessandra Cignarella, University of Turin, Turin, Italy

Simona Frenda, University of Turin, Turin, Italy

Valerio Basile, University of Turin, Turin, Italy

Cristina Bosco, University of Turin, Turin, Italy

Viviana Patti, University of Turin, Turin, Italy

Paolo Rosso, Universitat Politècnica de València, Spain

# credits

Sergio Rabellino, ICT Staff, Dipartimento di Informatica, University of Torino, Italy
