# Prompt engineering

In order to use Generative AI effectively, you need to get good at Prompt Engineering.

Prompt Engineering is art of crafting effective prompts that produce useful results from an AI model. I think Prompt Design would be a better term, but Prompt Engineering seems to have stuck so we'll go with that.

This skill is crucially important, whether you are using an AI product like ChatGPT or building your own AI product.

# Example - from bad to good prompt

Here’s an example. Let’s say I want help planning a workshop.

> **Prompt 1**  
> Give me an agenda for a workshop

This prompt is unlikely to give useful results. No matter how smart the AI is, if it doesn’t know the context of my workshop, it can only give vague, high level recommendations.

Let's improve it.

> **Prompt 2**  
> Give me an agenda for a workshop.  
> I'm meeting a leadership team at an aurospace consulting firm. The goal of the workshop is figure out how they can use AI. They are new to this. We have 8 people for 4 hours.

This second prompt is better. Now I provided a context. This is normally done iteratively. Write a prompt, look at the result, add a followup prompt to provide more information, or edit the original prompt. Rinse and repeat until you get a good result.

Here's another approach.

> **Prompt 3**
> Give me an agenda for a workshop.  
> Feel free to ask me any clarifying questions first.

Instead of me providing a bunch of context upfront, I'm asking it to interview me to get the context it needs, and then propose a workshop agenda after. So the AI is iterating over the conversation instead of me.

This tends to give more interesting and useful results, but can take a bit longer.

I often combine these techniques. I provide a bit of context, and then tell it to ask me if it needs any more info.

## The biggest limitation is you

The biggest limitation is not the AI model, but the quality of your prompts - and hence your prompt engineering skill. I keep seeing this. Whenever I get a bad or mediocre result from an AI, it almost always turns out to be because of a badly phrased prompt, or lack of context. When I fix the prompt, the results improve dramatically.

I've experienced situations where I'm sitting next a colleague, both of us are working on similar things and using AI assistance, and he keeps getting mediocre results while I keep getting really good results. At first glance you'd think that I was using a better model, but in fact I was just more experienced with prompt engineering, and better at providing a clear prompt with the right context.

## How to learn Prompt Engineering

There are plenty of courses, books, videos, and articles to help you learn this.

This book also contains a chapter called [Prompt Engineering Techniques](../4-extra/460-prompt-engineering-techniques.md), with more specific tips and examples.

But the most important thing is to practice, and learn by doing. Try using AI for all kinds of things, even silly things, or things that AI isn't good at. By toying around and testing the limits you will build your skills.

A nice side effect is that you will become better at communicating in general, since Prompt Engineering is really all about clarity and effective communication.

![](../.gitbook/assets/140-people-talking.png)
