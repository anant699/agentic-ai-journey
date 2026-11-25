# Agentic AI: Zero to Portfolio

> 8-week hands-on sprint from coding beginner to shipping real-world AI agents.

**Start:** November 17, 2026 · **Target:** January 10, 2027 · **Commitment:** ~25 hrs/week (~200 hours total)

---

## What this is

A disciplined 8-week sprint through Agentic AI, built around one principle: **you learn by building, debugging, and shipping — not by watching tutorials.**

By Jan 10 you will have:
- Working Python literacy (functions, dicts, APIs, error handling, debugging)
- Confidence calling Claude via AWS Bedrock
- Built an agent **from scratch** — no framework — so you understand the ReAct loop in your bones
- Used LangChain, Claude Agent SDK, and LangGraph in real projects
- Working knowledge of RAG, vector databases, MCP, evaluation, observability
- **2-3 portfolio projects on GitHub**
- **One deployed agent on AWS Lambda**

That's not "pro" — pro means shipping production systems with real users and real stakes, and that takes 3-6 more months of real-world reps after this. But it is **strong intermediate with a portfolio**, which is the level where interviews happen, teams hire you, and the next phase of learning compounds on real work.

Anyone selling "zero to pro in 8 weeks" is redefining pro.

---

## How this repo is organized

| File | What it is |
|---|---|
| **README.md** | This file — your map |
| **handbook.md** | The single consolidated reference. All concepts, code, patterns. **This is your textbook.** |
| **sprint-plan.md** | Week-by-week plan with daily rhythm, deliverables, and checkpoints |
| **00-python-basics/** → **capstone/** | Your work — one folder per module, with notes and code |

---

## The 8 weeks at a glance

| Week | Phase | Focus | Deliverable |
|---|---|---|---|
| 1 | **0** · Python Foundations | Environment, syntax, functions, dicts, errors | Weather CLI |
| 2 | **0** · Python Foundations | HTTP, JSON, files, modules | JSON data tool |
| 3 | **1** · AI Fundamentals | Tokens, APIs, prompting, first Claude calls | Claude CLI chatbot |
| 4 | **2a** · LangChain + Agent Loop | LCEL, chains, agent from scratch (no framework) | DIY research agent |
| 5 | **2b** · RAG + Evaluation | Embeddings, vector DBs, RAGAS | RAG-powered doc Q&A |
| 6 | **3a** · Agents & MCP | LangGraph, ReAct deep dive, MCP basics | LangGraph agent with tools |
| 7 | **3b** · Production | Memory, observability, guardrails, deploy | Deployed agent on AWS |
| 8 | **4** · Capstone | Workflow automation agent, end-to-end | Portfolio-ready project |

**⚠️ Holiday awareness:** Week 6 covers Dec 22-28 (Christmas). It's deliberately lighter. Week 7 covers New Year. Plan accordingly — the sprint plan has details.

---

## Tech stack

| Tool | Purpose | When introduced |
|---|---|---|
| Python 3.11+ | Primary language | Week 1 |
| VS Code | Editor | Week 1 |
| Git & GitHub | Version control, portfolio | Week 1 |
| AWS Bedrock | Primary LLM access (Claude) | Week 3 |
| LangChain | AI app framework | Week 4 |
| Chroma | Vector database (local) | Week 5 |
| LangGraph | Agent orchestration | Week 6 |
| MCP (Model Context Protocol) | Tool protocol standard | Week 6 |
| Langfuse | Observability | Week 7 |
| AWS Lambda | Deployment | Week 7-8 |

---

## Study principles

1. **Type the code, don't paste it.** Muscle memory matters more than people think.
2. **Break it, then fix it.** Change inputs. Read the errors. Debugging is 80% of real work.
3. **Explain back.** If you can't explain to a rubber duck, you don't know it.
4. **Ship, don't just learn.** Every module ends with code that runs.
5. **Keep a bugs journal.** You'll hit the same errors again. Write down the fix.
6. **Commit often.** Even broken code. Git history is a learning record.

---

## Progress tracker

- [ ] Week 1 — Python Foundations (Part 1)
- [ ] Week 2 — Python Foundations (Part 2)
- [ ] Week 3 — AI Fundamentals + First LLM Calls
- [ ] Week 4 — LangChain + Agent Loop from Scratch
- [ ] Week 5 — RAG + Evaluation
- [ ] Week 6 — LangGraph + MCP
- [ ] Week 7 — Production (deploy, observability)
- [ ] Week 8 — Capstone Project

---

## The path to "pro" after Jan 10

A rough outline for after the sprint, so you know where this is heading:

**Months 1-2 post-sprint:** Pick a real workflow problem (yours or a friend's business). Build and run an agent for it in production. Fix the bugs that only appear with real users and real data. This is where most of the "pro" skill actually comes from.

**Months 3-4:** Deep dive on one area — probably multi-agent systems, agent evaluation, or a domain specialization (legal, finance, healthcare). Contribute to an open-source agent framework.

**Months 5-6:** Ship something with paying users or deploy inside your company at scale. This is the point where "pro" stops being a label you want and starts being the obvious description of what you do.

Don't skip ahead. Finish the 8 weeks first.

---

## Sharing this journey

This repo is open. If you're learning Agentic AI too:
- Fork it, follow along, submit improvements
- Open issues when something is unclear — your confusion helps the next person
- Share your project work

Learning in public is a feature.

---

*Learning with Claude as coach · Last updated: November 2026*
