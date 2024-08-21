import { config } from "dotenv";
import * as fs from "fs";
import { OpenAI } from "openai";
import { readPdfText } from "pdf-text-reader";

config({ path: ".env" });
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const prompt = `
You are a recruitment expert.
Below is the CV of a job candidate for the following job: {job}.
Evaluate the candidate. Write the main pros and cons, and a brief personal reflection.
Keep it short.
Here is the CV:
{cv}
`;

const jobFile = "circus-artist.txt";
const cvFile = "HenrikKniberg.pdf";

async function main() {
  const job = await readFile(jobFile);
  const cv = await readFile(cvFile);

  const fullPrompt = prompt.replace("{job}", job).replace("{cv}", cv);

  const result = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [{ role: "user", content: fullPrompt }],
  });
  const evaluation = result.choices[0].message.content;
  console.log(evaluation);
}

// Returns the content of a text or pdf file
async function readFile(filePath) {
  if (filePath.endsWith(".pdf")) {
    return await readPdfText({ url: "files/" + filePath });
  } else {
    return fs.readFileSync("files/" + filePath, "utf8");
  }
}

main();
