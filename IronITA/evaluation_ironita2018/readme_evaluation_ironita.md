Evaluation script and gold standard of the IRONITA 2018 sthared task at EVALITA

Content of the archive:
- README.txt: this file
- evaluation_ironita.py: evaluation script
- baseline_random_ironita2018.tsv: result of the random baseline
- baseline_zero_ironita2018.tsv: result of the most frequent class baseline
- test_gold_ironita2018.tsv: annotated (gold standard) test set

To run the evaluation script:
$ python evaluation_ironita.py RESULT_FILE GOLD_STANDARD
 
For instance, to evaluate the results of the random baseline:

$ python evaluation_ironita.py baseline_random_ironita2018.tsv test_gold_ironita2018.tsv
Task A, precision (non ironic):  0.505773672055
Task A, recall (non ironic):  0.50114416476
Task A, F1-score (non ironic):  0.503448275862
Task A, precision (ironic):  0.503416856492
Task A, recall (ironic):  0.508045977011
Task A, F1-score (ironic):  0.505720823799
Task A, average F1-score:  0.50458454983
Task B, precision (non ironic):  0.505773672055
Task B, recall (non ironic):  0.50114416476
Task B, F1-score (non ironic):  0.503448275862
Task B, precision (ironic):  0.267281105991
Task B, recall (ironic):  0.264840182648
Task B, F1-score (ironic):  0.266055045872
Task B, precision (sarcastic):  0.267281105991
Task B, recall (sarcastic):  0.264840182648
Task B, F1-score (sarcastic):  0.266055045872
Task B, average F1-score:  0.337170818051


