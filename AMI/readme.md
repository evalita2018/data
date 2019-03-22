# AMI@Evalita2018
The dataset for the Automatic Misogyny Identification (AMI) Shared Task at Evalita 2018 can be obtained by accessing 
the task official repository of the [AMI](https://github.com/MIND-Lab/ami2018)

# Fair Use Policy
Please, cite the following paper if you intend to use our dataset for your own research:
Elisabetta Fersini, Debora Nozza, Paolo Rosso
[Overview of the Evalita 2018 Task on Automatic Misogyny Identification (AMI)](http://ceur-ws.org/Vol-2263/paper009.pdf) Proceedings of 6th Evaluation Campaign of Natural Language Processing and Speech Tools for Italian. Final Workshop (EVALITA 2018), Turin, Italy. CEUR.org.


# Automatic Misogyny Identification
The AMI (Automatic Misogyny Identification) shared task has been organized within Evalita 2018, the 6th evaluation campaign of Natural Language Processing and Speech tools for Italian, which will be held in Turin, Italy, on December 12-13, 2018.

# Introduction and Motivation

Given the huge amount of user-generated contents on the Web, and in particular on social media, the problem of detecting, and therefore possibly limiting the diffusion of hate speech against women, is rapidly becoming fundamental especially for the societal impact of the phenomenon. The AMI shared task is aimed at automatically identifying misogynous content in Twitter both in Italian and English languages.  More specifically, it is a two-fold task, as it follows.

Task A: Misogyny Identification

The main goal is to label each tweet either as misogynous or not misogynous.

Task B: Misogynistic Behaviour and Target Classification

The main goal is to classify the misogynous tweets according to both the misogynistic behaviour and the target of the message.

More specifically, each misogynous tweet must be classified uniquely within one of the following misogynistic behaviour:

* Stereotype & Objectification: a widely held but fixed and oversimplified image or idea of a woman; description of women’s physical appeal and/or comparisons to narrow standards.
* Dominance: to assert the superiority of men over women to highlight gender inequality.
* Derailing: to justify woman abuse, rejecting male responsibility; an attempt to disrupt the conversation in order to redirect  women’s conversations on something more comfortable for men.
* Sexual Harassment & Threats of Violence: to describe actions as sexual advances, requests for sexual favors, harassment of a sexual nature; intent to physically assert power over women through threats of violence.
* Discredit: slurring over women with no other larger intention.

Subsequently, each tweet must be classified according to the target:
* Active (individual): the text includes offensive messages purposely sent to a specific target.
* Passive (generic): it refers to messages posted to many potential receivers.


# Data

Regarding the training data, both the Italian and English corpora are composed of 4000 tweets. Concerning the test data, we provided 1000 tweets for each language. The training data has been provided as tab-separated, according to the following fields:
• id denotes a unique identifier of the tweet.
• text represents the tweet text.
• misogynous defines if the tweet is misogynous or not misogynous; it takes values as 1 if the tweet is misogynous, 0 if the tweet is not misogynous.
• misogyny category denotes the type of misogynistic behaviour; it takes value as:
– stereotype: denotes the category “Stereotype & Objectification”;
– dominance: denotes the category “Dominance”;
– derailing: denotes the category “Derailing”;
– sexual_harassment: denotes the category “Sexual Harassment & Threats of Violence”;
– discredit: denotes the category “Discredit”;
– 0 if the tweet is not misogynous.
• target denotes the subject of the misogynistic tweet; it takes value as:
– active: denotes a specific target (individual);
– passive: denotes potential receivers (generic);
– 0 if the tweet is not misogynous.

Regarding the testing data, both the Italian and English corpora are composed of 1000 tweets for each language.

# Evaluation

Each participating team will initially have access to the training data only. Later, the unlabeled test data has been released. After the assessment, the labels for the test data has been released as well.

The two subtasks have been evaluated as follows:

* Subtask A. Systems have been evaluated on the field “misogynous” using the standard accuracy measure, and ranked accordingly.
* Subtask B. Each field to be predicted has been evaluated independently on the other using a Macro F1-score. In particular, the Macro F1-score for the “misogyny category” field has been computed as average of F1-scores obtained for each category (stereotype, dominance, derailing, sexual harassment, discredit), estimating F1(misogyny category). Analogously, the Macro F1-score for the “target” field has been computed as average of F1-scores obtained for each category (active, passive), F1(target). The final ranking of the systems participating to Subtask B was based on the Average Macro F1-score (F1).


# References

[1] Anzovino M., Fersini E., Rosso P. (2018) Automatic Identification and Classification of Misogynistic Language on Twitter. In: Silberztein M., Atigui F., Kornyshova E., Métais E., Meziane F. (eds) Natural Language Processing and Information Systems. NLDB 2018. Lecture Notes in Computer Science, vol 10859.

[2] Poland, B. (2016). Haters: Harassment, Abuse, and Violence Online. University of Nebraska Press.

[3] Hewitt, S., Tiropanis, T., & Bokhove, C. (2016). The problem of identifying misogynist language on Twitter (and other online social spaces). In Proceedings of the 8th ACM Conference on Web Science, pp. 333-335.


# organizers

Elisabetta Fersini, University of Milano-Bicocca, Milan, Italy

Debora Nozza, University of Milano-Bicocca, Milan, Italy

Paolo Rosso, Universitat Politècnica de València, Valencia, Spain 
