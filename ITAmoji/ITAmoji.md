# ITAmoji - Italian Emoji Prediction @EVALITA 2018

Considered the widespread diffusion of emojis as visual devices useful to provide an additional layer of meaning to Social Media messages, on one hand, and the unquestionable role of Twitter as one of the most important Social Media platforms, on the other, we propose the Italian Emoji Prediction task (ITAmoji Task).

We invite participants to submit systems designed to predict, given a ​tweet in Italian​, its most likely associated emoji​. We will challenge systems to predict emojis among a wide and heterogeneous emoji space. As for the experimental setting, for simplicity purposes, we will consider tweets including only one emoji. After removing the emoji from the tweet, we will ask users to predict it.


# Fair Use Policy 

Please, cite the following paper if you intend to use our dataset for your own research:
>  Francesco Ronzano, Francesco Barbieri, Endang Wahyu Pamungkas, Viviana Patti, Francesca Chiusaroli (2018) [Overview of the EVALITA 2018 Italian Emoji Prediction (ITAMoji) Task](http://ceur-ws.org/Vol-2263/paper004.pdf) Proceedings of 6th Evaluation Campaign of Natural Language Processing and Speech Tools for Ital- ian. Final Workshop (EVALITA 2018), Turin, Italy. CEUR.org.



# The relevance of emojis in Social Media communication

During the last decade the use of emoji has increasingly pervaded Social Media platforms by providing users with a rich set of pictograms useful to visually complement and enrich the expressiveness of short text messages. Nowadays this novel, visual way of communication represents a de-facto standard in a wide range of Social Media platforms including fully-fledged portals for user-generated contents like Twitter, Facebook and Instagram as well as instant-messaging services like WhatsApp. As a consequence, the possibility to effectively interpret and model the semantics of emojis has become an essential task to deal with when we analyze Social Media contents.

Even if over the last few years the study of this new form of language has been focusing a growing attention, at present the body of investigations that deal with emojis is still scarce, especially when we consider their characterization from a Natural Language Processing (NLP) standpoint. While there are notable exceptions which study the semantics of emojis and their usage [1-8], or their sentiment [9], the interplay between text-based messages and emojis remains still explored only by a small number of studies. Among these investigations there is the analysis of emoji predictability by Barbieri et al. in 2017 [10]: they proposed a neural model to predict the most likely emoji to appear in a text message (tweet). The task resulted to be hard, as emojis encode multiple meanings [2]. Related to this, in the context of the International Workshop on Semantic Evaluation (SemEVAL 2018), the Multilingual Emoji Prediction Task [12] has been organized in order to challenge the research community to automatically model the semantics of emojis occurring in English and Spanish Twitter messages. The results of this tasks will be presented on June 2018 in the context of 16th Annual Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT 2018).

In general, exciting and highly relevant avenues for research are still to explore with respect to emoji understanding, since emojis represent often an essential of Social Media texts and thus ignoring or misinterpreting them may lead to misunderstandings in comprehending the intended meaning of a message [11]. The ambiguity of emojis raises an interesting question in human-computer interaction: how can we teach an artificial agent to correctly interpret and recognise emojis' use in spontaneous conversation? The main motivation behind this question is that an AI system able to predict emojis could contribute notably to better natural language understanding [9] and thus to different natural language processing tasks such as generating emoji-enriched social media content, enhancing emotion/sentiment analysis systems, and improving retrieval of social network material, and ultimately improving user profiling.


[1] Aoki, Sho, and Osamu Uchida. "A method for automatically generating the emotional vectors of emoticons using weblog articles." Proc. 10th WSEAS Int. Conf. on Applied Computer and Applied Computational Science, Stevens Point, Wisconsin, USA. 2011.

[2] Barbieri, Francesco, Francesco Ronzano, and Horacio Saggion. "What does this Emoji Mean? A Vector Space Skip-Gram Model for Twitter Emojis." LREC. 2016.

[3] Barbieri, Francesco, et al. "How cosmopolitan are emojis?: Exploring emojis usage and meaning over different languages with distributional semantics." Proceedings of the 2016 ACM on Multimedia Conference. ACM, 2016.

[4] Barbieri, Francesco, et al. "Overview of the evalita 2016 sentiment polarity classification task." Proceedings of Third Italian Conference on Computational Linguistics (CLiC-it 2016) & Fifth Evaluation Campaign of Natural Language Processing and Speech Tools for Italian. Final Workshop (EVALITA 2016). 2016.

[5] Eisner, Ben, et al. "emoji2vec: Learning emoji representations from their description." arXiv preprint arXiv:1609.08359 (2016).

[6] Ljubešić, Nikola, and Darja Fišer. "A global analysis of emoji usage." Proceedings of the 10th Web as Corpus Workshop. 2016.

[7] Chiusaroli, Francesca. "La scrittura in emoji tra dizionario e traduzione." CLiC it (2015): 88.

[8] Monti, Johanna, et al. "New online Tools and Digital Environments for Translation into Emoji." Third Italian Conference on Computational Linguistics (CLiC-it 2016). Accademia University Press, 2016.

[9] Novak, Petra Kralj, et al. "Sentiment of emojis." PloS one 10.12 (2015): e0144296.

[10] Barbieri, Francesco, Miguel Ballesteros, and Horacio Saggion. "Are Emojis Predictable?." arXiv preprint arXiv:1702.07285(2017).

[11] Miller, Hannah, et al. "Blissfully happy” or “ready to fight”: Varying Interpretations of Emoji." Proceedings of ICWSM 2016 (2016).

[12] Barbieri, Francesco and Camacho-Collados, Jose and Ronzano, Francesco and Espinosa-Anke, Luis and Ballesteros, Miguel and Basile, Valerio and Patti, Viviana and Saggion, Horacio. "SemEval-2018 Task 2: Multilingual Emoji Prediction" To be published in the Proceedings of the 12th International Workshop on Semantic Evaluation (SemEval-2018), NAACL 2018
