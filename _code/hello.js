import { config } from "dotenv";
import { OpenAI } from "openai";
config(); // load OpenAI key from .env file
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const result = await openai.chat.completions.create({
  model: "gpt-4",
  messages: [
    {
      role: "user",
      content: "Hey GPT, give me a really bad dad joke.",
    },
  ],
});
console.log(result);
