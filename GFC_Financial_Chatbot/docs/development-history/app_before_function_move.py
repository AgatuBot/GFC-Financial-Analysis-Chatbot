from flask import Flask, render_template, request, jsonify, session
import pandas as pd
import re
import os

app = Flask(__name__)

# Secret key for remembering conversation context
app.secret_key = os.environ.get("GFC_SECRET_KEY", "development-only-secret-key")

# Load financial data
df = pd.read_csv("financial_data.csv")


# -----------------------------
# Helper functions
# -----------------------------

def format_money(value):
    """Convert USD millions into readable USD billions."""
    return f"${value / 1000:,.2f} billion"


def detect_company(text):
    """Identify a company mentioned in the user's question."""
    text = text.lower()

    for company in ["Microsoft", "Tesla", "Apple"]:
        if company.lower() in text:
            return company

    return None


def detect_year(text):
    """Identify a year from 2023â€“2025."""
    years = re.findall(r"\b(2023|2024|2025)\b", text)

    if years:
        return int(years[-1])

    return None


def detect_metric(text):
    """Identify the financial metric requested by the user."""
    text = text.lower()

    if "revenue" in text or "sales" in text:
        return "Total Revenue"

    if "net income" in text or "profit" in text:
        return "Net Income"

    if "assets" in text:
        return "Total Assets"

    if "liabilities" in text:
        return "Total Liabilities"

    if "cash flow" in text or "operating cash" in text:
        return "Operating Cash Flow"

    return None


def get_company_data(company, year, metric):
    """Retrieve one financial data point."""
    result = df[
        (df["Company"] == company)
        & (df["Year"] == year)
    ]

    if result.empty:
        return None

    return result.iloc[0][metric]


def calculate_growth(company, metric, year):
    """Calculate year-over-year growth."""
    if year == 2023:
        return None

    current = get_company_data(
        company,
        year,
        metric
    )

    previous = get_company_data(
        company,
        year - 1,
        metric
    )

    if current is None or previous is None:
        return None

    return ((current - previous) / previous) * 100


# -----------------------------
# Chatbot logic
# -----------------------------

