
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('C:/Users/Lenova/OneDrive/ML/StudentsPerformance.csv')

# Streamlit app
def main():
    st.title("Student Performance Analysis")

    # Display Data
    if st.checkbox("Show Dataframe"):
        st.write(df.head())

    # Score Distributions (Histogram)
    st.subheader("Score Distributions")
    score_columns = ["math score", "reading score", "writing score"]
    fig, axes = plt.subplots(1, 3, figsize=(25, 9))
    for i, col in enumerate(score_columns):
        sns.histplot(df[col], bins=20, kde=True, color="skyblue", ax=axes[i])
        axes[i].set_title(f"Distribution of {col}")
    st.pyplot(fig)

    # Average Scores by Gender (Bar Chart)
    st.subheader("Average Scores by Gender")
    avg_scores_by_gender = df.groupby("gender")[score_columns].mean().reset_index()
    avg_scores_melted = avg_scores_by_gender.melt(id_vars="gender", var_name="Subject", value_name="Average Score")
    fig, ax = plt.subplots()
    sns.barplot(x="Subject", y="Average Score", hue="gender", data=avg_scores_melted, palette="coolwarm", ax=ax)
    ax.set_title("Average Scores by Gender")
    st.pyplot(fig)

    # Count Plot: Parental Level of Education
    st.subheader("Parental Level of Education Count")
    fig, ax = plt.subplots()
    sns.countplot(x="parental level of education", data=df, palette="viridis", 
                  order=df["parental level of education"].value_counts().index, ax=ax)
    plt.xticks(rotation=45)
    ax.set_title("Count of Parental Level of Education")
    st.pyplot(fig)

    # Average Scores by Parental Level of Education (Bar Chart)
    st.subheader("Average Scores by Parental Level of Education")
    avg_scores_by_parent_edu = df.groupby("parental level of education")[score_columns].mean().reset_index()
    avg_scores_melted_parent_edu = avg_scores_by_parent_edu.melt(id_vars="parental level of education", 
                                                                  var_name="Subject", value_name="Average Score")
    fig, ax = plt.subplots()
    sns.barplot(x="parental level of education", y="Average Score", hue="Subject", 
                data=avg_scores_melted_parent_edu, palette="viridis", ax=ax)
    plt.xticks(rotation=45)
    ax.set_title("Average Scores by Parental Level of Education")
    st.pyplot(fig)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap of Scores")
    correlation_matrix = df[score_columns].corr()
    fig, ax = plt.subplots()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
    ax.set_title("Correlation Heatmap of Scores")
    st.pyplot(fig)

    # Boxplot for Scores
    st.subheader("Boxplot of Scores")
    fig, ax = plt.subplots()
    sns.boxplot(data=df[score_columns], palette="pastel", ax=ax)
    ax.set_title("Boxplot of Scores")
    st.pyplot(fig)

    # Pie Chart (Gender Distribution)
    st.subheader("Gender Distribution")
    fig, ax = plt.subplots()
    df["gender"].value_counts().plot.pie(autopct="%1.1f%%", colors=["lightblue", "pink"], 
                                          startangle=90, wedgeprops={'edgecolor': 'black'}, ax=ax)
    ax.set_title("Gender Distribution")
    st.pyplot(fig)

    # Scatterplot (Math vs Reading Scores)
    st.subheader("Scatterplot of Math vs Reading Scores")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df["math score"], y=df["reading score"], color="blue", alpha=0.6, ax=ax)
    ax.set_title("Scatterplot of Math vs Reading Scores")
    st.pyplot(fig)

    # Boxplots: Scores based on Parental Level of Education
    st.subheader("Boxplots: Scores by Parental Level of Education")
    fig, axes = plt.subplots(1, 3, figsize=(25, 9))
    for i, col in enumerate(score_columns):
        sns.boxplot(x="parental level of education", y=col, data=df, palette="coolwarm", 
                    order=df["parental level of education"].value_counts().index, ax=axes[i])
        axes[i].set_title(f"{col} Distribution by Parental Education Level")
        axes[i].tick_params(axis='x', rotation=45)
    st.pyplot(fig)


if __name__ == "__main__":
    main()