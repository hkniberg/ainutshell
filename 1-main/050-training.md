# Training

![](.gitbook/assets/050-training.png)

A large language model may have billions or even trillions of parameters. That’s why they are called Large!

So how are all these numbers set? Well, not through manual programming, that would impossible, but through training.

Just like babies learning to speak. A baby isn’t told how to speak, she doesn’t get an instruction manual. Instead, she listen to people speaking around her, and when she’s heard enough she starts seeing the pattern. She speaks a few words at first, to the delight of the parents, then and later on, full sentences.

Similarly, during a training period the language model is fed a mind boggling amount of text to learn from, mostly from Internet sources. It plays “guess the next word” with all of this, and the parameters are automatically tweaked over and over until it starts getting really good at predicting the next word. This is called back-progation. It is a fancy term for “Oh, I guessed wrong, I better change something”.

However to become become truly useful, a model also needs to undergo human training. This is called Reinforcement Learning with Human Feedback, and involves thousands of hours of humans painstakingly testing and evaluating output from the model and giving feedback. Kind of like training a dog with a clicker, to reinforce good behavior.

That’s why a model like GPT won’t tell you how to rob a bank. It knows very well how to rob a bank, but through human training it has learned that it shouldn’t help people commit crimes.

When training is done, the model is mostly frozen, other than some fine-tuning that can happen later. That’s what the P stands for in GPT – “pretrained”. Although in the future we will probably have models that can learn continuously rather than just during training and fine-tuning.
