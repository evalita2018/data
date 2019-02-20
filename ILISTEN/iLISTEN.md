
# Fair Use Policy 

Please, cite the following paper if you intend to use our dataset for your own research:
>  Pierpaolo Basile and Nicole Novielli (2018) [Overview of the Evalita 2018 itaLIan Speech acT labEliNg (iLISTEN) Task](http://ceur-ws.org/Vol-2263/paper007.pdf) Proceedings of 6th Evaluation Campaign of Natural Language Processing and Speech Tools for Ital- ian. Final Workshop (EVALITA 2018), Turin, Italy. CEUR.org.


# Task Description

The task consists in automatically annotating dialogue turns with speech act labels, i.e. with the communicative intention of the speaker, such as statement, request for information, agreement, opinion expression, general answer, etc. [Table 1](#tab1) reports the full set of speech act labels, with definition and examples. Regarding the evaluation procedure, we will assess the ability of each system to issue the correct speech act label among those included in the taxonomy used for annotation, described in the following. Specifically, we will compute precision, recall and F1-score (macroaveraging) with respect to our gold standard. This approach, while more verbose than a simple accuracy test, arise from the need to correctly address the unbalance distribution of labels in the dataset. Furthermore, by providing detailed performance metrics, we aim at enhancing interesting conclusions on the nature of the problem and the data, as they might emerge from the participants’ final reports. As a baseline, we will use the most frequent label for the user speech acts.

<a name="tab1">**Table 1.**</a> Full set of speech act labels.

| Speech Act         | Description | Example |
|:-------------------|:------------|:--------|
| OPENING            | Dialogue opening or self-introduction | *"Ciao, io sono Antonella"* |
| CLOSING            | Dialogue closing, e.g. farewell, wishes, intention to close the conversation | *"Va bene, ci vediamo prossimamente"* |
| INFO-REQUEST       | Utterances that are pragmatically, semantically, and syntactically questions | *"E cosa mi dici delle vitamine?"*|
| SOLICIT-REQ-CLARIF | Request for clarification (please explain) or solicitation of system reaction            | *"Mmm, si ma in che senso?"* |
| STATEMENT          | Descriptive, narrative, personal statements | *"Penso che dovrei controllare maggiormente il consumo di dolciumi."* |
| GENERIC-ANSWER     | Generic answer | *"Si", "No", "Non so"* |
| AGREE       | Expression of agreement, e.g. acceptance of a proposal, plan or opinion            | *"Si, so che è importante."*        |
| REJECT             | Expression of disagreement, e.g. rejection of a proposal, plan, or opinion            | *"Ho sentito tesi contrastanti al proposito."*        |
| KIND-ATT-SMALLTALK | Expression of kind attitude through politeness, e.g. thanking, apologizing or smalltalk | *"Grazie","Sei per caso offesa per qualcosa che ho detto?"*        |

# Data Description

**A Dataset of Dialogues.** We leverage the corpus of natural language dialogues collected in the scope of previous research about Human-ECA interaction [[4]](#4), in order to speed up the process of building a gold standard. The corpus contains overall transcripts of 60 dialogues, 1,576 user dialogue turns, 1,611 system turns and about 22,000 words.

The dialogues were collected using a Wizard of Oz tool as dialogue manager. Sixty subjects (aged between 21–28) involved in the study, in two interaction mode conditions: thirty of them interacted with the system in a written-input setting, using keyboard and mouse; the remaining thirty dialogues were collected with users interacting with the ECA in a spoken-input condition. Dialogues collected using the spoken interaction mode were manually transcribed based on audio-recording of the dialogue sessions. Information about interaction mode (spoken vs. written) will be provided to participant with the dataset.

During the interaction, the ECA played the role of an artificial therapist and the users were free to interact with it in natural language, without any particular constraint: they could simply answer the question of the agent or taking the initiative and ask questions in their turn, make comments about the agent behavior or competence, argument in favor or against the agent's suggestion or persuasion attempts. The Wizard, on his behalf, had to choose among a set of about 80 predefined possible move. As such, the pre-defined system moves are provided only as a context information but will not be subject to evaluation and will not contribute to the final ranking of the participant systems. Conversely, systems will be evaluated on the basis of the performance observed for the user dialogue turns.

**Annotation.** Speech acts can be identified with the communicative goal of a given utterance, i.e. it represents its meaning at the level of its *illocutionary force* [[1]](#1).
In defining dialogue act taxonomies, researchers have been trying to solve the trade-off between the need for formal semantics and the need for computational feasibility, also taking into account the specificity of the many application domains that have been investigated (see [[8]](#8) for an exhaustive overview). The Dialogue Act Markup in Several Layers (DAMSL) represent an attempt by [[2]](#2) to define a domain independent framework for speech act annotation.

Defining a DA markup language is out of the scope of the present study. Therefore, we adopt the original annotation of the Italian advice-giving dialogues. [Table 1](#tab1) shows the set of nine labels employed for the purpose of this study, with definitions and examples. The taxonomy refines the DAMSL categories to allow appropriate tagging of the communicative intention with respect to the application domain, i.e. persuasion dialogues in the healthy eating domain.

In [Table 2](#tab2) we provide an excerpt from a dialogue from our gold standard. The system moves (dialogue moves and corresponding speech act labels) will be only as a context information. Conversely, **the final ranking of the participating systems will be performed based on the performance observed only on the users' move**, with respect to the set of users' label provided in [Table 1](#tab1). Please, note that the set of agent's moves will include also speech acts (such as persuasion attempts) that are observed only for the agent, given its caregiver role in the dialogue systems.

<a name="tab2">**Table 2.**</a> An excerpt from a dialogue.

| Actor | ID    | Speech Act | Dialogue Move |
|:------|:-----|:-----------|:--------------|
| SYSTEM | 5-S1 | OPENING | *Ciao, il mio nome è Valentina. Sono qui per darti dei suggerimenti su come migliorare la tua dieta* |
| USER | 5-U1 | OPENING | *Ciao, il mio nome è Oriana.* |
| SYSTEM | 5-S2 | INFO-REQUEST | *Quali sono le tue abitudini alimentari?* |
| USER | 5-U2 | STATEMENT | *Ho delle abitudini disordinate, mangio anche fuori orario.* |
| SYSTEM | 5-S3 | INFO-REQUEST | *Ti piace mangiare?* |
| USER | 5-U3 | STATEMENT | *Si, ma dipende dal periodo: se sono sotto stress mangio meno, quando sono più rilassata mangio molto* |
| SYSTEM | 5-S4 | INFO-REQUEST | *Segui una dieta variata?* |
| USER | 5-U3 | GENERIC-ANSWER | *No.* |

# Data Format

We will provide a set of both training and testing dialogues in the XML format following the struture proposed in [Table 2](#tab2).

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<dialogues>
  <dialogue>
    <speechAct act="OPENING" actId="13" id="T_5_S1">Ciao, il mio nome e' Valentina. Sono qui per darti dei suggerimenti su come migliorare la tua dieta.</speechAct>
    <speechAct act="OPENING" actId="10" id="T_5_U1">ciao il mio nome è oriana</speechAct>
    <speechAct act="QUESTION" actId="12" id="T_5_S2">Quali sono le tue abitudini alimentari?</speechAct>
    <speechAct act="STAT-ABOUT-SELF" actId="5" id="T_5_U2">ho delle abitudini un pò disordinate,nel senso che mangio anche fupri orario</speechAct>
    <speechAct act="QUESTION" actId="12" id="T_5_S3">Ti piace mangiare?</speechAct>
    <speechAct act="STAT-ABOUT-SELF" actId="5" id="T_5_U2">si,ma dipende dal periodo,se sono sotto stress mangio meno,quando sono più rilassata mangio molto</speechAct>
    <speechAct act="QUESTION" actId="12" id="T_5_S4">Segui una dieta variata?</speechAct>
    <speechAct act="GENERIC-ANSWER" actId="7" id="T_5_U4">no</speechAct>
    ...
```

Each participating team will initially have access to the training data only. Later, the unlabelled test data will be released.

The participants must provide results in a plain text file with comma-separated fields. Only the dialogue turns of the User, marked as **U** (as in id="T_5_**U**4") will be subject to evaluation and should be returned. In the following, we report an example of a what a submitted run should look like. Please, note that the **id** in the first column (in bold) should be the same provided for each User dialogue turn in the test set, while the speech *act* label in the second column (in italic) is the prediction of your system.

>  **id**,*act*<br>
**T_5_U1**,*OPENING*<br>
**T_5_U2**,*STAT-ABOUT-SELF*<br>
**T_5_U4**,*GENERIC-ANSWER*<br>
...


# References
[<a name="1">1</a>] J. L. Austin. How to do things with words. William James Lectures. Oxford University Press, 1962.

[<a name="2">2</a>] M. G. Core and J. F. Allen. Coding dialogs with the damsl annotation scheme, 1997.

[<a name="3">3</a>] J. R. Searle. Speech Acts: An Essay in the Philosophy of Language. Cambridge University Press, Cambridge, London, 1969.

[<a name="4">4</a>] G. Clarizio, I. Mazzotta, N. Novielli, and F. De Rosis. Social attitude towards a conver- sational character. pages 2–7, 2006.

[<a name="5">5</a>]  R. Kar and R. Haldar. Applying chatbots to the internet of things: Opportunities and
architectural elements. CoRR, abs/1611.03799, 2016.

[<a name="6">6</a>] T. Klüwer. “i like your shirt” - dialogue acts for enabling social talk in conversational
agents. In Intelligent Virtual Agents, pages 14–27, 2011.

[<a name="7">7</a>] A. Stolcke, N. Coccaro, R. Bates, P. Taylor, C. Van Ess-Dykema, K. Ries, E. Shriberg, D. Jurafsky, R. Martin, and M. Meteer. Dialogue act modeling for automatic tagging and recognition of conversational speech. Comput. Linguist., 26(3):339–373, Sept. 2000.

[<a name="8">8</a>] D. Traum. 20 questions for dialogue act taxonomies. Journal of Semantics, 17(1):7–30, 2000.

[<a name="8">8</a>] S. Vosoughi and D. Roy. A semi-automatic method for efficient detection of stories on social media. In Proc. of the 10th AAAI Conf. on Weblogs and Social Media., ICWSM 2016, pages 711–714, 2016

---

# Organizers
* Nicole Novielli, Dipartimento di Informatica, Università degli Studi di Bari Aldo Moro
* Pierpaolo Basile, Dipartimento di Informatica, Università degli Studi di Bari Aldo Moro


