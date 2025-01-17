# Generative AI in a Nutshell - how to survive and thrive in the Age of AI

This is the source code for the book Generative AI in a Nutshell.

This repository is public to enable community-submitted improvements to the AI-translated versions. See below for more details.

## Where to buy the book

The book is distributed on LeanPub (ebook) and Amazon (kindle, paperback, hardcover).

- https://leanpub.com/ainutshell
- https://www.amazon.com/dp/B0DSBFN12W

Technically you access the book content here for free, but I prefer if you buy it. You'll get a nicely formatted book (rather than raw markdown files), and you'll support my work.

## How to help improve a translation

The original version of the book is in English. We have made AI translations to 31 languages. AI translations are usually decent, but they are far from perfect, so some human help is appreciated.

So if you have time to read the book in your language and make the necessary language improvements, that would be great.

Here's how to do it (I'll probably provide a more detailed version of this later):

1. Create a GitHub account (if you don't have one already)
2. Open the branch for the language you want to improve: `preview-xx` (where `xx` is the language code, e.g. `ja` for Japanese)
3. Edit the file `manuscript/manuscript.md`. It uses Markua, which is a Markdown based format. You probably don't need to know the Markua syntax, but you can read more about it here: https://markua.com/
4. Also edit the file `manuscript/metadata.md` which contains the title, subtitle, and back cover text.
5. Commit the changes.
6. When you are finished reviewing and improving the translation, submit a Pull Request back to the `preview-xx` branch.
7. Me and Egbert (my AI sidekick) will review it, and if it seems OK we'll publish it to LeanPub, and the ebook version will be updated.
8. After some time, the Amazon version will be updated as well (that is a manual process done by LeanPub once roughly once per quarter).

## Translation improvement guidelines

- Don't fix what isn't broken. Only change sentences where the translation is incorrect, or if there is a more suitable way to phrase the sentence. Don't rewrite the whole book unless the AI translation was really horrible.
- Keep to the original style, tone, and meaning of the sentences. If something is unclear, look at the english version for reference. The english version is on the branch called `publish`.
- Don't add or remove any content. If you can't figure out how to phrase something correctly, leave the not-to-good phrasing (or leave it in English) rather than removing the sentence.
- Make a judgement call for which terminology should be translated, and which should be left in English. For example terms like "Prompt Engineering" or "Reinforcement Learning".
- Don't use AI to translate! The whole point of this is to get human translation to complement the existing AI translations. But you could use AI to bounce ideas.
- If a sentence or paragraph is hard to direct-translate, feel free to replace it with a different phrasing that makes sense in the target language. You can take some liberties here, as long as you stick to the overall intent of the paragraph (and my informal writing style).
- Some images in the book contain text. Those are not translated by default, and I don't expect you to translate them, since it involve some finicky image editing work. But if you do, that is really awesome! The images are in the manuscript/resources folder.

## Questions / support

If you need support or have a question, feel free to submit an issue on this repository, or email to ainutshell@ymnig.ai.

## Translation improvement status

![](https://img.shields.io/badge/todo-red) = the book still has the original AI translation, and human improvements are probably needed.
![](https://img.shields.io/badge/complete-green) = a human-improved translation has been done, so we probably don't need to do anything more.

![](https://img.shields.io/badge/todo-red) Arabic
![](https://img.shields.io/badge/todo-red) Bosnian
![](https://img.shields.io/badge/todo-red) Chinese (Simplified)
![](https://img.shields.io/badge/todo-red) Chinese (Traditional)
![](https://img.shields.io/badge/todo-red) Croatian
![](https://img.shields.io/badge/todo-red) Czech
![](https://img.shields.io/badge/todo-red) Danish
![](https://img.shields.io/badge/todo-red) Dutch
![](https://img.shields.io/badge/todo-red) French
![](https://img.shields.io/badge/todo-red) German
![](https://img.shields.io/badge/todo-red) Greek
![](https://img.shields.io/badge/todo-red) Hebrew
![](https://img.shields.io/badge/todo-red) Hindi
![](https://img.shields.io/badge/todo-red) Hungarian
![](https://img.shields.io/badge/todo-red) Indonesian
![](https://img.shields.io/badge/todo-red) Italian
![](https://img.shields.io/badge/todo-red) Japanese
![](https://img.shields.io/badge/todo-red) Korean
![](https://img.shields.io/badge/todo-red) Norwegian (Bokmål)
![](https://img.shields.io/badge/todo-red) Polish
![](https://img.shields.io/badge/todo-red) Portuguese (Brazilian)
![](https://img.shields.io/badge/todo-red) Portuguese (European)
![](https://img.shields.io/badge/todo-red) Punjabi
![](https://img.shields.io/badge/todo-red) Romanian
![](https://img.shields.io/badge/todo-red) Serbian (Cyrillic)
![](https://img.shields.io/badge/todo-red) Spanish
![](https://img.shields.io/badge/todo-red) Swedish
![](https://img.shields.io/badge/todo-red) Thai
![](https://img.shields.io/badge/todo-red) Turkish
![](https://img.shields.io/badge/todo-red) Ukrainian
![](https://img.shields.io/badge/todo-red) Vietnamese
