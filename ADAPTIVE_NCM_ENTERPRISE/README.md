# Uncertainty-Guided Adaptive NCM for Enterprise Agentic AI

An enterprise-grade multi-agent architecture featuring a **Custom Neural Cognitive Model (NCM)** for dynamic cognitive routing, uncertainty estimation, multi-agent orchestration, procedural/episodic memory retrieval, and self-adaptive failure recovery.

## Architecture Highlights
- **Cognitive Engine**: PyTorch-backed encoder, MC-Dropout/Ensemble uncertainty estimator, confidence calculator, state manager, and contextual bandit adaptive policy.
- **Agent Mesh**: 6 specialized autonomous agents (Planning, Reasoning, Knowledge, Verification, Reflection, Recovery).
- **Orchestration**: Dynamic Execution Graph scheduling, conditional dynamic routing based on cognitive uncertainty.
- **Memory Subsystem**: Dual Episodic/Semantic vector storage (Qdrant), Procedural patterns, and Failure reflection logs.
- **Learning & Calibration**: Supervised calibration routines and policy optimizers for continuous agent routing adjustment.
- **Infrastructure**: FastAPI engine, React + TypeScript Frontend, PostgreSQL database, Qdrant vector store, Redis cache, Prometheus monitoring metrics.

## Quick Start Guide

### 1. Requirements & Setup
Ensure Docker, Python 3.10+, and Node.js are installed.

```bash
git clone <repository-url>
cd ADAPTIVE_NCM_ENTERPRISE
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

### 2. Running Services with Docker
```bash
docker-compose up -d
```

### 3. Running System Standalone / Simulation Demo
```bash
python main.py
```

### 4. Running Backend Server
```bash
uvicorn backend.main:app --reload --port 8000
```
Visit API Documentation at `http://localhost:8000/docs`.
The dashboard is available at `http://localhost:8000/dashboard/` when running the backend, including when Node.js is unavailable.

### 5. Running Frontend Dashboard
```bash
cd frontend
npm install
npm run start
```
Navigate to `http://localhost:3000` to inspect cognitive metrics, uncertainty gauges, and real-time execution graphs.
