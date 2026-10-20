from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text="""
# The Future of Artificial Intelligence

## Introduction

Artificial Intelligence (AI) is transforming the way people work, learn, and communicate. From virtual assistants to self-driving cars, AI systems are becoming part of everyday life.

## 1. Machine Learning

Machine Learning is a branch of AI that allows computers to learn patterns from data without being explicitly programmed for every task.

Common types of machine learning include:

- **Supervised Learning:** Learns from labelled data.
- **Unsupervised Learning:** Finds patterns in unlabelled data.
- **Reinforcement Learning:** Learns through rewards and penalties.

## 2. Applications of AI

AI has many practical applications across different industries.

| Industry | Application |
|---|---|
| Healthcare | Medical image analysis |
| Education | Personalized learning |
| Finance | Fraud detection |
| Transportation | Autonomous vehicles |
| Agriculture | Crop monitoring |

## 3. The Importance of Data

Data is the foundation of most modern AI systems. The quality, quantity, and diversity of training data can influence a model's performance.

Poor-quality data may introduce bias or produce inaccurate predictions. Therefore, data cleaning and preprocessing are essential steps in a machine learning pipeline.

## 4. Challenges

Despite its benefits, AI introduces several challenges:

- Privacy and data protection
- Algorithmic bias
- High computational costs
- Security risks
- Lack of transparency

Developers must consider these challenges when designing AI-powered applications.

## Conclusion

Artificial Intelligence has the potential to solve complex problems and improve productivity. However, responsible development, reliable data, and careful evaluation are necessary to build useful and trustworthy systems.

> Technology is most valuable when it solves real problems and benefits people.
"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=200,
    chunk_overlap=0
)

chunks=splitter.split_text(text)

print(chunks)

print(len(chunks))