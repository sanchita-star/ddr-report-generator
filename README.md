# 🏗️ AI-Based DDR Report Generator

## 📌 Overview

This project is an AI-powered system that converts raw **inspection reports** and **thermal reports** into a structured **Detailed Diagnostic Report (DDR)**.

The system focuses on extracting relevant observations, merging multi-source data, and generating a clear, client-friendly report using a Large Language Model (LLM).

---

## 🎯 Problem Statement

Inspection and thermal reports are often:
- Unstructured
- Redundant
- Difficult to interpret for clients

This project solves that by:
- Extracting key observations
- Combining multiple data sources
- Generating a structured and readable DDR

---

## 🚀 Solution Approach

The system follows a modular pipeline:

1. **Document Ingestion**
   - Accepts inspection and thermal reports (PDF/text)

2. **Text Extraction**
   - Extracts raw text from uploaded documents

3. **Observation Extraction**
   - Identifies relevant areas (e.g., wall, roof, etc.)

4. **Data Merging**
   - Combines inspection + thermal findings
   - Removes duplicates
   - Handles missing data

5. **LLM-based Report Generation**
   - Uses Groq LLM (LLaMA 3.1) to generate structured DDR
   - Applies strict prompting rules for consistency

6. **Output Rendering**
   - Displays structured report in a clean UI

---

## 🧠 Key Features

- ✅ Multi-document input support
- ✅ Merges inspection and thermal data
- ✅ Handles missing information ("Not Available")
- ✅ Avoids duplicate observations
- ✅ Structured and client-friendly output
- ✅ Modular backend architecture
- ✅ Model-agnostic design (can switch LLM providers)

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **LLM:** Groq (LLaMA 3.1)
- **PDF Processing:** PyPDF2

---

## 📂 Project Structure
 
---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd ddr-report-generator
pip install -r requirements.txt
setx GROQ_API_KEY "
cd backend
python app.py
frontend/index.html

