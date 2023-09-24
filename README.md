
# RankMyResume

RankMyResume is a Python module that allows you to rank resumes based on their similarity to a given job description. This module currently supports PDF resume files and will soon support DOC and DOCX formats.

## Installation

You can install RankMyResume using pip:

```bash
pip install RankMyResume
```

## Usage

### Importing the Module

```python
from RankMyResume import RankMyResume
```

### Ranking Resumes

```python
# Create an instance of the RankMyResume class
ranker = RankMyResume()

# Provide the job description and the path to the directory containing resume files
job_description = "Your job description text here"
path_to_resumes = "/path/to/resumes"

# Rank the resumes
result_df = ranker.rank(job_description, path_to_resumes)

# Display the ranked resumes
print(result_df)
```

### Note on Supported Formats

- **PDF**: The module currently supports PDF resume files. You can place your PDF resume files in the specified directory.

- **DOC and DOCX (Coming Soon)**: Support for DOC and DOCX resume files will be added in future updates.

## Example

```python
from RankMyResume import RankMyResume

# Create an instance of the RankMyResume class
ranker = RankMyResume()

# Provide the job description and the path to the directory containing resume files
job_description = "We are looking for a Python developer with experience in web development."
path_to_resumes = "/path/to/resumes"

# Rank the resumes
result_df = ranker.rank(job_description, path_to_resumes)

# Display the ranked resumes
print(result_df)
```

## Dependencies

RankMyResume relies on the following Python libraries:

- os
- pdfminer
- sklearn
- pandas

You can install these dependencies using the provided installation instructions.

## License

This module is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Ibrahim

## Feedback and Contributions

Feedback and contributions are welcome! If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/ibrahim-string/RankMyResume).

---

Feel free to customize this README with your information and any additional details about your module. Additionally, if you plan to host your module on a version control platform like GitHub, you can include a link to the repository in the README for users to find the source code and contribute.