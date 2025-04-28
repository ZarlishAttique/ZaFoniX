# ZaFoniX

ZaFoniX - Personalized Medicine Guide
ZaFoniX is a precision medicine software tool that assists clinicians and researchers in identifying targeted therapies based on genetic test results. It uses curated drug information to suggest FDA-approved, experimental, and investigational drugs associated with specific diseases, genes, or drug names.

Developed by Zarlish Attique.

Features
Secure access with license key authentication (ZAFONIX-1234).

Search functionality for diseases, gene IDs, or drug names.

Filtering options to display:

FDA-approved drugs

Experimental drugs

Investigational drugs

Interactive data visualization:

Drug type distribution

Small molecule vs other types

Top target actions associated with drugs

Detailed search results in a scrollable, sortable table.

Option to export results to CSV or Excel formats.

Clean, professional graphical user interface (GUI) built using Tkinter.

Requirements
Python 3.7+

Required libraries:

tkinter

pandas

matplotlib

Pillow

Install the required Python packages using pip:

bash
Copy
Edit
pip install pandas matplotlib pillow
Usage
Clone or download the ZaFoniX project files.

Ensure you have the input dataset (DrugsList.xlsx) available at the path specified inside the code, or modify the path accordingly.

Run the application:

python zafonix.py
Upon launch, you will be prompted to enter an access key. Enter:

ZAFONIX-1234
Use the search bar to input a gene, disease, or drug name.

Apply optional filters (Approved, Experimental, Investigational) to refine results.

Explore the visual analytics and save search results if needed.

File Structure
zafonix.py – Main application script containing GUI and search functionalities.

DrugsList.xlsx – Excel dataset containing drug information.

Images (optional) – Path to scientist images for GUI display (adjust or remove if images are unavailable).

Notes
Make sure the paths for the dataset and images are correctly set based on your local system.

The tool automatically saves search results when prompted, supporting both CSV and Excel formats.

License
This project is intended for research and educational purposes only. For clinical use, ensure appropriate regulatory approvals from zarlishattiquebi@gmail.com | ranafaraz9266@gmail.com.

Contact
Developer: Zarlish Attique
Email: zarlishattiquebi@gmail.com | ranafaraz9266@gmail.com

