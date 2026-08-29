import os
from dataclasses import dataclass


@dataclass
class SystemConfig:

    # PubMed
    pubmed_email: str = os.getenv("PUBMED_EMAIL", "")
    pubmed_max_results: int = 10

    # Model
    model_path: str = "saved_model"
    max_length: int = 512

    # Planner
    uncertainty_threshold: float = 0.60
    expand_threshold: float = 0.5
    max_planner_iterations: int = 3

    # Corrector
    corrector_model: str = "llama-3.1-8b-instant"

    # Groq API key
    groq_api_key: str = os.getenv("GROQ_API_KEY", "")