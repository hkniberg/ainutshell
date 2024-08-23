# Prompt Engineering Techniques

OK let's dive into some specific prompt engineering techniques. I could write a whole book about this, but here I've just selected the most important techniques, things that I think will stay important even as the models improve and don't need as much babysitting.

## Iterating

Prompting is usually done iteratively. If you're doing something very simple you might get a great result from the first prompt, but as soon as you do something more complex you usually need a few rounds of iteration.

There are two basic approaches to iterating:

- Adding new prompts
- Editing previous prompts

### Adding new prompts

This is the most common approach for most people. Basically, if you aren't satisifed with your first result, add a new prompt to the chat thread providing more context, describing what you want, or why you weren't happy with the first result. Then keep doing that until you get what you want. So it becomes like a conversation where you are giving feedback to improve the result.

![](../.gitbook/assets/460-prompt-iterating-1.png)

Adding new prompts is a good default approach, since it is pretty simple and intuitive, and you also get a nice log of your entire chat history for this thread.

### Editing previous prompts

The other way is to edit a previous prompt, essentially creating a new branch in your conversation tree, and cutting away the old branch. This is kind of like pressing Undo, or saying "Hey ignore my previous prompt, let's pretend I wrote it like this instead".

![](../.gitbook/assets/460-prompt-iterating-2.png)

Both techniques are super useful. So how do you know when to use what?

### When to add, when to edit

The decision to add a new prompt or edit an old prompt is very situational.

The main guiding question is: **How useful is the current conversation history?**

For example, if the last response was not great, but it was at least somewhat in the right direction, then you can add a followup prompt. But if the last response was completely off, then you should probably edit the previous prompt instead. Otherwise the really bad response will stay in the chat history and essentially pollute the conversation, making the AI confused.

Let's say I'm using AI to help plan a team offsite. Here's my abbreviated chat history:

- Prompt 1: I'm planning a team offsite, and I want to do some cool original activity. Any suggestions? Give me a short list.
- Response 1: Escape Room, Rafting, VR team quest, Parkour workshop, Skydiving (.... and imagine more ideas here...)
- Prompt 2: **How about Skydiving?**
- Response 2: (.... Ai gives me skydiving info...)
- Prompt 3: OK, tell me more about... (skydiving questions)
- Response 3: (.... bla bla bla)

Let's say it suggests skydiving for my company offsite. I ask some followup questions about that, and then I conclude that we definitely don't want to do skydiving. I want to discuss other possible activities, and the skydiving discussion history isn't relevant anymore.

So in this case it is better to go back up and edit Prompt 2, essentially cleaning up and revising the chat history.

- Prompt 1: I'm planning a team offsite, and I want to do some cool original activity. Any suggestions? Give me a short list.
- Response 1: Escape Room, Rafting, VR team quest, Parkour workshop, Skydiving (.... and imagine more ideas here...)
- Prompt 2 (edited): **How about Escape room?**
- Response 2: (.... Ai gives me escape room info...)

If we continue the conversation from there, the AI model now has a clean conversation history without the tangent about Skydiving.

Let's say the AI gave us some useful info about escape rooms, and now I have followup questions. In that case it is better to add a followup prompt, since the previous response is still relevant, and we want to build on it.

- Prompt 1: I'm planning a company offsite, and I want to do some cool original activity. Any suggestions? Give me a short list.
- Response 1: Escape Room, Rafting, VR team quest, Parkour workshop, Skydiving (.... and imagine more ideas here...)
- Prompt 2: How about Escape room?
- Response 2: (.... Ai responds with lots of info about escape rooms)
- Prompt 3: **Tell me more about the third option. Would we be able to fit that into an afternoon?**

I'm surprised by how often people just accept the first response from an AI. Iterating makes a huge difference for the quality of the result.

## Self-reflection prompt

This is an interesting variant of the "Add prompt" technique. You basically ask the AI model to evaluate its own result. This is useful when:

- You suspect the model might be wrong, or might be hallucinating
- You want it to think more deeply about the problem
- You want more details

For example I tried this prompt:

> **Prompt **  
> How many ping-pong balls would fit in the Sydney Opera house?

In response I got a detailed analysis that took into account:

