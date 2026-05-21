# Customer Experience Analytics for Fintech Apps

A real-world data engineering and analytics project focused on scraping, processing, and analyzing Google Play Store reviews from Ethiopian banking applications.

---

# Project Objective

This project analyzes customer reviews from the following Ethiopian fintech banking applications:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The goal is to transform raw customer feedback into actionable insights through:

- Web scraping
- Data preprocessing
- Sentiment analysis
- Theme extraction
- Complaint clustering
- Data visualization
- PostgreSQL database engineering

---

# Project Structure

```text
fintech-review-analytics/

├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── data/
│   └── raw/
│
├── notebooks/
│
├── scripts/
│   └── scrape_reviews.py
│
├── src/
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Task 1 — Data Collection and Preprocessing

## Data Source

Reviews were collected from the Google Play Store using the Python library:

- google-play-scraper

---

# Applications Scraped

| Bank | Package Name |
|---|---|
| CBE | com.combanketh.mobilebanking |
| BOA | com.boa.boaMobileBanking |
| Dashen | com.dashen.dashensuperapp |

---

# Fields Collected

The following fields were extracted:

| Column | Description |
|---|---|
| review | User review text |
| rating | Star rating (1–5) |
| date | Review date |
| bank | Bank name |
| source | Review source |

---

# Scraping Methodology

The scraper performs the following steps:

1. Connects to Google Play Store
2. Retrieves reviews for each banking app
3. Extracts:
   - Review text
   - Rating
   - Date
   - App information
4. Combines all reviews into a single dataset
5. Cleans and preprocesses the data
6. Saves the final dataset as CSV

---

# Preprocessing Steps

The following cleaning operations were performed:

- Removed duplicate reviews
- Dropped rows with missing review text
- Dropped rows with missing ratings
- Standardized date format to YYYY-MM-DD
- Trimmed whitespace from review text

---

# Output Dataset

Final cleaned dataset:

```text
data/raw/fintech_reviews_clean.csv
```

Dataset columns:

```text
review
rating
date
bank
source
```
## Task 3: PostgreSQL Database Design

A relational database was implemented using PostgreSQL to store processed fintech review data.

### Database Name
bank_reviews

### Tables

#### banks
Stores bank metadata:
- bank_id (PK)
- bank_name
- app_name

#### reviews
Stores user feedback:
- review_id (PK)
- bank_id (FK)
- review_text
- rating
- review_date
- sentiment_label
- sentiment_score
- identified_theme
- source

---

### Setup Steps
1. Create PostgreSQL database: bank_reviews
2. Run schema file: create_schema.sql
3. Run insert script: insert_data.py

---

### Verification Queries
- Count reviews per bank
- Average rating per bank
- Null value validation
---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/fintech-review-analytics.git
cd fintech-review-analytics
```

---

# Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

## Windows

```bash
.venv\Scripts\activate
```

## Mac/Linux

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Scraper

```bash
python scripts/scrape_reviews.py
```

---

# Expected Output

```text
Scraping reviews for CBE...
Scraping reviews for BOA...
Scraping reviews for Dashen...

Final Dataset Shape: (1200+, 5)

DATASET SAVED SUCCESSFULLY
```

---

# Limitations

- Google Play Store may limit older review availability
- Some reviews may be multilingual
- Certain reviews may be very short or ambiguous
- Review counts can fluctuate over time

---

# Technologies Used

- Python
- pandas
- google-play-scraper
- tqdm
- GitHub Actions

---

# Author

Sam