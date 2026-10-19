import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.runnables import RunnableParallel
load_dotenv()

model1 = ChatOpenAI(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
    temperature=0,
    timeout=120,
    max_retries=1,
    max_tokens=4096,
)

model2=ChatNVIDIA(
  model="meta/llama-3.2-90b-vision-instruct",
  api_key=os.getenv("NVIDIA_API_KEY_LLAMA"),
  temperature=0,
  timeout=180,
  top_p=1,
  max_completion_tokens=4096,
)

prompt1=PromptTemplate(
    template='Generate a short and simple notes from the following text {text}',
    input_variables=['text']
)
prompt2=PromptTemplate(
    template='Generate 5 short simple questions and answers from the text\n {text}',
    input_variables=['text']
)
prompt3 = PromptTemplate(
    template="""Merge the following notes and quiz into one organized document.

Notes:
{notes}

Quiz:
{quiz}""",
    input_variables=["notes", "quiz"],
)

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'notes':  prompt1 | model1 |parser,
    'quiz': prompt2 | model2| parser
})

merge_chain=prompt3 | model1| parser
chain=parallel_chain|merge_chain

text="""
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

chain.invoke({'text':text})