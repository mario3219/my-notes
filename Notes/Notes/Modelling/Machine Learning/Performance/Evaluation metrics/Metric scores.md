Different scores are more important depending on the goal of the model, for example if false positives are more damaging than false negatives.

<u>Sensitivity</u>
Missing a positive is bad
$\frac{TP}{TP+FN}$

<u>Specificity</u>
False positives are costly
$\frac{TN}{TN+TP}$

<u>Precision</u>
Care about trust in positive labels
$\frac{TP}{TP+FP}$

<u>FPR</u>
How often a false alarm happens
$\frac{FP}{FP+TN}$

<u>Accuracy</u>
How often am I correct
$\frac{TP+TN}{TP+TN+FP+FN}$

<u>F1 Score</u>
How good is my model overall
$\frac{2\cdot TP}{2\cdot TP +FP+FN}$

