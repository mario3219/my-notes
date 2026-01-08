**Speed up training**
Using for example wikipedia:
3 000 000 words, 100 word dimensions

**Negative sampling**
All but one input is zero, do not need to multiply weights to input zero, which saves calculation time, and also do not need to predict all words from every word.
