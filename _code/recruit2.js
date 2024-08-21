import { config } from "dotenv";
import * as fs from "fs";
import { OpenAI } from "openai";
import * as path from "path";
import { readPdfText } from "pdf-text-reader";

config();
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const systemMessage = "You are a recruitment expert with sarcastic tendencies";

const candidateEvaluationPrompt = `
Below is the CV of a job candidate for the following job: {job}.

Evaluate the candidate. Write the main pros and cons, and your personal reflection.
Write the result in markdown format.
Here is the CV:
{cv}
`;

const finalRecommendationPrompt = `
Below is an evaluation of job candidates for the following job: {job}.

Based on this information, who seems most suitable for this job?
---
{candidateEvaluations}
---
Give a short answer in markdown format, about one paragraph. Be specific about who the best candidate is, and why.
If they are all bad for the job, who is the least bad?
`;

const jobDescriptionFile = "jobs/baker.txt";
const candidatesDir = "candidates";
const outputDir = "evaluations";

async function evaluateCandidate(job, candidateFileName) {
  console.log(`Evaluating ${candidateFileName}...`);

  const cv = await readFile(path.join(candidatesDir, candidateFileName));
  const fullPrompt = candidateEvaluationPrompt
    .replace("{job}", job)
    .replace("{cv}", cv);

  const result = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
      { role: "system", content: systemMessage },
      { role: "user", content: fullPrompt },
    ],
  });

  const evaluationText = result.choices[0].message.content;
  console.log(`...got result for ${candidateFileName}`);

  await saveCandidateEvaluation(candidateFileName, evaluationText);
  return evaluationText;
}

async function generateFinalRecommendation(job, evaluations) {
  const fullPrompt = finalRecommendationPrompt
    .replace("{job}", job)
    .replace("{candidateEvaluations}", evaluations.join("\n\n"));

  console.log("Generating final recommendation..");
  const result = await openai.chat.completions.create({
    model: "gpt-4-1106-preview",
    messages: [
      { role: "system", content: systemMessage },
      { role: "user", content: fullPrompt },
    ],
  });
  return result.choices[0].message.content;
}

async function main() {
  const job = await readFile(jobDescriptionFile);
  const candidateFileNames = fs.readdirSync(candidatesDir);
  const evaluations = await Promise.all(
    candidateFileNames.map((candidateFileName) =>
      evaluateCandidate(job, candidateFileName)
    )
  );
  let finalRecommendation = await generateFinalRecommendation(job, evaluations);
  saveFinalRecommendation(finalRecommendation);
  console.log(finalRecommendation);
}

async function readFile(fileName) {
  if (fileName.endsWith(".pdf")) {
    return await readPdfText({ url: fileName });
  } else {
    return fs.readFileSync(fileName, "utf8");
  }
}

async function saveCandidateEvaluation(candidateFileName, evaluationText) {
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir);
  }
  const evaluationFile = path.join(
    outputDir,
    candidateFileName.replace(/\..+$/, "") + "-evaluation.md"
  );
  fs.writeFileSync(evaluationFile, evaluationText);
}

function saveFinalRecommendation(finalRecommendation) {
  const recommendationFile = path.join(outputDir, "recommendation.md");
  fs.writeFileSync(recommendationFile, finalRecommendation);
}

main();
