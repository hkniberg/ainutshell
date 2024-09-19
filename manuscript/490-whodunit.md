# Whodunit - the AI powered mystery game

In this chapter I will share some insights from a hobby project - an AI powered mystery game.

![](resources/490-board.png)

## How it started

It started as a fun little experiment. I was sitting on the porch with my cousin and my kids, goofing around with ChatGPT, trying to see if we could generate a role-playing game. We wrote a prompt like this:

> **Prompt**  
> You are the game master or a sherlock holmes-style mystery game.
> You will make up setting for the mystery, and the characters involved.
> I will roleplay as the detective, interrogating the characters and trying to solve the mystery.
> You will roleplay as the characters.

So GPT took the role gamemaster for a murder mystery game, and generated the setting, characters, etc. We played the role of a detective interrogating the suspects to figure out who the murderer is, and GPT roleplayed all the characters.

It worked surprisingly well! That is, until the chat history got too long and GPT started losing context and becoming inconsistent, and started changing the story on the fly. The AI model was essentially like a forgetful gamemaster who just wings it and doesn't actually have a plan or a consistent storyline in mind, and doesn't remember what they said earlier in the game. Pretty funny, but not great for a murder mystery where you need consistency.

I was intrigued by the idea, though, and decided to try to build something in code instead, using the OpenAI API instead of using ChatGPT directly. That way I could control the context, and make sure the AI gamemaster was roleplaying in a consistent way and sticking to the storyline. Development went insanely fast, because I pair-programmed with GPT all the time.

This project turned into a rather wild experiment in how far I could go with AI in game development. In fact, the game is entirely based on AI and would not be possible to build without it.

- AI wrote most of the code (with my guidance and feedback)
- AI generates all the content – mysteries, newspaper articles, crime scenes, characters, back-stories, plot twists, bulletin boards, images, loading texts, etc. With one button click you can ask it to generate a new mystery with a theme of your choice (or let GPT decide).
- AI roleplays all the characters in the game, and the crime scene search, and the police officer when you make your accusation, and the media writing articles about the crime and your investigation, and the epilogue describing the aftermath.
- AI even acts as a database administrator, and can answer questions about the number of players, the latest played mystery, etc.

You can try it at whodunit.kniberg.com.

## Playing the game

In the game you play the role of a detective trying to solve a crime. The first thing you do is decide which mystery to solve.

![](resources/490-select-mystery.png)

These are all auto-generated. You can create your own mysteries by pressing the “Generate new mystery” button at the top.

![](resources/490-mystery-generator.png)

You don’t need to type anything here, you can just press “Generate new mystery” and AI will make everything up. But if you want, you can describe a style or setting or theme, with as much or little detail as you like. Some examples are provided, and they are also auto-generated.

Your mysteries are private by default – only you can see it, and those who you share the link with. You can press “publish” to make your visible to everyone.

After selecting (or generating) a mystery, you get to the overview page.

![](resources/490-board.png)

![](resources/490-mystery-intro.png)

Press “Start Mystery” to get started!

To the left you see a list of all suspects and the crime scene. Click on a suspect to interrogate him/her, click on the crime scene to search. Each interrogation & search is a chat session for you play the role of the detective and GPT plays the role of the character being interrogated or the crime scene being searched.

![](resources/490-interrogate.png)

![](resources/490-crime-scene.png)

So search the crime scene, interrogate the suspects, and ask typical detective-story questions like where they were at the scene of the crime, about their relationship with other characters, etc.

When you think you know who committed the crime, press “Accuse”. Now your job is to present your case to the police in a convincing way. The police won’t accept flimsy accusations, you need to present a pretty good case for why you think character X is the culprit. There could also be multiple culprits!

![](resources/490-accusation-rejected.png)

If the police reject your accusation you need to rephrase it to make your case stronge, or go do some more interrogating.

![](resources/490-accusation-accepted.png)

An important thing here is that convincing the police doesn’t mean you were right! You might have convincingly accused the wrong person! Click “Go to the ending page” to find out.

The ending page includes newspaper article about the arrest, an evaluate of your result (Failure, Success, or Partial Success), and an epilogue describing the aftermath. In this case we arrested an innocent person, ouch!

![](resources/490-epilogue-failure.png)

You can also end up with a Partial Success, where you catch some of the culprits but not all.

![](resources/490-partial-success.png)

## Administrating the game

Normally with a product like this I would also build an adminstration backend to be able to see basic statistics like number of players, number of mysteries solved, etc.

But in the spirit of going all-in with AI, I just built an admin chat instead.

![](resources/490-admin-chat.png)

So I could ask questions like "how many mysteries have been played", "how many people have solved this mystery", etc. AI turns this into database queries, interprets the results, and explains it to me. In the example below you can see the database queires it was executing for me.

![](resources/490-admin-chat-2.png)

I think this is an interesting use case in general - using an AI chat as a general purpose tool for adminstration and analytics, or using AI chat as a user-friendly proxy for interacting with backend systems that are otherwise quite complicated.

## How the game was made

(note - this section is slightly technical)

The first playable version of the game took only 3 days to make. I used a tech stack that I had never used before (React + Next.js + Vercel), but thanks to GPT that was no problem. I learned it on the fly. This would have taken weeks to do without AI assistances, so this made me 5-10 times faster than usual.

Once I got the core gameplay loop working I spent another another couple of weeks spread out of the summer, tweaking and improving the game.

Here are some examples of how I used AI assistance:

- **Architecture discussion.** “I want to do X, which tools & tech are suitable for that?”. GPT helped me select React + Next.js + Vercel + MongoDB as tech stack, and it was a great choice for this.
- ** Design discussions.** “What is the best way to do X?”
- **Adding features**. “Here is some code (…), please add feature X.”
- **Fixing bugs.** “Here is some code, an error message, and a stack trace. Fix it. “
- **Explaining things.** “How does document serialization work in MongoDB?” or “How do api routes work in Next.js?”
- **Improving the UI.** “This page is ugly and confusing. Improve it.”
- **Fixing performance issues.** “This page loads really slowly. Speed it up”. GPT helped me figure out were it makes sense to use client-side rendering vs server-side rendering for example.
- **Adding functions.** “Write a function that does XYZ” (although copilot could often do that too, if I just start writing a comment or function name).
- **Code cleanup.** “This code is messy and full of duplication. Refactor it.” For example in several cases my react page started getting too big, so I asked GPT to extract reusable components from it.

I used GPT4, which might be considered a dinosaur by the time you read this. But it was surprisingly good!

As long as I provided a clear context (for example existing code), and a clear goal or problem statement, it nailed it almost every time. When it failed or created bugs, it was either because my instructions were unclear, or because we were dealing with code or APIs that had changed after GPT4’s training date.

A lot of my work was prompt engineering – writing and tuning prompts to generate the right content. The game is quite special because we use one prompt to generate the mystery, and then the output of that is a “dm info” that is used as input to the AI that roleplays all characters and runs the mystery.

This is like a team of AIs prompting each other, which requires especially well-crafted prompts.

We can compare it to a traditional D&D roleplaying campaign. One AI is “campaign creator” and creates a campaign booklet describing the world, all characters with motives, personalities, etc, and of course the goal of the campaign. And then another AI is “dungeon master” and uses the campaign booklet when talking to the players and role-playing all characters. And then there are separate AIs to generate images and newspaper articles and bulletin boards and other content on the fly.

Here’s a crude attempt to illustrate this…

![](resources/490-prompt-graph.png)

## Prompts used

In this section I will share some of the prompts used inside the game.
I used all of the techniques described in the [Prompt Engineering Techniques chapter](460-prompt-engineering-techniques.md).
