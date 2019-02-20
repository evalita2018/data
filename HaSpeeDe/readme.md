# haspeede2018
The dataset for the Hate Speech Detection Task at Evalita 2018 can be obtained by accessing 
the task official repository of the [Hate Speech Detection Task](https://github.com/msang/haspeede2018)

# Fair Use Policy
Please, cite the following paper if you intend to use our dataset for your own research:
Cristina Bosco, Felice Dell'Orletta, Fabio Poletto, Manuela Sanguinetti, Maurizio Tesconi
[Overview of the EVALITA 2018 Hate Speech Detection Task](http://ceur-ws.org/Vol-2263/paper010.pdf) Proceedings of 6th Evaluation Campaign of Natural Language Processing and Speech Tools for Italian. Final Workshop (EVALITA 2018), Turin, Italy. CEUR.org.


# haspeede@evalita 2018
The HaSpeeDe (Hate Speech Detection) shared task will be organized within Evalita 2018, the 6th evaluation campaign of Natural Language Processing and Speech tools for Italian, which will be held in Turin, Italy, on December 12-13, 2018.

# introduction and motivation

Online hateful content, or Hate Speech (HS), is characterized by some key aspects (such as virality, or presumed anonymity) which distinguish it from offline communication and make it potentially more dangerous and hurtful. Therefore, its identification becomes a crucial mission in many fields.

HaSpeeDe consists in automatically annotating messages from two popular micro-blogging platforms, Twitter and Facebook, with a boolean value indicating the presence (or not) of HS.

It is proposed for the first time for Italian within the context of Evalita, following the success of similar tasks on sentiment analysis, such as those for polarity and subjectivity detection, organized in the two last editions of this campaign.

target audience
The task is open to everyone from industry and academia.

task description
Considering the linguistic, as well as meta-linguistic, features that distinguish Twitter and Facebook posts, namely due to the differences in use between the two platforms, the task will be further organized into three sub-tasks, based on the dataset used:

A) HaSpeeDe-FB, where only the Facebook dataset can be used to classify the Facebook test set

B) HaSpeeDe-TW, where only the Twitter dataset can be used to classify the Twitter test set

C) Cross-HaSpeeDe, where only the Facebook dataset can be used to classify the Twitter test set and vice versa

relation with ironita@evalita2018
Considering that a small portion of the task dataset contains ironic tweets, such set will also be used in another shared task proposed for EVALITA 2018, namely the one for irony detection (ironITA)

# data

The dataset proposed for this task is the result of a joint effort of two research groups on unifying the annotation previously applied to two different datasets, in order to allow their exploitation in the task.

The first dataset is a collection of Facebook posts developed by the group from Pisa and created in 2016 [Del Vigna et al. 2017], while the other one is a Twitter corpus developed in 2018 by the group from Turin [Poletto et al. 2017; Sanguinetti et al. 2018].

The annotation format is the same for both datasets used for this task, and it consists of a simplified version of the schemes adopted in the two corpora mentioned above: it thus comprises the tweet or Facebook comment along with the respective annotation.

The tags included in the scheme are only 1 and 0, expressing the presence or not of hate speech in the post, respectively.

# evaluation

Each participating team will initially have access to the training data only. Later, the unlabeled test data will be released (see the timeframe below). After the assessment, the labels for the test data will be released as well.

The evaluation will be performed according to the standard metrics known in literature (precision, recall and F-measure). Details on evaluation metrics to be applied for the evaluation of the participant results will be published in the Task guidelines.


# references
[Bosco et al. 2017] Cristina Bosco, Patti Viviana, Marcello Bogetti, Michelangelo Conoscenti, Giancarlo Ruffo, Rossano Schifanella, and Marco Stranisci. Tools and resources for detecting hate and prejudice against immigrants in social media. In Proceedings of First Symposium on Social Interactions in Complex Intelligent Systems (SICIS), AISB Convention 2017, AI and Society, Bath, UK, 2017.

