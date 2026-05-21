import pandas as pd
import psycopg2
from config import DB_CONFIG

# Load processed dataset
df = pd.read_csv("data/processed/fintech_reviews_sentiment.csv")

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# =========================
# INSERT BANKS
# =========================
banks = df["bank"].unique()

for bank in banks:
    cur.execute("""
        INSERT INTO banks (bank_name, app_name)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING;
    """, (bank, bank))

conn.commit()

# =========================
# INSERT REVIEWS
# =========================
for _, row in df.iterrows():

    # get bank_id
    cur.execute("SELECT bank_id FROM banks WHERE bank_name = %s", (row["bank"],))
    bank_id = cur.fetchone()[0]

    # insert review
    cur.execute("""
        INSERT INTO reviews (
            bank_id,
            review_text,
            rating,
            review_date,
            sentiment_label,
            sentiment_score,
            identified_theme,
            source
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        bank_id,
        row["review"],
        row["rating"],
        row["date"],
        row["sentiment"],
        0.0,  # placeholder if you didn’t compute score
        ",".join(eval(row["feature_tags"])) if "feature_tags" in row else None,
        row["source"]
    ))

conn.commit()
cur.close()
conn.close()

print("Data inserted successfully into PostgreSQL")