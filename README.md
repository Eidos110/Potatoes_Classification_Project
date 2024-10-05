# Potatoes Classification Project

A deep learning project focused on classifying different types of potatoes using the VGG16 architecture, with Data Version Control (DVC) for efficient data and experiment management.

## Project Highlights

- **Goal**: Build a model to accurately classify potato types.
- **Approach**: Leveraged transfer learning with VGG16 for feature extraction and classification.
- **Tools**: DVC was used to track datasets, models, and pipeline reproducibility.

## Project Structure

- **data/**: Raw and processed data files.
- **src/**: Scripts for data preparation, training, and evaluation.
- **dvc.yaml**: DVC pipeline configuration.

## How to Run

1. **Clone Repository**:
   ```sh
   git clone https://github.com/Eidos110/Potatoes_Classification_Project.git
2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
3. **Run the DVC Pipeline**:
   ```sh
   dvc repro

## Results

- **Model Performance**: Achieved high validation accuracy.
- **Evaluation Metrics**: Accuracy, Precision, Recall, and F1-score.

## Future Work

- Experiment with advanced models like ResNet.
- Expand the dataset to include more potato types.
- Deploy using a web service (e.g., Flask) for live classification.

## Tools & Technologies

- **Languages**: Python
- **Libraries**: TensorFlow, OpenCV, scikit-learn
- **Data Management**: DVC

## License

Licensed under the [MIT License](LICENSE).

 
