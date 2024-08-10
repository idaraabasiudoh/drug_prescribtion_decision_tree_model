# Drug Classification Using Decision Tree

## Table of Contents
- [Introduction](#introduction)
- [Objectives](#objectives)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Visualizing the Decision Tree](#visualizing-the-decision-tree)
- [Contributions](#contributions)
- [Acknowledgments](#acknowledgments)
- [Change Log](#change-log)
- [License](#license)

## Introduction
This repository contains a machine learning project focused on classifying drugs based on patient characteristics using a Decision Tree classifier. The project leverages Python and popular data science libraries such as scikit-learn, pandas, and matplotlib.

## Objectives
The primary objectives of this project are:
- To implement a Decision Tree classifier using scikit-learn to predict drug type.
- To train, test, and evaluate the model on a dataset of patient characteristics and corresponding drug prescriptions.
- To visualize the decision tree for interpretability.

## Dataset
The dataset used in this project, `drug200.csv`, contains data on 200 patients, including age, sex, blood pressure (BP), cholesterol levels, the ratio of sodium to potassium, and the drug type prescribed. The dataset includes the following columns:
- `Age`: Age of the patient.
- `Sex`: Gender of the patient (F or M).
- `BP`: Blood Pressure level (LOW, NORMAL, HIGH).
- `Cholesterol`: Cholesterol level (NORMAL, HIGH).
- `Na_to_K`: Ratio of sodium to potassium in the blood.
- `Drug`: Type of drug prescribed.

[Dataset Source](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv)

### Requirements

Ensure you have the following dependencies installed:

- `Python 3.x`
- `numpy`
- `pandas`
- `scikit-learn`
- `matplotlib`

## Installation
To run this project locally, you need to have Python installed along with the required libraries. You can install the necessary packages using the following command:

Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/idaraabasiudoh/drug-classification-decision-tree.git
cd drug-classification-decision-tree
pip install -r requirements.txt
```


## Usage
To use this repository, follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/idaraabasiudoh/drug-classification-decision-tree.git
    ```
2. Navigate to the project directory:
    ```bash
    cd drug-classification-decision-tree
    ```
3. Run the classification script:
    ```bash
    python classify_drug.py
    ```

## Modeling
The modeling process involves the following steps:
1. **Data Loading**: Import the dataset and understand its structure.
2. **Data Preprocessing**: Convert categorical variables to numerical values using label encoding.
3. **Data Splitting**: Split the data into training and testing sets.
4. **Model Training**: Train a Decision Tree model using the training set.
5. **Model Prediction**: Make predictions on the test set using the trained model.

## Evaluation
The performance of the model is evaluated using the test dataset. The key metrics used for evaluation include:

- **Accuracy**: This metric indicates the proportion of correct predictions made by the model out of all predictions.
    ```python
    from sklearn import metrics
    print("Decision Tree's Accuracy:", metrics.accuracy_score(y_testset, predTree))
    ```

### Example Code
Here is an example of how to evaluate the model using accuracy:

```python
from sklearn import metrics

# Assuming y_testset contains the actual values and predTree contains the predicted values
print("Decision Tree's Accuracy:", metrics.accuracy_score(y_testset, predTree))
```

## Visualizing the Decision Tree
The trained Decision Tree model can be visualized using the `export_graphviz` function from scikit-learn:

```python
from sklearn.tree import export_graphviz

# Visualize the decision tree
export_graphviz(drugTree, out_file='tree.dot', filled=True, feature_names=['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K'])
```

## Contributions
We welcome contributions from the community to improve this project. To contribute, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right of the repository page to create a copy of this repository on your GitHub account.

2. **Clone the Repository**: Clone your forked repository to your local machine.
    ```bash
    git clone https://github.com/your-username/drug-classification-decision-tree.git
    ```

3. **Create a New Branch**: Create a new branch for your feature or bug fix.
    ```bash
    git checkout -b feature-name
    ```

4. **Make Changes**: Make your changes to the codebase.

5. **Commit Your Changes**: Commit your changes with a clear and descriptive commit message.
    ```bash
    git commit -m "Description of your changes"
    ```

6. **Push to Your Branch**: Push your changes to your forked repository.
    ```bash
    git push origin feature-name
    ```

7. **Open a Pull Request**: Open a pull request to merge your changes into the main repository. Provide a detailed description of your changes in the pull request.

We appreciate your contributions and will review your pull request as soon as possible. Thank you for helping improve this project!


## Acknowledgments

Saeed Aghabozorgi

<a href="http://www.linkedin.com/in/idaraabasiudoh" target="_blank">Idara-Abasi Udoh</a>

### Other Contributors

<a href="https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01" target="_blank">Joseph Santarcangelo</a>

<a href="https://www.linkedin.com/in/richard-ye/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01" target="_blank">Richard Ye</a>

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By | Change Description                               |
| ----------------- | ------- | ---------- | ------------------------------------------------ |
| 2024-08-09        | 2.4     | Idara-Abasi Udoh | Project completion                         |
| 2022-05-24        | 2.3     | Richard Ye | Fixed ability to work in JupyterLite and locally |
| 2020-11-20        | 2.2     | Lakshmi    | Changed import statement of StringIO             |
| 2020-11-03        | 2.1     | Lakshmi    | Changed URL of the csv                           |
| 2020-08-27        | 2.0     | Lavanya    | Moved lab to course repo in GitLab               |
|                   |         |            |                                                  |
|                   |         |            |                                                  |

## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