def simple_chatbot(user_query):
    """Process a financial question using rule-based logic."""

    query = user_query.strip()
    lower_query = query.lower()

    # -------------------------
    # Greeting
    # -------------------------

    if lower_query in [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]:
        return (
            "Hello! I can help you analyze financial performance for "
            "Microsoft, Tesla, and Apple from 2023â€“2025. "
            "You can ask about revenue, net income, assets, liabilities, "
            "operating cash flow, growth, or comparisons."
        )

    # -------------------------
    # Check whether the question
    # is related to supported
    # financial topics
    # -------------------------

    financial_keywords = [
        "revenue",
        "sales",
        "net income",
        "profit",
        "assets",
        "liabilities",
        "cash flow",
        "financial",
        "finance",
        "growth",
        "change",
        "compare",
        "company",
        "microsoft",
        "tesla",
        "apple",
        "2023",
        "2024",
        "2025"
    ]

    is_financial_question = any(
        keyword in lower_query
        for keyword in financial_keywords
    )

    # Do not allow unrelated questions to use
    # previously saved financial context.
    if not is_financial_question:
        return (
            "I'm a financial analysis assistant focused on Microsoft, "
            "Tesla, and Apple. I can answer questions about revenue, "
            "net income, assets, liabilities, operating cash flow, "
            "growth, and financial comparisons from 2023â€“2025."
        )

    # -------------------------
    # Detect information in the
    # current question
    # -------------------------

    companies = detect_companies(query)
    company = detect_company(query)
    year = detect_year(query)
    metric = detect_metric(query)

    # Handle multi-company financial questions
    if len(companies) > 1 and metric and year:
        selected_data = df[
            (df["Company"].isin(companies)) &
            (df["Year"] == year)
        ]

        if not selected_data.empty:
            metric_name = metric.replace("Total ", "").lower()
            responses = []

            for company_name in companies:
                row = selected_data[
                    selected_data["Company"] == company_name
                ]

                if not row.empty:
                    value = row.iloc[0][metric]
                    responses.append(
                        f"{company_name}: {format_money(value)}"
                    )

            if responses:
                return (
                    f"{metric_name.capitalize()} in {year}: "
                    + "; ".join(responses)
                    + "."
                )

    # -------------------------
    # Save detected information
    # for follow-up questions
    # -------------------------

    if company:
        session["company"] = company

    if metric:
        session["metric"] = metric

    if year:
        session["year"] = year

    # -------------------------
    # Highest revenue
    # -------------------------

    if (
        "highest revenue" in lower_query
        or "most revenue" in lower_query
    ):
        selected_year = year if year else 2025

        year_data = df[
            df["Year"] == selected_year
        ]

        if year_data.empty:
            return (
                f"I don't have financial data available for "
                f"{selected_year}."
            )

        highest = year_data.loc[
            year_data["Total Revenue"].idxmax()
        ]

        return (
            f"In {selected_year}, {highest['Company']} had the "
            f"highest revenue at "
            f"{format_money(highest['Total Revenue'])}."
        )

    # -------------------------
    # Compare two years
    # -------------------------

    if (
        "compare" in lower_query
        or "difference between" in lower_query
    ):
        if company and metric:

            years = [
                int(y)
                for y in re.findall(
                    r"\b(2023|2024|2025)\b",
                    query
                )
            ]

            if len(years) >= 2:

                year1 = years[0]
                year2 = years[1]

                value1 = get_company_data(
                    company,
                    year1,
                    metric
                )

                value2 = get_company_data(
                    company,
                    year2,
                    metric
                )

                if value1 is not None and value2 is not None:

                    change = value2 - value1

                    if value1 != 0:
                        percentage = (change / value1) * 100
                    else:
                        percentage = 0

                    direction = (
                        "increase"
                        if change >= 0
                        else "decrease"
                    )

                    article = (
                        "an"
                        if direction == "increase"
                        else "a"
                    )

                    metric_name = (
                        metric
                        .replace("Total ", "")
                        .lower()
                    )

                    return (
                        f"{company}'s {metric_name} changed from "
                        f"{format_money(value1)} in {year1} to "
                        f"{format_money(value2)} in {year2}. "
                        f"That represents {article} {direction} of "
                        f"{format_money(abs(change))}, or "
                        f"{abs(percentage):.2f}%."
                    )

        return (
            "To compare financial performance, please specify a "
            "company, metric, and two years. For example: "
            "\"Compare Apple's revenue in 2024 and 2025.\""
        )

    # -------------------------
    # Growth/change questions
    # -------------------------

    if (
        "growth" in lower_query
        or "change" in lower_query
        or "increased" in lower_query
        or "decreased" in lower_query
    ):

        selected_company = (
            company
            or session.get("company")
        )

        selected_metric = (
            metric
            or session.get("metric")
        )

        if selected_company and selected_metric:

            # Specific year:
            # calculate year-over-year growth
            if year:

                growth = calculate_growth(
                    selected_company,
                    selected_metric,
                    year
                )

                if growth is None:
                    return (
                        "Growth cannot be calculated for 2023 because "
                        "the dataset begins in 2023."
                    )

                direction = (
                    "increased"
                    if growth >= 0
                    else "decreased"
                )

                metric_name = (
                    selected_metric
                    .replace("Total ", "")
                    .lower()
                )

                return (
                    f"{selected_company}'s {metric_name} "
                    f"{direction} by {abs(growth):.2f}% "
                    f"from {year - 1} to {year}."
                )

            # No specific year:
            # compare 2023 with 2025
            value_2023 = get_company_data(
                selected_company,
                2023,
                selected_metric
            )

            value_2025 = get_company_data(
                selected_company,
                2025,
                selected_metric
            )

            if (
                value_2023 is not None
                and value_2025 is not None
            ):

                overall_change = (
                    (value_2025 - value_2023)
                    / value_2023
                ) * 100

                direction = (
                    "increased"
                    if overall_change >= 0
                    else "decreased"
                )

                metric_name = (
                    selected_metric
                    .replace("Total ", "")
                    .lower()
                )

                return (
                    f"From 2023 to 2025, {selected_company}'s "
                    f"{metric_name} {direction} by "
                    f"{abs(overall_change):.2f}%. "
                    f"It changed from "
                    f"{format_money(value_2023)} to "
                    f"{format_money(value_2025)}."
                )

    # -------------------------
    # Follow-up questions
    # -------------------------

    if lower_query in [
        "what about 2023?",
        "what about 2024?",
        "what about 2025?",
        "and 2023?",
        "and 2024?",
        "and 2025?"
    ]:

        if (
            session.get("company")
            and session.get("metric")
            and year
        ):

            value = get_company_data(
                session["company"],
                year,
                session["metric"]
            )

            if value is not None:

                metric_name = (
                    session["metric"]
                    .replace("Total ", "")
                    .lower()
                )

                return (
                    f"{session['company']}'s {metric_name} in "
                    f"{year} was {format_money(value)}."
                )

    # -------------------------
    # Direct financial question
    # -------------------------

    selected_company = (
        company
        or session.get("company")
    )

    selected_metric = (
        metric
        or session.get("metric")
    )

    selected_year = (
        year
        or session.get("year")
    )

    if (
        selected_company
        and selected_metric
        and selected_year
    ):

        value = get_company_data(
            selected_company,
            selected_year,
            selected_metric
        )

        if value is not None:

            metric_name = (
                selected_metric
                .replace("Total ", "")
                .lower()
            )

            return (
                f"{selected_company}'s {metric_name} in "
                f"{selected_year} was "
                f"{format_money(value)}."
            )

    # -------------------------
    # Error handling
    # -------------------------

    return (
        "I'm sorry, I couldn't match that question to my "
        "supported financial analysis. You can ask questions "
        "such as: "
        "\"What was Microsoft's revenue in 2025?\", "
        "\"What was Tesla's net income in 2024?\", "
        "\"Compare Apple's revenue in 2024 and 2025.\", or "
        "\"How did Microsoft's net income change?\""
    )


# -----------------------------
# Flask routes
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({
            "response": "Please enter a financial question."
        }), 400

    user_query = data["message"]

    if not isinstance(user_query, str):
        return jsonify({
            "response": "Please enter a valid text question."
        }), 400

    if not user_query.strip():
        return jsonify({
            "response": "Please enter a financial question."
        }), 400

    response = simple_chatbot(user_query)

    return jsonify({
        "response": response
    })


# -----------------------------
# Run Flask application
# -----------------------------

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "0") == "1")


def detect_companies(query):
    """Return all supported companies mentioned in the query."""
    companies = []
    lower_query = query.lower()

    for company in ["Microsoft", "Tesla", "Apple"]:
        if company.lower() in lower_query:
            companies.append(company)

    return companies



