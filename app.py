import streamlit as st
import boto3, pandas as pd
from io import BytesIO

s3 = boto3.client("s3")
BUCKET = "reasey-capstone-2026"

st.title("Diabetes Risk Dashboard")

obj = s3.get_object(Bucket=BUCKET, Key="processed/diabetes_clean.csv")
df = pd.read_csv(BytesIO(obj["Body"].read()))

st.dataframe(df.head())
st.line_chart(df, x="age", y="glucose")

category = st.selectbox("Filter by outcome", df["target"].unique())
st.write(df[df["target"] == category])