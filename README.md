# Decision-tree-from-scratch
I build decision tree classifier for multi-class classification with continuous feature values from scratch (i.e. without any advanced libraries such as Numpy, Scikit-learn, Pandas, etc.)

## Tree specifications
- use binary split and a threshold to split data
``` 
if attribute X <= threshold theta:
  -> left node
else
  -> right node
```
- use information gain to construct the decision tree
- always choose the attribute or label with the smallest value (i.e. if splitting on either attribute X1 or X2 gives the best information gain, choose the smaller of X1 and X2)

## Dataset specifications
- each attribute is named by a non-negative integer
- each line in dataset has the following space-separated format:
```
[label] [attribute 1]:[value 1] [attribute 2]:[value 2]...
```
