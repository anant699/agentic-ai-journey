# 8-Week Sprint Plan — Agentic AI

**Nov 17, 2026 → Jan 10, 2027** · 25 hrs/week · 200 total hours

This is your execution plan. The handbook.md has the concepts and code; this file tells you **what to do when**.

---

## How to use this plan

Each week has:
- **Theme** — what you're trying to internalize
- **Daily rhythm** — rough split of weekday vs. weekend work
- **Learning (from handbook.md)** — sections to read
- **Hands-on work** — code to write, exercises to do
- **Deliverable** — the one thing that must exist by end-of-week
- **Checkpoint** — self-test questions. If you can't answer them, don't move on.

**The one non-negotiable rule:** Finish the week's deliverable before moving to the next week. Skipping forward is the fastest way to end up confused in week 6 with no foundation.

---

## Week 1: Python Foundations — Part 1
**Dates:** Nov 17–23 · **Phase 0** · **~25 hrs**

### Theme
Get Python into your fingers. Variables, functions, data structures, control flow. Don't aim for mastery — aim for literacy.

### Daily rhythm
| Day | Focus | Hours |
|---|---|---|
| Mon | Environment setup (Python, VS Code, Git, GitHub repo) | 3 |
| Tue | Variables, types, basic I/O, arithmetic | 3 |
| Wed | Functions, control flow (if/else, loops) | 3 |
| Thu | Lists and dictionaries (critical for everything) | 3 |
| Fri | Error handling (try/except) | 2 |
| Sat | Review + start Weather CLI project | 6 |
| Sun | Finish Weather CLI, commit to GitHub | 5 |

### Learning (from handbook.md)
- Phase 0, Sections 0.1 through 0.5

### Hands-on work
- Install Python 3.11+, VS Code, Git
- Create GitHub repo (`agentic-ai-journey`), push README.md and handbook.md
- Write 20+ small scripts from the Phase 0 exercises
- Keep a `bugs-journal.md` in your repo — write down every error you hit and how you fixed it

### Deliverable
**Weather CLI** — a command-line tool that takes a city name and prints the current weather. Uses a free weather API (OpenWeatherMap or similar). Pushed to `00-python-basics/weather-cli/` in your repo.

### Checkpoint — must be able to answer
1. What's the difference between a list and a dictionary? When would you use each?
2. What happens when a function doesn't have a `return` statement?
3. What does `try/except` do? Give one example where you'd use it.
4. What's a virtual environment and why does it matter?

---

## Week 2: Python Foundations — Part 2
**Dates:** Nov 24–30 · **Phase 0** · **~25 hrs**

### Theme
APIs, JSON, files, and the Python ecosystem. By end of week, you should be comfortable reading other people's code.

### Daily rhythm
| Day | Focus | Hours |
|---|---|---|
| Mon | HTTP, the `requests` library, calling a REST API | 3 |
| Tue | JSON parsing (the data format every API speaks) | 3 |
| Wed | File I/O (read, write, append, context managers) | 3 |
| Thu | Modules, pip, requirements.txt | 3 |
| Fri | Classes basics (just enough to read SDK code) | 3 |
| Sat | JSON data tool mini-project | 5 |
| Sun | Finish, commit, write notes | 5 |

### Learning (from handbook.md)
- Phase 0, Sections 0.6 through 0.10

### Hands-on work
- Call 3 different public APIs and parse the responses
- Read/write JSON to files
- Write a Python module you can import elsewhere

### Deliverable
**JSON Data Tool** — a script that calls a public API (e.g., GitHub, crypto prices, news headlines), saves results as JSON to a file, and reads/filters them. Lives in `00-python-basics/json-tool/`.

### Checkpoint — must be able to answer
1. What's the difference between `requests.get()` and `response.json()`?
2. What's a `KeyError` and how do you avoid it when parsing JSON?
3. What does `with open(...) as f:` do? Why not just `f = open(...)`?
4. What's `pip install -r requirements.txt` doing?

---

## Week 3: AI Fundamentals + First LLM Calls
**Dates:** Dec 1–7 · **Phase 1** · **~25 hrs**

