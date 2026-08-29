# 🧠 AI Medical Hallucination Detector

An AI-powered medical hallucination detection and verification system that identifies potentially unsupported medical claims, retrieves supporting evidence, ranks the evidence, and generates an evidence-backed response.

## 🎯 Problem Statement

Large Language Models can generate medically inaccurate or unsupported statements. In healthcare-related applications, detecting these hallucinations is especially important because incorrect information can lead to poor decisions.

This project builds a multi-stage pipeline that analyzes medical claims, classifies them using a fine-tuned biomedical transformer model, retrieves relevant evidence, and generates a corrected response.

## 🚀 Key Features

* **Medical Hallucination Detection** using fine-tuned BiomedBERT
* **3-class classification**:

  * Supported
  * Hallucinated
  * Insufficient Evidence
* **Multi-agent processing pipeline**
* **Evidence retrieval** from biomedical sources
* **BM25-based evidence reranking**
* **LLM-based correction generation**
* **Flask REST API** for serving the pipeline
* **Git LFS** for storing the trained model weights

## 🏗️ System Architecture

```text
Medical Claim
     │
     ▼
Claim Processing
     │
     ▼
BiomedBERT Classifier
     │
     ├── Supported
     ├── Hallucinated
     └── Insufficient Evidence
     │
     ▼
Evidence Retrieval
     │
     ├── PubMed
     ├── Semantic Scholar
     └── Europe PMC
     │
     ▼
BM25 Evidence Reranking
     │
     ▼
Evidence-based Correction
     │
     ▼
Final Response
```

## 🤖 Multi-Agent Pipeline

The system uses specialized agents for different stages of the verification process.

| Agent                      | Responsibility                                |
| -------------------------- | --------------------------------------------- |
| Claim Decomposer           | Breaks medical input into individual claims   |
| Hallucination Detector     | Classifies claims using fine-tuned BiomedBERT |
| Query Formulator           | Converts claims into searchable queries       |
| PubMed Retriever           | Retrieves biomedical evidence                 |
| Semantic Scholar Retriever | Retrieves relevant research papers            |
| Europe PMC Retriever       | Retrieves biomedical literature               |
| BM25 Reranker              | Ranks retrieved evidence by relevance         |
| Correction Generator       | Generates an evidence-backed correction       |
| Response Assembler         | Produces the final structured response        |

## 🧠 Machine Learning Model

### Base Model

**Microsoft BiomedBERT**

```text
microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
```

The base biomedical language model was fine-tuned for a 3-class medical hallucination detection task.

### Training Configuration

| Parameter               |    Value |
| ----------------------- | -------: |
| Maximum sequence length |      256 |
| Batch size              |       16 |
| Epochs                  |        3 |
| Learning rate           | 2 × 10⁻⁵ |
| Weight decay            |     0.01 |
| Warmup ratio            |      0.1 |
| Optimizer               |    AdamW |

## 📊 Model Performance

The model was fine-tuned using the project's dataset-loading pipeline and evaluated on a held-out test set.

| Metric    |     Result |
| --------- | ---------: |
| Accuracy  | **94.49%** |
| Macro F1  | **86.01%** |
| Precision | **86.22%** |
| Recall    | **85.81%** |

### Dataset

The training pipeline combined available biomedical/medical datasets and produced:

```text
Total samples: 24,328

Training:   19,464
Validation:  2,432
Testing:    2,432
```

> Note: One optional dataset source (`MedFact`) was unavailable during the training run, so the final dataset consisted of the successfully loaded sources.

## 🛠️ Technology Stack

### Machine Learning

* Python
* PyTorch
* Hugging Face Transformers
* BiomedBERT
* Scikit-learn

### NLP & Retrieval

* Biomedical NLP
* PubMed
* Semantic Scholar
* Europe PMC
* BM25 ranking
* Biopython / Entrez

### Backend

* Flask
* Flask-CORS
* REST API

### LLM

* Groq API
* LLaMA-based correction generation

### Development

* Git
* GitHub
* Git LFS

## 📁 Project Structure

```text
AI-Hallucination-Detector/
│
├── agents/
│   ├── medverify_agent.py
│   └── pipeline_agents.py
│
├── config/
│   └── settings.py
│
├── core/
│   └── base_agent.py
│
├── data/
│   └── load_datasets.py
│
├── saved_model/
│   ├── config.json
│   ├── eval_results.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   └── tokenizer_config.json
│
├── training/
│   └── train.py
│
├── vision/
│   └── biovil_reader.py
│
├── api.py
├── pipeline.py
├── README.md
├── .gitignore
└── .gitattributes
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/Kundanika-08/AI-Hallucination-Detector.git
cd AI-Hallucination-Detector
```

### 2. Install dependencies

Install the required Python packages used by the project.

```bash
pip install torch transformers datasets scikit-learn accelerate biopython flask flask-cors
```

### 3. Configure environment variables

Create a `.env` file for your API credentials.

```text
GROQ_API_KEY=your_api_key_here
```

**Never commit `.env` or API keys to GitHub.**

### 4. Run the API

```bash
python api.py
```

The Flask backend starts locally and loads the fine-tuned model from:

```text
saved_model/
```

## 🔬 Training the Model

The model can be retrained using:

```bash
python training/train.py
```

The training script:

1. Loads the medical datasets.
2. Creates training, validation, and test splits.
3. Downloads the BiomedBERT base model.
4. Fine-tunes the classifier.
5. Evaluates the model.
6. Saves the trained model and tokenizer to `saved_model/`.

## 🔐 Security

API keys are stored using environment variables and are excluded from version control.

The trained model weights are stored using **Git LFS** because of their large file size.

## 📌 Project Outcome

The completed system combines:

**Transformer-based classification + biomedical evidence retrieval + relevance ranking + LLM-based correction**

to provide a practical pipeline for identifying and responding to potentially hallucinated medical information.

## 👤 Author

**Kundanika-08**

GitHub:
https://github.com/Kundanika-08
