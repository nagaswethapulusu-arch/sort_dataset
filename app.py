import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sort a Dataset", page_icon="↕️", layout="wide")
st.title("↕️ Sort a Dataset with Pandas")
st.caption("Upload a CSV or use the sample Employee dataset, then sort by one or more columns in ascending or descending order.")

uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
try:
    df = pd.read_csv(uploaded) if uploaded is not None else pd.read_csv("employees.csv")
except Exception as e:
    st.error(f"Could not load the dataset: {e}")
    st.stop()

st.write(f"Total records: **{len(df)}**")

cols = st.multiselect("Sort by (the order you pick matters)", list(df.columns), default=[df.columns[-2]] if len(df.columns) > 1 else [])

if cols:
    orders = []
    left, right = st.columns(2)
    for i, c in enumerate(cols):
        choice = (left if i % 2 == 0 else right).radio(
            f"{c}", ["Ascending", "Descending"], horizontal=True, key=f"order_{c}")
        orders.append(choice == "Ascending")

    result = df.sort_values(cols, ascending=orders, ignore_index=True)
    st.subheader("Code used")
    st.code(f"df.sort_values({cols}, ascending={orders}, ignore_index=True)")
else:
    result = df
    st.info("Choose at least one column to sort by.")

show = st.slider("Rows to show", 5, max(len(df), 6), min(15, len(df)))
st.subheader("Sorted DataFrame")
st.dataframe(result.head(show), use_container_width=True)

with st.expander("Sorting cheat sheet"):
    st.markdown("""
| Goal | Code |
|---|---|
| Ascending | `df.sort_values('salary')` |
| Descending | `df.sort_values('salary', ascending=False)` |
| Two columns | `df.sort_values(['department', 'salary'])` |
| Mixed order | `df.sort_values(['department', 'salary'], ascending=[True, False])` |
| Top N | `df.nlargest(5, 'salary')` |
""")
