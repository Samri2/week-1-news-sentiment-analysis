df["date"] = pd.to_datetime(df["date"])

trend = df.groupby([
    df["date"].dt.to_period("M"),
    "sentiment"
]).size().unstack()

trend.plot()

plt.title("Sentiment Trend Over Time")

plt.xlabel("Month")
plt.ylabel("Review Count")

plt.tight_layout()

plt.savefig("../visuals/sentiment_trend.png")

plt.show()