[Burnap and Williams 2015] Pete Burnap and Matthew L. Williams. Cyber hate speech on twitter: An application of machine classification and statistical modeling for policy and decision making. Policy & Internet, 7(2):223–242, 2015.

[Davidson et al. 2017] Thomas Davidson, Dana Warmsley, Michael W. Macy, and Ingmar Weber. Automated hate speech detection and the problem of offensive language. CoRR, abs/1703.04009, 2017.

[Del Vigna 2017] Fabio Del Vigna, Andrea Cimino, Felice Dell’Orletta, Marinella Petrocchi, and Maurizio Tesconi. Hate me, hate me not: Hate speech detection on Facebook. In Proceedings of the First Italian Conference on Cybersecurity (ITASEC17), Venice, Italy, January 17-20, 2017., pages 86–95, 2017.

[Erjavec and Kovacic 2012] Karmen Erjavec and Melita Poler Kovacic. "You don’t understand, this is a new war!" Analysis of hate speech in news web sites’ comments. Mass Communication and Society, 15(6):899–920, 2012.

[Gambäck and Sikdar 2017] Björn Gambäck and Utpal Kumar Sikdar. Using convolutional neural networks to classify hate-speech. In Proceedings of the First Workshop on Abusive Language, 2017.

[Gitari et al. 2015] Njagi Dennis Gitari, Zhang Zuping, Hanyurwimfura Damien, and Jun Long. A lexicon-based approach for hate speech detection. International Journal of Multimedia and Ubiquitous Engineering, 10(4):215—-230, 2015.

[Kwok and Wang 2013] Irene Kwok and Yuzhou Wang. Locate the hate: Detecting tweets against blacks. In Marie desJardins and Michael L. Littman, editors, AAAI. AAAI Press, 2013.

[Mehdad and Tetreault 2016] Yashar Mehdad and Joel Tetreault. Do characters abuse more than words? In 17th Annual Meeting of the Special Interest Group on Discourse and Dialogue, Los Angeles, CA, USA, 2016.

[Musto et al. 2016] Cataldo Musto, Giovanni Semeraro, Marco de Gemmis, and Pasquale Lops. Modeling community behavior through semantic analysis of social data: The italian hate map experience. In Proceedings of the 2016 Conference on User Modeling Adaptation and Personalization, UMAP 2016, Halifax, NS, Canada, July 13 - 17, 2016, pages 307–308, 2016.

[Pelosi et al. 2017] Serena Pelosi, Alessandro Maisto, Pierluigi Vitale, and Simonetta Vietri. Mining offensive language on social media. In Proceedings of the Fourth Italian Conference on Computational Linguistics (CLiC-it 2017), Rome, Italy, December 11-13, 2017., 2017.

[Poletto et al. 2017] Fabio Poletto, Marco Stranisci, Manuela Sanguinetti, Viviana Patti, and Cristina Bosco. Hate speech annotation: Analysis of an italian twitter corpus. In Proceedings of the Fourth Italian Conference on Computational Linguistics (CLiC-it 2017). CEUR, december 2017.

[Sanguinetti et al. 2018] Manuela Sanguinetti, Fabio Poletto, Cristina Bosco, Viviana Patti, and Marco Stranisci. An italian twitter corpus of hate speech against immigrants. In Proceedings of LREC 2018, May 2018.

[Schmidt and Wiegand 2017] Anna Schmidt and Michael Wiegand. A survey on hate speech detection using natural language processing. In Proceedings of the Fifth International Workshop on Natural Language Processing for Social Media, pages 1–10. Association for Computational Linguistics, 2017.

# organizers

Cristina Bosco, University of Turin, Turin, Italy

Felice Dell'Orletta, Istituto di Linguistica Computazionale "Antonio Zampolli" - CNR, Pisa, Italy

Fabio Poletto, University of Turin, Turin, Italy

Manuela Sanguinetti, University of Turin, Turin, Italy

Maurizio Tesconi, Istituto di Informatica e Telematica - CNR, Pisa, Italy

For more information on the task, see also the guidelines available in this repository, and the web page. You can also join our Google group at haspeede-evalita2018@googlegroups.com
