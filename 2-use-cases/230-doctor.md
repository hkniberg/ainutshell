# Use case: AI Doctor

Most model providers say that you shouldn't use their models to provide medical advice. This is likely because:

- The models can hallucinate, especially the cheaper models
- If the user isn't good at prompt engineering, they may get the wrong advice
- The model providers don't want to risk getting sued if something goes wrong

Despite this, my experience is that the best AI models are capable of producing useful and safe medical advice.
This is supported by studies such as [GPT versus Resident Physicians — A Benchmark Based on Official Board Scores](https://ai.nejm.org/doi/full/10.1056/AIdbp2300192).

Quoting the paper (highlights are mine):

> GPT-4 ranked higher than the majority of physicians in psychiatry, with a median percentile of 74.7% (95% confidence interval [CI] for the percentile, 66.2 to 81.0), and it performed similarly to the median physician in general surgery and internal medicine, displaying median percentiles of 44.4% (95% CI, 38.9 to 55.5) and 56.6% (95% CI, 44.0 to 65.7), respectively. GPT-4 performance was lower in pediatrics and OB/GYN but remained **higher than a considerable fraction of practicing physicians**, with a median score of 17.4% (95% CI, 9.55 to 30.9) and a median score of 23.44% (95% CI, 14.84 to 44.5), respectively. GPT-3.5 did not pass the examination in any discipline and was inferior to the majority of physicians in the five disciplines. Overall, **GPT-4 passed the board residency examination in four of five specialties, revealing a median score higher than the official passing score of 65%.**

I have a personal story to share here. In early 2024 I did a health checkup and got a scary result: something was badly wrong with my kidneys. I went through a series of tests over the next few months, and the results confirmed the problem but also showed another problem: high blood pressure (hypertension), which was likely related. I met several kidney experts along the way, who looked at the data and tried to diagnose the problem. During this process, I gathered all the raw data from the lab tests, and dumped it all into Claude 3.5 Sonnet, unfiltered. Then I wrote this prompt:

> **Prompt**  
> Evaluate this medical data, explain what's wrong with me, and explain what I should do about it.

This was pretty simple prompt, but I included A LOT of context, dozens of pages of lab data.

The response was a very detailed analysis and diagnosis, and concrete advice. And to my surprise it matched exactly what the kidney experts said! This was a jaw-dropping moment for me.

The model had "proven" that it knew what it was talking about, so I felt comfortable asking it a lot of followup questions. My access to the kidney experts was limited, but the AI model had infinite time and patience to talk to me, so I could ask it all the stupid questions I wanted. I double-checked some answers via Google, but never saw any sign of hallucination. Hallucination tends to happen when you use a cheap model and don't provide enough context. In this case I used a good model and provided a ton of context.

When I met the kidney experts again, I was better equipped to discuss with them, since I had a deeper understanding of the problem. The AI doctor and human doctor both agreed that the immediate remedy was blood pressure meds. Using that my blood pressure came down to normal levels, and my kidney values improved. The disease is chronic, but the worst of it is over and I'm no longer in immediate danger. Whew.

## So should you use AI as your doctor?

Yes and no. I still think a human expert should be in the loop, I don't recommend replacing the human doctor with an AI doctor. If nothing else, the human doctor has eyes, nose, ears, arms, and legs - useful tools which the AI doctor lacks. The human doctor can take tests, the AI doctor cannot (well, who knows, maybe it can by the time you read this). Plus the human connection is nice.

However, an AI doctor can _complement_ a human doctor by giving you a second opinion and providing more information. Also, an AI doctor will never be in a hurry, or impatient, or stressed, or in a bad mood, or suffer from lack of sleep. And, the fact that it lacks eyes makes it less likely to discriminate based on gender/race/age/clothing/etc.

But what if you don't have access to a human specialist? What if you can't afford it, or have a very rare condition which your doctor doesn't understand?

In that case, an AI doctor can be a life saver! With a good AI model and decent prompt engineering skills, an AI doctor will always be better than no doctor at all, or the opinions of your well-intended (but uninformed) friends and family.

In general, I find it fascinating that it is possible to create a skilled AI doctor using just a simple prompt and a generalist app like Claude or ChatGPT. Good prompt engineering skills pretty much give you superpowers.

Just keep in mind: If you do this, make sure you use a good model! The free or cheaper models are more likely to hallucinate or give you incorrect advice, which can be dangerous. Quoting the benchmark:

> GPT-3.5 did not pass the examination in any discipline and was inferior to the majority of physicians in the five disciplines

Also keep in mind: Human doctors can hallucinate too. We just call it something else: human error...
