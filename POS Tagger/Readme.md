## About

In this assignment, we need to modify the Viterbi algorithm to solve the problem of unknown words using at __least two techniques__. Though there could be multiple ways to solve this problem, you may use the following hints:

* Which tag class do you think most unknown words belong to? Can you identify rules (e.g. based on morphological cues) that can be used to tag unknown words? You may define separate python functions to exploit these rules so that they work in tandem with the original Viterbi algorithm.
* Why does the Viterbi algorithm choose a random tag on encountering an unknown word? Can you modify the Viterbi algorithm so that it considers only one of the transition or emission probabilities for unknown words?