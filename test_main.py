from main import load_and_summarize_csv


def test_dataset_shape():
    df = load_and_summarize_csv()
    assert df.shape == (5, 4), "Expected 5 rows and 4 columns"


def test_columns_present():
    df = load_and_summarize_csv()
    expected = {"country", "population_millions", "gdp_per_capita_usd", "year"}
    assert expected.issubset(df.columns)


def test_population_positive():
    df = load_and_summarize_csv()
    assert (df["population_millions"] > 0).all()


def test_highest_gdp_is_germany():
    df = load_and_summarize_csv()
    top = df.loc[df["gdp_per_capita_usd"].idxmax(), "country"]
    assert top == "Germany"
