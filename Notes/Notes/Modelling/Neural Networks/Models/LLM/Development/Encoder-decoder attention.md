
![[Pasted image 20260108235033.png]]

Encoder (left) and decoder (right)
At the output of encoder, you get contextual vectors, which are passed to the decoder as memory. The decoder looks similar, just with an extra attention block. Shifted right means that the block doesn't see the token it is predicting.

**How GPT does it**
- All previous tokens attend to each other
- Representations are updated through many layers
- A probability distribution over the next token is produced
- One token is selected
- That token becomes part of the context for the next step
No encoder, only decoder.

**How it gets trained to answer in a certain format**
The model through probability gets trained to form different formats, from queries from users, which nudges weights in favouring those answer formats.