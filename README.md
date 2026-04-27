# 🏗️ AI-Based DDR Report Generator

## 📌 Overview

This project is an AI-powered system that converts raw **Inspection Reports** and **Thermal Reports** into a structured **Detailed Diagnostic Report (DDR)**.

The system focuses on extracting relevant observations, merging multi-source data, and generating a clear, client-friendly report using a Large Language Model (LLM).

---

## 🎯 Objective

To design an AI workflow that:

* Extracts key observations from technical documents
* Combines inspection and thermal data logically
* Handles missing or conflicting information
* Produces a structured, professional DDR

---

## 🚀 Solution Approach

The system follows a modular pipeline:

1. **Document Ingestion**

   * Accepts inspection and thermal reports (PDF/text)

2. **Text Extraction**

   * Extracts raw text using PDF parsing

3. **Observation Extraction**

   * Identifies area-wise issues (e.g., wall, roof, etc.)

4. **Data Merging**

   * Combines inspection + thermal findings
   * Removes duplicate observations
   * Handles missing/conflicting data

5. **LLM-based Report Generation**

   * Uses Groq (LLaMA 3.1) to generate structured DDR
   * Applies strict prompting for consistency and clarity

6. **Output Rendering**

   * Displays structured report in a clean UI

---

## 🧠 Key Features

* Multi-document input (inspection + thermal)
* Logical merging of observations
* Handles missing data ("Not Available")
* Avoids duplicate issues
* Structured and client-friendly output
* Modular backend design
* Model-agnostic architecture (can switch LLMs)

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **LLM:** Groq API (LLaMA 3.1)
* **PDF Processing:** PyPDF2

---

## 📂 Project Structure

```
ddr-report-generator/
│
├── frontend/
│   └── index.html
│
├── backend/
│   ├── app.py
│   ├── extractor.py
│   ├── merger.py
│   ├── generator.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-link>
cd ddr-report-generator
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Set Environment Variable

⚠️ Do NOT hardcode API keys

```
setx GROQ_API_KEY "your_api_key_here"
```

Restart terminal after setting.

---

### 4. Run Backend

```
cd backend
python app.py
```

---

### 5. Run Frontend

Open:

```
frontend/index.html
```

in your browser.

---

## 🧪 How It Works

1. Upload inspection and/or thermal reports
2. System extracts relevant observations
3. Merges multi-source data logically
4. Sends structured input to LLM
5. Generates DDR report
6. Displays output in UI

---

## ⚠️ Limitations

* Uses basic keyword-based extraction
* No image-based thermal analysis
* Output depends on input data quality
* LLM responses may vary

---

## 🔮 Future Improvements

* Advanced NLP-based extraction
* Thermal image processing
* Improved severity classification
* Export as formatted PDF
* Database integration

---

## 📽️ Demo

👉 Add your Loom video link here

---

## 👩‍💻 Author

Sanchita Patil

---

## ⭐ Note

This project emphasizes **AI workflow design, reasoning, and structured output generation**, rather than UI complexity.
/index.html