- The estimated volume of the Sydney Opera House (1.5 million cubic meters)
- The estimated volume of a ping-pong ball (3.35 × 10^-5 cubic meters)

The resulting estimate was about 44 billion balls.

Then I add a prompt, simply asking it to evaluate its own result:

> **Self-reflection prompt**
> Evaluate your result

It started questioning its own assumptions, and realized that you can't pack balls perfectly. So it added:

- The estimated packing efficiency of the balls (about 60-70%)

... and came up with an improved answer of 26 billion balls.

It was a very detailed analysis, and I got a very good answer.

But I suspected the model might be wrong, or hallucinating. So I tried this prompt:

> > **Prompt **  
> > Please check your analysis, and make sure it is correct.

## Mind the context window

The context window is the maximum amount of text that a model can accept as input. More expensive models have a larger context window. For example, at the time of writing GPT-4o has a context window of 128,000 tokens, which equates to about 90,000 words, which is about the size of a typical novel. May sound like a lot, but it can still run out!

Context is very important to keep in mind when working with AI. If you are writing code against an API, you will get an error message if you send more text than the model can handle. However, if you are using an app like Claude or ChatGPT, something more subtle happens when you exceed the context window.

When using an AI chat app, you build up a conversation history. Every time you write a prompt, the app will send the full chat history plus your new prompt to the model. That's how the model knows what you've been talking about so far.

If the chat history is rather short then there is nothing to worry about. Everything can fit in the context window, so the model will take your entire chat history into account when generating the response. That means you're likely to get a good result, since it won't "forget" anything (if you are using a good model).

![](../.gitbook/assets/460-short-chat-history.png)

But what if your chat history gets so long that it can't fit in the context window?

![](../.gitbook/assets/460-long-chat-history.png)

Something needs to give! The app will do something funky to get around the problem. Exactly what will depend on which app you are using, but some common approaches are:

- **Truncation** - the older messages are simply ignored. That means it will completely forget about them.
- **Summarization** - the app summarizes older messages in the background. That means it will remember roughly what you were talking about, but lose some details.

![](../.gitbook/assets/460-truncation-summarization.png)

There are other techniques as well, but regardless of that, **information will be lost** in one way or another..

What does this mean in practice?

It means you need to **pay attention to the length of your chat history**. Watch out for symptoms that look awefully a lot like human forgetfulness or alzheimer's. For example you're having a conversation about an upcoming event, and suddenly the AI doesn't remember exactly which date it was, because that piece of information was quite far back in the chat history.

So what can you do to deal with a long chat history? Some options:

- **Accept it**. Maybe the details of the older parts of the conversation aren't so important.
- **Start a new conversation thread**. For example maybe you've had a conversation about an upcoming workshop, explored a bunch of options for how to do it, and decided to go with one of them. Then you can start a new conversation about that, since the discussion about all the different options isn't relevant anymore.
- **Refresh the context**. For example ask it to summarize the most important parts of the conversation so far (_before_ it starts forgetting). That summary will now be "top of mind" for the continued conversation.
- **Repeat important information**. If you notice or worry that it will start forgetting things, you can repeat important information that you don't want it to forget. "Remember, the wedding is on Oct 12".
- **Go back to earlier parts of the conversation**. Many chat apps let you go back in your chat history and restart some part of it. So let's say you have a conversation about an important decision to make, and you explored the different options, and decided go with option 2. You can now scroll back up in the conversation history and edit one of your earlier prompts, before you got into the conversation about different options. That's like saying "Let's go back in time and pretend we didn't discuss these options, and I just went with option 2 immediately". By cutting off the brainstorm part you are effectively shortening the chat history, so it can fit better in the context window.

Dealing with context windows is a balancing ac. Your chat history often contains vital context for your continued conversation, but if it gets to long or messy then it can reduce the quality of your answers. The AI model basically gets confused by all the history.

Even if you haven't exceeded the context window, having a very long chat history can introduce so much noise that the AI model starts losing track of important details.

In summary: Whenever you are using an AI app that builds up a chat history, you need to mind the context window, and take steps to keep the chat history manageable.

Rule of thumb, if a chat starts degrading too much, just start a new conversation with a fresh context.

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

Use cheaper models sometimes. Example: email cleaner.
