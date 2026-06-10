# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

The domain that I choose is about technology career information. The goal of this project is to help users learn about the different technology careers such as software engineering, data science, machine learning, cybersecurity, cloud engineering, AI engineering, UX design, DevOps, and Product Management. Although there is information about different careers online, it is available across many websites which makes it difficult to compare roles within tech industry, required skills, job outlook, and career paths all in one place.  

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source                    | Description                                                                                            | URL or location |
|---|---------------------------|--------------------------------------------------------------------------------------------------------|-----------------|
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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size: 500 characters**

**Overlap: 100 characters **

**Reasoning: The documents contain career information organized into multiple sections and paragraphs. Using 500 character chunks helps keep related information together, while a 100 character overlap helps maintain context between chunks. This approach produced about 249 chunks and improved retrieval accuracy. **

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model: all_MiniLM-L6-v2 from sentence transformers**

**Top-k: 4 chunks per query**

**Production tradeoff reflection: If this system were used in production, I would compare models based on retrieval accuracy, speed of the response, and context length. I would choose the model that understands the user prompts throiugh the questions well and returns accurate results especially for comparison questions.**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What programming languages and technical skills are commonly required for software engineers?| Languages such as Python, Java, C, C++, or Scala, along with databases, cloud computing, version control, testing, and debugging skills.|
| 2 | What everyday tasks does a data scientist perform?| Finding patterns in data, building models, forecasting outcomes, using machine learning, and communicating insights.|
| 3 | What skills are needed to become an AI engineer?| Programming, statistics, machine learning, big data technologies, and AI frameworks such as TensorFlow and PyTorch.|
| 4 | How do the responsibilities of a software engineer differ from those of a data scientist?| Software engineers focus on building and maintaining software systems, while data scientists focus on analyzing data, building models, and generating insights. |
| 5 | How does UX design differ from product management?| UX design focuses on improving the user experience through research and design, while product management focuses on product strategy, development, and business goals.|

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. The retrieval system may return chunks from careers that are related instead of the most relevant documents since some career paths within tech industry require similar skills and technological tools and platforms.

2. The questions asked about comparison may require information from multiple documents. If all of the relevant chunks are not retrieved, the generated response may be incomplete or not fully accurate. 

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->


Career Information files (.txt) -> Load Documents -> Cleaning (to remove whitespaces) -> Chunking (500 character chunks with 100 charcters of overlap) -> Embedding + Vectore Storage (embeddings from all-MiniLM-L6-v2 stored in ChromaDB) -> Retrieval (retrieve top 4 relevant chunks per question asked) -> Generation (answer for the question prompt) -> Interface (Gradio web UI for displaying answer and sources)
           

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking: I will give ChatGPT my Chunking strategy for being able to implement chunk_text using 500 character chunk size and 100 character overlap. I will verfiy the output through generated chunks**

**Milestone 4 — Embedding and retrieval: I will give chatGPT my retrieval approach for implementing the all-MiniLM-L6-v2 and retrieving top chunks with the ChromaDB. I will further implement these and verify outputs through testing sample queries.**

**Milestone 5 — Generation and interface: I will give ChatGPT my Architectural diagram for connecting to Gradio interface. I will further test responses through the UI as well.**
