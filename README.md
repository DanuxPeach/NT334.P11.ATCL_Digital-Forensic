# 📂 NT334.P11.ATCL - File Fingerprinting of the ZIP Format  
### Digital Forensics Project  

## 📌 Project Description  
This project focuses on **file fingerprinting of the ZIP format** to identify and track provenance. The study involves analyzing ZIP file metadata and structure using **zipdetails**, an official forensic tool.  

### 🔍 Key Objectives  
- Utilize **zipdetails** and its dataset to examine ZIP file structures.  
- Perform forensic analysis on both pre-existing ZIP files and self-created test samples.  
- Develop and test Python scripts to modify ZIP file metadata, specifically **extract os**, to bypass forensic detection in zipdetails.  

### 🛠 Tools & Technologies  
- **zipdetails** (Official ZIP forensic tool)  
- **Python** (for forensic bypass experimentation)  
- **ZIP file dataset** (from zipdetails' official repository)  

### 📑 Methodology  
1. **Dataset Analysis:**  
   - Use zipdetails to inspect metadata, structure, and fingerprinting properties of ZIP files.  
2. **Custom ZIP File Testing:**  
   - Create ZIP files with varied structures to analyze their fingerprinting behavior.  
3. **Bypassing Forensic Detection:**  
   - Implement Python scripts to alter **extract os** in ZIP metadata.  
   - Validate if zipdetails detects these modifications.  

### 🚀 How to Run the Python Script  
1. **Install Dependencies**  
   ```sh
   pip install zipfile
   ```
2. **Run the Script**
   ```sh
   python code_change_extract_os.py input.zip output.zip
   ```
3. **Verify the Modified File using zipdetails.**

### 📄 Project Report
**Detailed findings and methodology are documented in:**
- NT334.P11.ATCL-Group8_FinalReport.pdf
- NT334.P11.ATCL-Group8_VideoDemo.mp4 (Demonstration video)
