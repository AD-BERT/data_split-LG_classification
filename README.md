<<<<<<< HEAD
## Data info

Statistics of what's in the pubmed abstract:

- AD: 2692

- eczema non-AD: 6001

- dermatitis non-AD: 515

- other non-AD: 3474

*<<without repetition>>*

- **AD**: 2691

- **eczema non-AD**: 6001

- dermatitis non-AD: 514

- other non-AD: 3472

*class definition:*

- AD: 'atopic dermatitis' in text

- eczema non-AD: 'atopic dermatitis' NOT in text, and ' eczema ' in text

- dermatitis non-AD: 'atopic dermatitis' NOT in text and ' eczema ' NOT in text, and ' dermatitis ' in text

- other non-AD: text not having 'atopic dermatitis', ' eczema ', or ' dermatitis '.

## Data processing

'''python3 src/data_process.py'''

This will randomly split the 2691 **AD** abstracts into Train-Dev-Test with the amount of 2091-300-300, and randomly pick the same amount of **eczema non-AD** abstracts and did the train-dev-test split in the same way.

The preprocessed data will be stored in '''AD_nonAD/''', which can be used to train and tune the classification model.

## Classification

'''python3 src/lg_classify.py'''

This will train a **logistic regression classifier** with **tf-idf features** on the data by the data processing step.

After masking the keywords we used to prepare the classification data, the classifier achieves an average accuracy is around 80\%.



=======
# Experiments on PubMed Abstracts

1. Split the pubmed abstracts found by the key word: eczema from pubmed central, into abstracts containing the term Atopic Dermatitis (AD).
2. Train a binary classifier that can classify AD and non-AD abstracts. As a pre-processing steps the terms eczema and atopic dermatitis is removed.
  This is to avoid trivial classification.
>>>>>>> 9c76b23294184eb91c7170c7b3dc570b24656650
