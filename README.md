# AI Video Assistant

An AI-powered video analysis and meeting intelligence application that transforms YouTube videos into structured insights and enables conversational question answering using Retrieval-Augmented Generation (RAG).

## Overview

AI Video Assistant processes a YouTube video through an end-to-end AI pipeline:

**YouTube Video → Audio Processing → Whisper Transcription → LLM Analysis → RAG → Conversational Q&A**

The application generates a transcript, summary, title, action items, key decisions, and open questions from the video. The transcript is also indexed into a vector database, allowing users to ask natural-language questions about the content.

## Key Features

- **YouTube Video Processing** — Extracts audio from YouTube videos using `yt-dlp`
- **Speech-to-Text** — Transcribes audio using OpenAI Whisper
- **AI Summarization** — Generates concise summaries and meaningful session titles
- **Meeting Intelligence** — Extracts action items, key decisions, and open questions
- **RAG-based Q&A** — Enables semantic search and question answering over the transcript
- **Vector Search** — Uses embeddings and ChromaDB for efficient retrieval
- **Interactive UI** — Streamlit-based interface for processing and querying videos

## Architecture

```text
                     YouTube URL
                          │
                          ▼
                   Audio Extraction
                          │
                          ▼
                   Audio Processing
                          │
                          ▼
                  Whisper Transcription
                          │
                          ▼
                      Transcript
                          │
              ┌───────────┼───────────┐
              │           │           │
              ▼           ▼           ▼
         Summarization  Extraction   RAG Pipeline
              │           │           │
              │      ┌────┼────┐      ▼
              │      │    │    │   Chunking
              │      ▼    ▼    ▼      │
              │   Tasks Decisions     ▼
              │        Questions   Embeddings
              │                       │
              │                       ▼
              │                    ChromaDB
              │                       │
              └───────────────────────┤
                                      ▼
                                   Mistral AI
                                      │
                                      ▼
                              Conversational Q&A
