# Prompt Engineering Techniques

## Iterating

## Reflection prompt

This is an interesting technique. You can ask the AI model to evaluate its own result.

## Elements of a good prompt

## Iterating

Prompting is usually done iteratively. If you're doing something very simple you might get a great result from the first prompt, ut as soon as you start doing something more complex you usually need a few rounds of iteration.

One way to do that is by simply adding a followup prompt to the chat thread.

![](../.gitbook/assets/140-prompt-iterating-1.png)

The other way is to edit a previous prompt, essentially creating a new branch in your conversation tree. This is kind of like pressing Undo, or saying "Hey ignore my previous prompt, let's say I wrote it like this instead".

![](../.gitbook/assets/140-prompt-iterating-2.png)

Both techniques are super useful. So how do you know when to use what?

The key question: **How useful is the current conversation history?**

For example, if the last response was not great, but it was at least somewhat in the right direction, then you can use a followup prompt. While if the last response was completely off, then you should probably edit the prompt instead. Otherwise the really bad response will stay in the chat history and essentially pollute the conversation, making the AI confused.

Example:

- Prompt 1: I'm planning a company offsite, and I want to do some cool original activity. Any suggestions? Give me a short list.
- Response 1: Escape Room, Rafting, VR team quest, Parkour workshop, Skydiving (.... and imagine more ideas here...)
- Prompt 2: Skydiving sounds interesting, tell me more about that.
- Response 2: (.... Ai responds with lots of info about skydiving)
- Prompt 3: OK, tell me more about... (skydiving questions)
- Response 3: (.... bla bla bla)

Let's say it suggests skydiving for my company offsite, and we have a conversation about how that might work. And then I conclude that we definitely don't want to do skydiving. I want to discuss other possible activities, and the skydiving discussion history isn't relevant anymore.

So in this case it is better to go back up and edit Prompt 2, essentially cleaning up the chat history.

- Prompt 1: I'm planning a company offsite, and I want to do some cool original activity. Any suggestions? Give me a short list.
- Response 1: Escape Room, Rafting, VR team quest, Parkour workshop, Skydiving (.... and imagine more ideas here...)
- Prompt 2: How about Escape room?
- Response 2: (.... Ai responds with lots of info about escape rooms)

If we continue the conversation from there, the AI model now has a clean conversation history without the tangent about Skydiving.

Let's say the AI gave us some useful info about escape rooms, and now I have followup questions. In that case it is better to add a followup prompt, since the previous response is still relevant, and we want to build on it.

- Prompt 1: I'm planning a company offsite, and I want to do some cool original activity. Any suggestions? Give me a short list.
- Response 1: Escape Room, Rafting, VR team quest, Parkour workshop, Skydiving (.... and imagine more ideas here...)
- Prompt 2: How about Escape room?
- Response 2: (.... Ai responds with lots of info about escape rooms)
- Prompt 3: Tell me more about the third option. Would we be able to fit that into an afternoon?

I'm surprised by how often people just accept the first response from an AI. Iterating makes a huge difference for the quality of the result.

## Is Prompt Engineering really important?

Some people argue that, as AI models get better, the need for good prompt engineering skills does down. I think this is partially true, but not entirely.

Gen AI models are to some extent trying to read your mind, trying to guess what you want. That's how they differ from programming languages. With programming languages you have to be very explicit. The compiler or interpreter will never guess what you want, if some information is missing it will simply fail. But if you tell a Gen AI model "write a cheerful goodnight story" it will make all kinds of guess and assumptions. It will guess what length you want, what genre, what characters, what you mean by cheerful, what the target audience is, what format and tone, etc.

In fact, this is one of the things that makes Gen AI models so powerful - that you don't have to write a complete, perfect specification. For example when using AI in programming, I sometimes write vague prompts like "Make this user interface look better" or "improve the code structure" and often get surprisingly useful results (if using a good model).

In the early days of Gen AI, people uncovered all kinds of prompting tricks and incantations that made the results measurably better.

For example "Take a deep breath and let's think step by step". This made models more likely to describe their thinking first before providing an answer. The answers tended to be much better, since it didn't just jump to the conclusion. There have even been academic papers written on specific prompt engineering tricks like this.

However over time the better models started doing many of these things automatically. Almost as if the engineers tuned the models to do this.

For example let's say I write:

> **Prompt **  
> How many ping-pong balls would fit in the Sydney Opera house?

Early AI models would respond immediately with a number, and if I asked again it would give a completely different number. It was almost as if it rolled a dice or something.

If I added "Think step by step", then it would give a longer answer

- Step 1: Estimate the Volume of the Sydney Opera House (...)
- Step 2: Estimate the Volume of a Ping-Pong Ball (...)
- Step 3: Divide the Volume of the Opera House by the Volume of a Ping-Pong Ball (...)

Then it would give a more consistent answer. And by thinking out loud, it also makes it easier for me to evaluate if it makes sense.

Now, however, I don't need to write "Think step by step". Even the cheaper models do this automatically.

For example with older models.

Same thing with

So which aspects of prompt engineering are important regardless of how good the models get? And which parts become less important?

I think these aspects are important regardless of how good the models get:

-

Yes, I think it is very important. The better you get at Prompt Engineering, the faster and better results you will get from AI. Whenever I get a bad or mediocre result from an AI, it almost always turns out to be because of a badly phrased prompt, or lack of context. When I fix the prompt, the results improve dramatically.

As the models get better, they also get better at guessing what you mean even when you write a vague or badly formulated prompt.

The most important element of a good prompt is a clear

Some aspects of Prompt Engineering are important regardless of how good the models get:

- Describing your expectations
- Providing necessary context

While some specific techniques and tricks become less important.

In fact, with good prompt engineering skills you can get a cheap AI model behave like an expensive one.
