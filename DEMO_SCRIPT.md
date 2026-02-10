# Chemical Equipment Visualizer - Demo Video Script
**Target Duration:** 2-3 Minutes

| Time | Visual (Action) | Audio (Narration) |
|------|-----------------|-------------------|
| **0:00-0:15** | **[Intro Screen / Diagrams]**<br>Show the project architecture diagram or a title slide with "Chemical Equipment Parameter Visualizer". | "Hello! Welcome to the demonstration of the Chemical Equipment Parameter Visualizer. This is a hybrid full-stack solution designed to analyze and visualize chemical equipment data using both a modern Web Interface and a native Desktop Application." |
| **0:15-0:30** | **[Features Overview]**<br>Briefly flash the 'Tech Stack' slide or just show the empty Web and Desktop apps side-by-side. | "The project is built with a powerful Django REST Framework backend that serves two distinct frontends: a React.js web dashboard and a PyQt5 desktop app. Both share the same data and authentication system, ensuring a seamless experience across platforms." |
| **0:30-0:50** | **[Web App - Upload]**<br>Open Web App (localhost:3000). Log in. Navigate to 'Upload' tab. Drag and drop `sample_equipment_data.csv`. | "Let's start with the Web Application. After logging in securely, I can navigate to the 'Upload Dataset' section. Here, I'm uploading a CSV file containing flow rates, pressures, and temperatures for various chemical reactors. The system automatically parses and validates this data in real-time." |
| **0:50-1:15** | **[Web App - Visualization]**<br>Click on the new dataset. Show the interactive charts. Hover over bars. Toggle legend items. | "Once uploaded, the data is instantly visualized. We use Chart.js for these interactive dashboards. You can see the distribution of equipment types here, and a detailed multi-parameter comparison below. Notice how responsive the charts are—allowing engineers to quickly identify anomalies in pressure or temperature." |
| **1:15-1:30** | **[Web App - Reporting]**<br>Click 'Download PDF Report'. Open the PDF. Scroll through it. | "For documentation, users can generate professional PDF reports with a single click. These reports include summary statistics and formatted tables, generated on the server using ReportLab, making it easy to share insights with stakeholders." |
| **1:30-1:55** | **[Desktop App - Sync]**<br>Open Desktop App. Log in (emphasize it's the same creds). See the dataset already there. | "Now, let's switch to the Desktop Application. I'm logging in with the exact same credentials. Notice that the dataset I just uploaded on the web is already here. This demonstrates the centralized nature of our Django backend—data is synchronized instantly across all platforms." |
| **1:55-2:15** | **[Desktop App - Visualization]**<br>Open the dataset in Desktop app. Show the Matplotlib charts. Point out the difference in style (native look). | "In the desktop view, we utilize Matplotlib embedded within PyQt5 for high-fidelity scientific plotting. These charts are optimized for offline analysis and provide the granular detail that researchers and engineers often prefer in a native environment." |
| **2:15-2:30** | **[Conclusion]**<br>Show both apps side-by-side or return to Title Slide. | "In summary, this project demonstrates a robust architecture combining the flexibility of React web access with the power of native desktop tools, all unified by a secure Django API. Thank you for watching!" |

## Key Technical Points to Mention (If time permits)
*   **Backend:** Django 4.2 + DRF (Single Source of Truth)
*   **Web:** React 18 + Chart.js (Responsive, Modern)
*   **Desktop:** PyQt5 + Matplotlib (Scientific, Native)
*   **Data:** Pandas for heavy-lifting CSV processing
*   **Reporting:** Automated PDF generation

## Preparation Checklist
1.  **Server:** Ensure Django server is running (`python manage.py runserver`).
2.  **Web:** Ensure React dev server is running (`npm start`).
3.  **Desktop:** Have the PyQt5 app ready to launch.
4.  **Data:** Have `sample_equipment_data.csv` on your desktop for easy drag-and-drop.
5.  **Clean State:** Create a fresh user or delete old test datasets so the dashboard looks clean.
