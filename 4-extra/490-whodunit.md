# Whodunit - the AI powered mystery game

In this chapter I will share some insights from a hobby project - an AI powered mystery game.

## How it started

It started when I was sitting on the porch with my kids and some friends, and we tried using ChatGPT is a gamemaster for a role-playing game. We wanted to roleplay as a detective in a sherlock holmes-style mystery game.

We started with this prompt:

> **Prompt**  
> You are the game master or a sherlock holmes-style mystery game.
> You will make up setting for the mystery, and the characters involved.
> I will roleplay as the detective, interrogating the characters and trying to solve the mystery.
> You will roleplay as the characters.

It worked surprisingly well, and we had a lot of fun trying to unravel the mystery. You can it yourself, just copy the prompt above.

However after a few interrogations, the story started losing consistency. Originally the cause of death was poison, but then it somehow changed to a knife wound. And the more we played, the more inconsistencies started building up.

This makes sense if you know how Generative AI works. It has only a limited context window, so older messages in the chat will be forgotten. The AI model is essentially like a forgetful gamemaster who is just winging it and doesn't actually have a plan or a consistent storyline in mind, and doesn't remember what they said earlier in the game.

I was intrigued by the idea, though, and decided to try to build something in code instead. That way I could control the context, and make sure the AI gamemaster was roleplaying based on a consistent setting and storyline.

This project turned into a rather wild experiment in how far I could go with AI in game development. In fact, the game is entirely based on AI and would not be possible to build without it.

- AI wrote most of the code (with my guidance and feedback)
- AI generates all the content – mysteries, newspaper articles, crime scenes, characters, back-stories, plot twists, bulletin boards, images, loading texts, etc. With one button click you can ask it to generate a new mystery with a theme of your choice (or let GPT decide).
- AI roleplays all the characters in the game, and the crime scene search, and the police officer when you make your accusation, and the media writing articles about the crime and your investigation, and the epilogue describing the aftermath.
- AI even acts as a database administrator, and can answer questions about the number of players, the latest played mystery, etc.

You can try it at whodunit.kniberg.com.