### Theme
Understand what an LLM actually is (and isn't), how APIs work, and make your first real Claude calls via AWS Bedrock.

### Daily rhythm
| Day | Focus | Hours |
|---|---|---|
| Mon | AI fundamentals: tokens, embeddings, transformers, prediction vs. understanding | 3 |
| Tue | Prompt engineering: system prompts, few-shot, chain-of-thought | 3 |
| Wed | AWS Bedrock setup, first Claude API call | 3 |
| Thu | Streaming, parameters (temperature, max_tokens), message structure | 3 |
| Fri | Prompt experimentation — same task, 5 different prompts, compare results | 3 |
| Sat | Build CLI chatbot | 5 |
| Sun | Add conversation memory, polish | 5 |

### Learning (from handbook.md)
- Phase 1, all sections (1.1 through 1.5)

### Hands-on work
- Set up AWS Bedrock access (I'll walk you through in-session)
- Make 10+ different Claude calls — vary prompts, see how output changes
- Compare Opus, Sonnet, Haiku on the same task

### Deliverable
**Claude CLI Chatbot** — a terminal chat app that calls Claude, remembers the conversation history, streams responses, and lets you switch models mid-chat. Lives in `01-first-llm-calls/cli-chatbot/`.

### Checkpoint — must be able to answer
1. What's a token? Why does the number of tokens matter for cost and context?
2. What's the difference between a system prompt and a user message?
3. Why does temperature=0 produce more consistent outputs?
4. How does your chatbot "remember" the conversation when LLM APIs are stateless?

---

## Week 4: LangChain + Agent Loop from Scratch
**Dates:** Dec 8–14 · **Phase 2a** · **~25 hrs**

### Theme
Two things in parallel: learn LangChain (the industry framework), AND build an agent from scratch with no framework so you understand what LangChain is doing under the hood.

### Daily rhythm
| Day | Focus | Hours |
|---|---|---|
| Mon | LangChain basics: models, prompts, chains, LCEL | 3 |
| Tue | Output parsers (structured data from LLMs), memory | 3 |
| Wed | What is the ReAct loop? Why does it matter? | 3 |
| Thu | Build an agent **from scratch** — no framework, just Python + Claude + a loop | 3 |
| Fri | Add 2-3 tools to your scratch agent (web search, file read, calculator) | 3 |
| Sat | Build DIY research agent — handles multi-step research tasks | 5 |
| Sun | Compare: rewrite same agent in LangChain, see the difference | 5 |

### Learning (from handbook.md)
- Phase 2, Sections 2.1 through 2.4 (LangChain basics)
- Phase 3, Sections 3.1 through 3.3 (agent loop concepts)

### Hands-on work
- Write the ReAct loop yourself in ~100 lines of Python before touching any framework
- Then write the same thing in LangChain — notice what the framework handles

### Deliverable
**DIY Research Agent** — takes a question, uses web search + file tools to find and synthesize an answer. Two versions: scratch (no framework) and LangChain. Lives in `04-agent-loop/`.

### Checkpoint — must be able to answer
1. Walk through the ReAct loop — Reason, Act, Observe. When does it stop?
2. What is the `|` operator in LangChain doing? What does it return?
3. Why would you ever write an agent without a framework?
4. What makes a good tool description for an LLM?

---

## Week 5: RAG + Evaluation
**Dates:** Dec 15–21 · **Phase 2b** · **~25 hrs**

### Theme
Give your agents access to private knowledge via RAG (Retrieval-Augmented Generation). Learn to measure if your system is actually good (evaluation).

### Daily rhythm
| Day | Focus | Hours |
|---|---|---|
| Mon | Embeddings explained — why they make semantic search possible | 3 |
| Tue | Vector databases — Chroma locally, Pinecone/pgvector for production | 3 |
| Tue | Chunking strategies (the decision most people get wrong) | 2 |
| Wed | Build full RAG pipeline — ingestion + query | 3 |
| Thu | Advanced RAG: hybrid search, re-ranking, HyDE | 3 |
| Fri | Evaluation — why you need it, how to do it, RAGAS | 3 |
| Sat | Build RAG doc Q&A bot on 20-50 docs of your choice | 4 |
| Sun | Build an eval suite for it — measure faithfulness, relevancy | 4 |

### Learning (from handbook.md)
- Phase 2, Sections 2.5 through 2.9 (RAG, vector DBs, evaluation)

### Hands-on work
- Index at least 20 docs into Chroma
- Compare different chunking strategies on the same docs
- Build an eval set of 20 questions with known answers, measure your RAG
- Use LLM-as-judge to score custom quality dimensions

### Deliverable
**RAG-Powered Doc Q&A** — point it at a folder of PDFs/text files and ask questions about them. Includes a `tests/` folder with 20 eval questions and automated scoring. Lives in `05-rag/`.

### Checkpoint — must be able to answer
1. Why do "cancel my subscription" and "stop paying" have similar embeddings?
2. If your chunks are too large, what goes wrong? Too small?
3. What's RAGAS measuring with "faithfulness" vs. "answer_relevancy"?
4. When would you use hybrid search instead of pure vector search?

---

## Week 6: LangGraph + MCP (⚠️ Holiday Week)
**Dates:** Dec 22–28 · **Phase 3a** · **~18 hrs** (reduced for Christmas)

### Theme
Learn LangGraph (the production-grade framework for complex agents) and MCP (Model Context Protocol — the standard for how agents connect to tools).

**Why lighter this week:** Christmas is Dec 25. Plan around your family time. If you can't do 25 hours, that's fine. Finish the deliverable, even if less polished.

### Daily rhythm
| Day | Focus | Hours |
|---|---|---|
| Mon | LangGraph intro — nodes, edges, state, graphs | 3 |
| Tue | Build a LangGraph agent with conditional routing | 3 |
| Wed | Human-in-the-loop with LangGraph checkpointer | 2 |
| Thu | MCP concepts — architecture, servers, clients | 2 |
| Fri-Sun | Christmas window — keep it light, finish deliverable | 8 |

### Learning (from handbook.md)
- Phase 3, Sections 3.4 through 3.6 (LangGraph, MCP)

### Hands-on work
- Rewrite your DIY research agent using LangGraph with proper state management
- Use an existing MCP server (filesystem or GitHub) with Claude Desktop
- Optional if time: write your own simple MCP server

### Deliverable
**LangGraph Agent with Tools** — a stateful agent that handles a multi-step business task (e.g., "research these 3 companies and create a comparison report"). Lives in `06-langgraph-mcp/`.

### Checkpoint — must be able to answer
1. What does LangGraph give you that `create_react_agent` doesn't?
2. What is the agent state? Why does it matter?
3. What problem does MCP solve? Give the USB-C analogy.
4. When would you add human-in-the-loop to an agent?

---

## Week 7: Production — Memory, Observability, Deployment
**Dates:** Dec 29 – Jan 4 · **Phase 3b** · **~22 hrs** (New Year compressed)

### Theme
Turn your agent from a prototype into something that could run in production. Memory across sessions. Observability. Guardrails. Deployment.

### Daily rhythm
| Day | Focus | Hours |
|---|---|---|
| Mon | Agent memory — the 4 types, when to use each | 3 |
| Tue | Observability with Langfuse — tracing every call, cost tracking | 3 |
| Wed | Guardrails, safety, prompt injection defense | 3 |
| Thu | AWS Lambda deployment — package, deploy, invoke | 3 |
| Fri | Error handling, retries, cost limits | 3 |
| Sat | Deploy your Week 6 agent to AWS Lambda with full observability | 5 |
| Sun | ⚠️ New Year's Day — rest or catch up | 2 |

### Learning (from handbook.md)
- Phase 3, Sections 3.7 through 3.10

### Hands-on work
- Set up Langfuse (free tier) — trace every call in your existing projects
- Add cost tracking: every agent run writes to a cost log
- Deploy your Week 6 agent to AWS Lambda — wire up API Gateway so you can call it over HTTP

### Deliverable
**Deployed Agent on AWS** — a public HTTPS endpoint that invokes your LangGraph agent. Langfuse dashboard showing all runs. Cost per run visible. Lives in `07-production/`.

### Checkpoint — must be able to answer
1. What's the difference between in-context memory and long-term memory?
2. What does Langfuse show you that print statements can't?
3. What's prompt injection? How do you defend against it?
4. What's the cold-start problem on Lambda and how do you mitigate it?

---

## Week 8: Capstone Project
**Dates:** Jan 5–10 · **Phase 4** · **~25 hrs**

### Theme
Build and ship one real business workflow automation agent. This is your portfolio piece — the thing you'll show interviewers, send to friends, and use yourself.

### Daily rhythm
| Day | Focus | Hours |
|---|---|---|
| Mon | Scope the capstone — exact use case, user, inputs, outputs | 3 |
| Tue | Design agent: tools, memory, safety, failure modes | 3 |
| Wed | Build core agent | 4 |
| Thu | Add RAG if needed, observability, guardrails | 4 |
| Fri | Deploy to AWS, test end-to-end | 4 |
| Sat | Write a strong README, record a demo video, write a blog post | 4 |
| Sun | **Done.** Push final version. Celebrate. | 3 |

### Capstone candidates (pick one)
Pick the one closest to your actual work or life — motivation matters.

| Project | What it does |
|---|---|
| **Email Triage Agent** | Reads your inbox, categorizes emails, drafts replies, flags urgent ones |
| **Document Processing Agent** | Watches a folder, extracts structured data from PDFs/docs, routes to destinations |
| **Meeting Assistant** | Takes a recording/transcript, summarizes, extracts action items, writes follow-up emails |
| **Report Generator** | Pulls from multiple data sources (CRM, Google Sheets, APIs), generates periodic reports |
| **Research Agent** | Takes a topic, researches it across web and your private docs, produces a briefing |

### Deliverable
**Portfolio-ready capstone** in `capstone/` folder containing:
- Complete working code
- README with: problem statement, architecture diagram, setup instructions, demo
- Eval suite (at least 10 test cases)
- Deployed on AWS with public endpoint or clear demo video
- A 500-word blog post in `capstone/WRITEUP.md` explaining what you built and what you learned

### Final checkpoint
If you can hand the capstone and README to a stranger and they can understand what it does, how it works, and how to run it — **you've hit the strong-intermediate bar.**

---

## Daily/weekly rhythm advice

**Weekday schedule (3-4 hrs/day):**
- 1 hour before work: read handbook, type small code snippets
- 2-3 hours evening: real coding on the week's deliverable
- Last 15 min: update bugs-journal.md, commit code

**Weekend schedule (5-6 hrs/day):**
- Block 2-hour sessions with 15-min breaks
- One session for learning, one for building
- Don't exceed 6 hrs/day — diminishing returns, you'll burn out

**Red flags (slow down if you see these):**
- Rushing through handbook sections without doing exercises → you're accumulating knowledge debt
- Stuck on a bug for >1 hour → ask me, or take a walk and come back
- Dreading opening VS Code → you're either overloaded or on the wrong project; talk to me

---

## When you're stuck

**Order of operations when something breaks:**
1. **Read the error.** Actually read it. The answer is usually in the last line.
2. **Check your bugs-journal.md** — have you hit this before?
3. **Reproduce it in isolation** — strip the code down to the smallest thing that still breaks.
4. **Search the exact error message** — someone else has hit it.
5. **Ask Claude** — paste the error, the code, what you expected vs what happened.

Steps 1-4 are where learning happens. Don't skip to step 5 immediately — it feels faster but builds no skill.

---

## End-of-sprint milestones

By Jan 10, your GitHub repo should contain:

- [ ] 8 module folders with working code
- [ ] A bugs-journal.md with 50+ entries
- [ ] 2-3 deployed projects (or one deployed + clear demos)
- [ ] Handbook.md marked up with your personal notes
- [ ] One capstone with blog post
- [ ] Your progress tracker in README.md all checked off

This is what "strong intermediate with portfolio" looks like on paper. If you've genuinely done the work — not just copied code, but typed it, broken it, fixed it, explained it — you'll have something to show and skills that compound.

---

*Last updated: November 2026*
