Neural networks that apply the transformer architecture. Works on sequences. Instead of using a sliding window like in CNN's, instead partitions images into smaller windows and then inserts the windows in an array. Each element gets a position embedding, and the model trains to understand global relationships.

Meaning, smaller regions of the image can influence interpretation of a distant one.