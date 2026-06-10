# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

This system covers technology careers, including software engineering, data science, AI engineering, cloud engineering, cybersecurity, DevOps, UX design, product management, and machine learning. It is useful because users can quickly ask questions and compare different technology careers without searching through multiple articles. The system retrieves information from a collection of career guides and provides grounded answers with sources, making it easier to find relevant information about skills, responsibilities, and career paths in one place.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | software_engineering.txt  | Information about software engineering responsibilities, skills, salary, and job outlook.              | https://www.coursera.org/articles/software-engineer 
| 2 | data_science.txt          | Information about data science careers, skills, tools, and job growth.                                 | https://www.coursera.org/articles/what-is-a-data-scientist
| 3 | machine_learning.txt      | Overview of machine learning engineering roles, responsibilities, and required skills.                 | https://www.ibm.com/think/topics/machine-learning 
| 4 | cybersecurity.txt         | Information about cybersecurity careers, certifications, and security responsibilities.                | https://www.ibm.com/think/topics/cybersecurity 
| 5 | cloud_engineering.txt     | Information about cloud engineering, cloud platforms, certifications, and career paths.                | https://www.coursera.org/articles/what-is-a-cloud-engineer 
| 6 | ai_engineer.txt           | Information about artificial intelligence engineering roles, skills, and technologies.                 | https://www.coursera.org/articles/ai-engineer 
| 7 | devops.txt                | Information about DevOps practices, automation, CI/CD, and infrastructure management.                  | https://learn.microsoft.com/en-us/training/career-paths/devops-engineer 
| 8 | ux_design.txt             | Information about UX design responsibilities, user research, and design processes.                     | https://grow.google/intl/en_in/ux-design-course/?srsltid=AfmBOopk09Z4OCfJcUZ5aJYaRXDN6PPYxXBGN9-2WmAR1FcwFqvse_8j 
| 9 | product_management.txt    | Information about product management responsibilities, skills, and career growth.                      | https://www.ibm.com/think/topics/product-management 
| 10| tech_career_comparison.txt| Comparisons between technology careers including software engineering, data science, and related roles.| https://ixdf.org/literature/article/what-tech-career-is-right-for-me 

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size: 500 characters**

**Overlap: 100 characters**

**Why these choices fit your documents: The documents contain career information organized into multiple sections and paragraphs. Using 500 character chunks helps keep related information together, while a 100 character overlap helps maintain context between chunks. This approach produced about 249 chunks and improved retrieval accuracy.**

**Final chunk count: 249**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used: all_MiniLM-L6-v2 from sentence transformers**

**Production tradeoff reflection: If this system were used in production, I would compare models based on retrieval accuracy, speed of the response, and context length. I would choose the model that understands the user prompts throiugh the questions well and returns accurate results especially for comparison questions.**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction: The system tells the model to answer only the retrieved context. If the context does not contain enough information, I prompted it to say , "I don't have enough information to answer that."**

**How source attribution is surfaced in the response: Each of the retrieved chunk includes metadata for the source document and chunk ID. The final response has the answer to the question along with the sources section.**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What programming languages and technical skills are commonly required for software engineers?| Languages such as Python, Java, C, C++, or Scala, along with databases, cloud computing, version control, testing, and debugging skills.| Programming languages for software engineers include Python, Java, C, C++, or Scala. Technical skills required include object-oriented programming, database architecture, Agile and Scrum project management, operating systems, cloud computing, version control, design testing, and debugging.| It displayed most of the information correctly and retrieved most of the chunks| Response is accurate and is from the information through the text file.|
| 2 | What everyday tasks does a data scientist perform?| Finding patterns in data, building models, forecasting outcomes, using machine learning, and communicating insights.|A data scientist performs tasks such as: Finding patterns and trends in datasets to uncover insights, Creating algorithms and data models to forecast outcomes, and Using machine learning techniques to improve the quality of data or product offerings| Retrieval quality is good as it identified important chunks of information| Reponse it accurate as it relates to the field. || 3 | What skills are needed to become an AI engineer?| Programming, statistics, machine learning, big data technologies, and AI frameworks such as TensorFlow and PyTorch.| To become an AI engineer, you need basic computer, information technology (IT), and math skills, as well as technical skills including knowledge of programming languages such as Python, R, Java, and C++.| Retrieval is good because it captures the chunks with correct information | Response is also good as uses the main source for its information|
| 4 | How do the responsibilities of a software engineer differ from those of a data scientist?| Software engineers focus on building and maintaining software systems, while data scientists focus on analyzing data, building models, and generating insights. | Software engineers design, develop, test, and maintain software applications and computer systems. Data scientists find patterns in datasets, create algorithms and data models, and deploy data tools.  | The retrieval is pretty good because it captured chunks from both fields as well as a common document with information about both fields | Response is also pretty accurate because it has all necessary information|
| 5 | How does UX design differ from product management?| UX design focuses on improving the user experience through research and design, while product management focuses on product strategy, development, and business goals.|I don't have enough information to answer that.
| Retrieval is not good because it failed to capture chunks of information from wither of the fields.| Response is not good as it does not have information to answer that.|

**Retrieval quality:** Relevant : Questions 1 - 4/ Partially relevant / Off-target : Question 5 
**Response accuracy:** Accurate : Questions 1 - 4/ Partially accurate / Inaccurate : Question 5

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed: How does UX design differ from product management?**

**What the system returned: I don't have enough information to answer that.**

**Root cause (tied to a specific pipeline stage): The retrieval stage did not return relevant chunks from both the UX design and product management documents. Since the model only answers using retrieved context, it did not receive enough information to generate a comparison**

**What you would change to fix it: Increase the number of retrieved chunks or improve retrieval for comparison questions so relevant chunks from both documents are included**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation: The planning document helped me define the chunking strategy, retrieval approach, and evaluation questions before coding. This made it easier to implement and test each stage of the RAG pipeline.**

**One way your implementation diverged from the spec, and why: I had to add extra setup steps such as configuring environment variables and connecting Groq with the API to the system. These steps were necessary to get the application running correctly.**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI: My chunking requirements for the chunk_text() function *
- *What it produced: Helped enhance the chunk_test() with overlapping chunks*
- *What I changed or overrode: Improved so that it accurately retrieved the correct chunks with the correct number of characters*

**Instance 2**

- *What I gave the AI: My retrieval requirements using all-MiniLM-L6-v2 and ChromaDB*
- *What it produced: function template for the embedding of the retrieval code*
- *What I changed or overrode: Added the prompt for correct and better responses for a improved accuracy.*
