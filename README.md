# ⚖️ Trustworthy AI Workshop

This repository contains hands-on machine learning exercises for exploring AI documentation practices using Data Cards,Model Cards and Use Case Cards in an interactive and fun way!

## Few words about the Repo Contents

- `experiments/iris_experiments.py` — Classification using Iris dataset with logistic regression and random forests
- `experiments/cancer_experiments.py` — Binary classification on breast cancer data with decision trees and boosting
- `experiments/wine_experiments.py` — Multi-class classification with SVM and random forests
- `requirements.txt` — Python dependencies
- `cards/` — Templates for Model and Data documentation
- `card_examples/` — Examples for card-based documentation from real-world cases
- `templates/` — Templates for a documentation checklist.


## ▶️ How to Run

```bash
python -m venv venv_workshop
source venv_workshop/bin/activate   # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
python experiments/iris_experiments.py 
```

Repeat for each experiment script.
Feel free to use any model or dataset you like! (could be from your research or interests/hobbies!) These are just examples 😁

Note that you can adapt the code to save some important information, such as training parameters, splits, models used and performance metrics in a dedicated file to help you later.

## 🗒️ Documentation Templates
Can be found in this repository in the following paths:

- `cards/dataset_card_template.json` # for datasets
- `cards/datasheets_for_datasets_template.json` #for datasets
- `cards/model_card_template.json` # for models
- `cards/model_card_template.json` # for models

These are human- and machine-readable documentation templates to be filled in after experimentation.

--- 
## 💻 Exercises - Your time to shine!

* Step 1: Run each experiment, by following the instructions above.
For each experiment run, do the following:
* Step 2: Fill in (some or all of) the following data cards:
- The one here `cards/DataCardsExtendedTemplate.docx` (you can use this as an example.--> `card_examples\Open Images Extended - MIAP - Data Card.pdf`)
- The two found in the documentation templates above. 
* Step 3: Fill in (some or all of) the following model cards:
- The two found in the documentation templates above. 
- Create a model card in a fun and interactive way! https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool (you can find many examples here, for instance https://huggingface.co/google/vaultgemma-1b )
- Bonus tip: Feel free to explore Google's model cards here --> https://modelcards.withgoogle.com/explore-a-model-card 
* Step 4: Fill in the following use case cards:
- `cards/UseCaseCard_Template.docx` 
- An example can be found here : `card_examples/Filling-in-a-use-case-card-example-of-a-scene-narrator-application_W640.jpg`

* Step 6: Repeat for as many experiments as you'd like!
* Step 7: Note the advantages, disadvantages, limitations, considerations and anything relevant, because a Group Discussion is coming up! 🥳

---
## Optional Exercises

### 🔍 Compare Documentation Practices

Pick 2–3 dataset or model cards from different sources (e.g. Hugging Face, Google, OpenML) and:

- Evaluate their completeness using the checklist found here: `templates/documentation_review_checklist.md`
- Identify what makes each one effective or lacking
- Present your findings in small groups

Suggested sources:
- Inside the repo: `/card_examples/`
- Hugging Face: https://huggingface.co/models
- Google PAIR: https://pair-code.github.io/datacardsplaybook/
- OpenML: https://www.openml.org/

---
### For AI-generated content fill in an AI usage card!
To facilitate the documentation and reporting needs for the responsible use of AI-generated content, AI Usage Cards is proposed as a standardized practice to incorporate the principles of transparency, integrity, and accountability. (Wahle, Jan Philip & Ruas, Terry & Mohammad, Saif M. & Meuschke, Norman & Gipp, Bela, ‘AI Usage Cards: Responsibly Reporting AI-Generated Content’. 2023 ACM/IEEE Joint Conference on Digital Libraries (JCDL), 2023, https://arxiv.org/pdf/2303.03886 )
Fill in the following AI usage cards for yourself to check it out:
- https://beta.ai-cards.org/ 

---
## Create Your Own Card Template based on existing gaps, future directions and what we've learnt!

Using inspiration from **model**, **data**, **use case**, **AI** card (and others) documentation examples:

- Create a hybrid YAML/Markdown template that combines features from all
- Include metadata fields for:
  - Model details
  - Dataset schema
  - Usage context
  - Ethics and limitations
  - Lessons learnt
  - ... and anything else you deem appropriate

---

### 📝 Example: Hybrid Card Template (YAML format)

```yaml
card_type: hybrid
name: Titanic Survival Classifier
version: 1.0
owner:
  name: Your Name
  contact: your@email.com

model:
  framework: scikit-learn
  type: logistic regression
  trained_on: titanic.csv
  performance:
    metric: accuracy
    value: 0.82

data:
  name: Titanic Dataset
  source: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
  license: CC0
  features:
    - name: Age
      type: numerical
      description: Age of passenger
    - name: Pclass
      type: categorical
      description: Ticket class

usage:
  intended_users:
    - educators
    - students
  limitations:
    - may not generalize to modern demographics
    - missing values in 'Age' column
  ethical_considerations:
    - sensitive to gender/age biases
```

---
## License

This material is created by Georgia Gkioka and is provided for educational purposes only.
